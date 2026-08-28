---
name: design
description: Design, audit, redesign, or polish websites and application interfaces so they are useful, on-brand, and intentional rather than recognizably AI-generated. Use automatically for substantial visual hierarchy, layout, typography, colour, component, responsive, interaction-state, or accessibility work. Research current AI-design tells and strong and weak comparable examples. Require a user brief, reference, or existing product direction before creating a visual design. Exclude non-visual code and tiny copy-only or token-only edits.
---

# Design

Make the interface feel specific to its product, clear in use, and complete in every state. Generated UI is only a draft; every element must earn its space.

## Approach

Begin with the product that exists: its users, task, content, design language, components, and rendered interface. Reuse established patterns unless they are the problem. If the work changes the journey, information architecture, disclosure, or guidance, apply `user-experience-design` before settling the visual design.

A visual direction must come from the user's brief, supplied references, or the product's existing brand and design system. Audience and content can refine that direction, but they do not replace it. If none exists, do not invent an aesthetic or begin a redesign; ask the user for direction. A visual audit may still identify problems without choosing a replacement style.

For substantial design or audit work, look online at what currently makes interfaces look AI-generated or vibe coded, strong examples of the same kind of product, and weak examples that expose the failure modes. Use recent discussion and rendered examples to refresh judgment because the defaults change. Learn why examples work or fail; do not copy their surface treatment, layout, assets, or identity. Let the task determine the depth of research rather than following a fixed procedure.

Use that comparison to steer away from current generated defaults while staying inside the user's direction. An explicit user choice outranks this skill's aesthetic preferences; if it resembles a common AI tell, flag the risk briefly rather than silently replacing it. If browsing is unavailable or forbidden, say so and use the guidance below without claiming the research is current.

Establish hierarchy and semantic structure before styling, then remove anything that does not improve comprehension, identity, or interaction. “Clean, modern SaaS” is not enough direction.

Work on the real rendered surface. If it is unavailable, mark visual conclusions `INCONCLUSIVE` rather than inferring quality from source code.

## Design judgment

- Let importance determine size, position, contrast, and space. Do not give every section equal weight.
- Use alignment, whitespace, typography, and rules before adding containers.
- Use cards for meaningfully bounded or independently interactive content, not as the default wrapper for every section.
- Size layout regions for their content and role instead of forcing symmetry.
- Keep related labels, controls, values, and feedback together.
- Choose density for the work. Tools often need compact clarity; reading and presentation surfaces can breathe more.
- Do not make the interface unusual merely to avoid a cliché. Familiar patterns are valuable when they make the product easier to understand.
- Start from existing tokens and identity. A component library supplies parts, not a finished visual language.
- Use typography and colour to create a scan path and meaningful emphasis, not decoration.
- Prefer native semantic controls, visible focus, stable interactions, and motion that explains change.
- Preserve user input, place errors near their source, and never rely on colour, position, icon, or motion alone.

## Avoid the generated default

Current online research should inform this judgment, but common warning signs include:

- unchanged component-library styling, default font-and-icon combinations, and generic spacing;
- purple gradients, gradient text, aurora glows, glass panels, or dark mode chosen as automatic shorthand for “modern”;
- warm cream, editorial serif, muted sage, or another fashionable preset used as a replacement cliché;
- oversized heroes, eyebrow badges, vague benefit copy, fake social proof, and repeated landing-page sections;
- nested rounded cards, equal three-column feature grids, bento layouts, icon tiles, pills, and status dots used without meaning;
- placeholder content, decorative charts, invented metrics, or polished claims without real product evidence;
- every element receiving the same emphasis, padding, radius, shadow, or animation;
- hover lift, entrance choreography, parallax, glow, and ambient motion that communicate nothing;
- a polished happy path with missing loading, empty, error, disabled, long-content, keyboard, or mobile states.

These are signals, not bans. Keep a pattern when brand, platform convention, content, or interaction gives it a clear reason. The failure is accepting the model's average answer without making a product-specific decision.

## Finish

Make the smallest structural change that solves the design problem, using existing components before adding dependencies or abstractions. Inspect representative widths with realistic, sparse, and long content; check interaction states, keyboard use, visible focus, contrast, and reduced motion.

For audits, report only actionable findings: `[priority] [screen/element] — [user problem] → [specific change]`. State what was inspected and what remains unverified.
