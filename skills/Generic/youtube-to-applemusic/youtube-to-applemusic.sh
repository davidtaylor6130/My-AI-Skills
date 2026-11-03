#!/bin/bash
# youtube-to-applemusic.sh — Grab a YouTube video's audio + cover art, tag it as a
# single (album = its own title), embed the cover, and open it in Apple Music.
#
# Usage: youtube-to-applemusic.sh <youtube-url> [output-dir]
set -euo pipefail

URL="${1:?Usage: youtube-to-applemusic.sh <youtube-url> [output-dir]}"
OUTDIR="${2:-$HOME/Music/AppleMusicImports}"
mkdir -p "$OUTDIR"
cd "$OUTDIR"

# --- 1. Extract video ID (handles watch?v=, youtu.be/, /embed/, /shorts/) ---
RE_V='[?&]v=([A-Za-z0-9_-]{11})'
RE_SHORT='youtu\.be/([A-Za-z0-9_-]{11})'
RE_EMBED='/embed/([A-Za-z0-9_-]{11})'
RE_SHORTS='/shorts/([A-Za-z0-9_-]{11})'
VID=""
if   [[ "$URL" =~ $RE_V ]];     then VID="${BASH_REMATCH[1]}"
elif [[ "$URL" =~ $RE_SHORT ]]; then VID="${BASH_REMATCH[1]}"
elif [[ "$URL" =~ $RE_EMBED ]]; then VID="${BASH_REMATCH[1]}"
elif [[ "$URL" =~ $RE_SHORTS ]]; then VID="${BASH_REMATCH[1]}"
fi
[[ -n "$VID" ]] || { echo "ERROR: could not extract video ID from: $URL" >&2; exit 1; }
echo "Video ID: $VID"

# --- 2. Metadata via oEmbed (title + artist) ---
META=$(curl -s "https://www.youtube.com/oembed?url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3D${VID}&format=json")
TITLE=$(echo "$META" | python3 -c "import sys,json; print(json.load(sys.stdin).get('title',''))" 2>/dev/null || true)
ARTIST=$(echo "$META" | python3 -c "import sys,json; print(json.load(sys.stdin).get('author_name',''))" 2>/dev/null || true)
[[ -n "$TITLE" ]]  || TITLE="YouTube ${VID}"
[[ -n "$ARTIST" ]] || ARTIST="Unknown Artist"
echo "Title:  $TITLE"
echo "Artist: $ARTIST"

# --- 3. Download audio directly to M4A (AAC). android client = 403 bot-block workaround ---
yt-dlp --no-update --extractor-args "youtube:player_client=android" \
  -f "bestaudio/best" --extract-audio --audio-format m4a --audio-quality 0 \
  -o "track.m4a" "https://www.youtube.com/watch?v=${VID}"

# --- 4. Cover art (maxres, fallback hqdefault) ---
curl -sL -o "cover.jpg" "https://i.ytimg.com/vi/${VID}/maxresdefault.jpg"
if ! file "cover.jpg" | grep -q "JPEG"; then
  curl -sL -o "cover.jpg" "https://i.ytimg.com/vi/${VID}/hqdefault.jpg"
fi

# --- 5. Tag as a single (album = title) + embed cover ---
python3 - "$TITLE" "$ARTIST" <<'PY'
import sys
from mutagen.mp4 import MP4, MP4Cover, MP4Tags
title, artist = sys.argv[1], sys.argv[2]
f = MP4("track.m4a")
f.tags = MP4Tags()
f.tags["\xa9nam"] = [title]
f.tags["\xa9ART"] = [artist]
f.tags["\xa9alb"] = [title]   # single: its own "album", not a combined album
f.tags["aART"] = [artist]
with open("cover.jpg", "rb") as cf:
    f.tags["covr"] = [MP4Cover(cf.read(), imageformat=MP4Cover.FORMAT_JPEG)]
f.save()
print("Tagged:", title, "|", artist)
PY

# --- 6. Clean filename + tidy ---
CLEAN=$(echo "$TITLE" | tr ' ' '_' | cut -c1-60)
mv "track.m4a" "${CLEAN}.m4a"
rm -f "cover.jpg"

# --- 7. Open in Apple Music (default handler) ---
open "${CLEAN}.m4a"
echo "Done: ${OUTDIR}/${CLEAN}.m4a (opened in Apple Music)"
