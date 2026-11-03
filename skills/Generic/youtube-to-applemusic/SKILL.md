---
name: youtube-to-applemusic
description: |
  Take a YouTube video URL and turn it into a working single in Apple Music:
  grabs the audio, grabs the thumbnail as cover art, tags it (title, artist,
  album = its own title so it's a single, not a combined album), embeds the
  cover, and opens it in Apple Music. Use when the user gives a YouTube link
  and wants the song/audio added to Apple Music, or wants the audio + album art
  grabbed from a YouTube video.
---

# YouTube → Apple Music

Turn a YouTube video into a tagged single in Apple Music, in one command.

## When to use
- User gives a YouTube URL and wants the song in Apple Music
- User wants the audio + cover art grabbed from a YouTube video

## How
Run the helper script with the YouTube URL (and optionally an output dir):

```bash
bash <skill-dir>/youtube-to-applemusic.sh "<youtube-url>" [output-dir]
```

Default output dir is `~/Music/AppleMusicImports/`.

The script does, in order:
1. Extract the video ID (handles `watch?v=`, `youtu.be/`, `/embed/`, `/shorts/`)
2. Get title + artist via the oEmbed API
3. Download the audio directly to M4A (AAC) via yt-dlp — uses the `android` player client to get past YouTube's 403 bot-block
4. Download the cover art (`maxresdefault.jpg`, fallback `hqdefault.jpg`)
5. Tag as a single: title, artist, **album = title** (so it's its own single, not a combined album), and embed the cover — via mutagen, which writes to the correct MP4 atoms Apple Music reads
6. Open it in Apple Music via `open`

## Requirements (all present on this machine)
- `yt-dlp`, `ffmpeg`, `curl`, `python3` with `mutagen`

## Notes
- If a track shows stale/wrong in Apple Music, delete the old track and re-open the new file (Apple Music can cache the old version).
- Album is set to the title (single convention). If the user wants a combined album instead, set the `©alb` tag to the shared album name.
- The `open` step hands the file to the default handler; on this Mac that imports it into Apple Music.
