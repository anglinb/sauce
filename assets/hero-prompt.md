# Hero Image — Generation Prompt

This folder contains everything you need to generate the `sauce` repo hero image in ChatGPT (or any vision-capable image model — DALL-E 3, Sora, Midjourney with `/blend`, etc.).

## How to use

1. Open ChatGPT (with image generation enabled, GPT-5 or newer)
2. Attach **all 12 reference images** from `assets/references/` to the chat
3. Paste the **prompt** below
4. Iterate from there — see "Iteration tips" at the bottom

> ⚠️ Some models will refuse to render real named public figures. If that happens, swap "as named below" with "as stylized characters inspired by the attached photos" — the model will then use the refs for *style and identity flavor* without reproducing any one person's likeness.

---

## The prompt

> A vibrant, cinematic editorial-poster illustration in a 16:9 widescreen composition. At the dead center, a tall, glossy hot-sauce bottle (Sriracha/Tabasco silhouette, with a black screw cap and a curved neck) is filled with viscous, glowing molten-orange sauce that emits a soft inner light, as if radioactive with knowledge.
>
> Above and around the bottle, a massive swirling vortex of small floating objects spirals down into the bottle's open neck like a galaxy collapsing into a singularity. The vortex is made of:
>
> - tiny stylized podcast microphones (Shure SM7B-style, in chrome and black)
> - small square video thumbnails with red YouTube-style play buttons in the corner
> - speech bubbles
> - audio waveforms rendered as ribbons of golden light
> - and — most importantly — small illustrated portrait medallions of recognizable founders and operators, each rendered as a stylized 1-inch circular bust (think: Pixar-meets-Saturday-Evening-Post illustration). Use the attached reference photos as the basis for who each portrait depicts, drawn in a consistent illustrated style (NOT photo-realistic). Render approximately 12 portraits, scattered through the swirl. Reference cast:
>   - **Sam Altman** (OpenAI) — short brown hair, gray crewneck or button-down vibe
>   - **Paul Graham** (Y Combinator) — bearded, thoughtful, classic essayist look
>   - **Naval Ravikant** — close-cropped beard, serene expression
>   - **Patrick Collison** (Stripe) — younger, redhead, focused
>   - **Brian Chesky** (Airbnb) — designer-CEO energy, clean-cut
>   - **Marc Andreessen** (a16z) — bald, broad, statesman vibe
>   - **Reid Hoffman** (LinkedIn / Greylock) — round face, glasses, blazer
>   - **Tim Ferriss** — wavy hair, podcast-host warmth
>   - **Lex Fridman** — black t-shirt, dark hair, intense gaze
>   - **DHH** (Basecamp / Rails) — confident, slightly punk-tech energy
>   - **Ben Horowitz** (a16z) — bald, glasses, gravitas
>   - **Garry Tan** (Y Combinator president) — younger, energetic
>
> The portraits and icons get smaller and denser as they spiral toward the bottle's neck, creating a sense of compression and convergence — like all this collective wisdom is being distilled down into the sauce.
>
> From the bottle's tip, a single thick, gleaming drop is falling toward the bottom of the frame. Inside the drop, a tiny glowing lightbulb is visible — the metaphor: a single droplet of distilled wisdom.
>
> The bottle has a small visible label in the front (illegible script or simple wordmark — do NOT render readable text), in a vintage condiment-label style.
>
> **Color palette:** deep navy-blue background gradient (lighter toward the bottle, darker at the corners) with subtle starlike specks; vibrant orange-red and amber for the sauce and its glow; gold highlights on the audio ribbons; warm skin tones on the illustrated portraits.
>
> **Style:** crisp vector-illustration meets editorial magazine cover, slight grain texture, bold confident lines, NOT photo-realistic, NOT 3D-rendered. Think: a New Yorker cover crossed with a Pixar still crossed with classic Mad Magazine swirl-of-detail energy. Cinematic depth, soft glow on the sauce, dramatic chiaroscuro.
>
> **Aspect ratio:** 16:9 widescreen, suitable as a GitHub README banner.
>
> **No readable text anywhere in the image.** The label on the bottle should be a stylized squiggle, not legible words.

---

## Iteration tips

If the first generation isn't right, try these targeted edits (paste as a follow-up message to the same chat):

- **Bottle wrong shape:** _"Make the bottle taller and narrower, more like a vintage Tabasco bottle. The cap should be matte black, not red."_
- **Portraits too small / unrecognizable:** _"Make the founder portraits larger and clearer — about 8% of the canvas each, with enough detail that they're visibly inspired by the reference photos. Keep them in the swirl but bring the closest ones forward."_
- **Sauce wrong color:** _"The sauce should be a richer amber-orange, like clover honey lit from within. Add a stronger inner glow."_
- **Too cluttered:** _"Reduce the number of icons by half. Keep all 12 portraits but space them more generously through the swirl."_
- **Too cluttered (alt):** _"Drop the audio waveforms; keep only the podcast mics, portraits, and play-button thumbnails."_
- **Wrong vibe:** _"Make the lighting darker and more cinematic — like a movie poster. Push the navy background closer to black at the edges."_
- **Need text added later:** Don't ask the model — add the word **SAUCE** in Photoshop/Figma after generation. AI text rendering is still unreliable for hero images.

## Output recommendations

- **GitHub README banner:** 1500×500 (3:1) — crop the 16:9 generation
- **OpenGraph card:** 1200×630 — re-crop or regenerate at this ratio
- **Final file:** save at `assets/hero.png` in the repo, then add to `README.md`:
  ```markdown
  <p align="center">
    <img src="assets/hero.png" alt="Sauce — distilled operator wisdom" width="100%" />
  </p>
  ```

## Reference image attribution

All reference photos under `assets/references/` are sourced from Wikipedia / Wikimedia Commons and used here as visual references for AI image generation only. They are not redistributed as standalone media. See each image's Wikimedia page for license details (most are CC-BY-SA).
