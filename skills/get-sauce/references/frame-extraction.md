# Reference: Visual Frame Extraction

Sometimes the sauce isn't in what someone *said* — it's in what they *showed*. A pixel-art tutorial, a UI demo, an architecture diagram inside a conference talk: the transcript line "and here's what that looks like" is worthless without the image it refers to.

This doc covers the **frame-extraction workflow**: download a YouTube video (or just the segment you need), seek to a timestamp, and pull a single frame as a PNG. Uses tools you already have for `sync.py` (`yt-dlp`, `ffmpeg`).

## When to reach for this

Use frame extraction when **any** of these are true:

- The source is a YouTube tutorial where the verbal commentary is uninformative without the screen recording (pixel art, design, UI, code walkthroughs)
- The user asks "what does X look like?" or "show me the frame at Y minute"
- A transcript references a slide / diagram / image and you need to actually see it
- You're comparing visual styles across multiple operators and need static reference images

**Do NOT use this when:** you're doing a normal sauce hunt for verbal/textual content. The transcript is the cheap and right tool. Frame extraction is heavier (downloads MP4, requires ffmpeg) and pollutes disk with large files.

## Prerequisites

You already have these if `sync.py` works:

- `yt-dlp` — `brew install yt-dlp`
- `ffmpeg` — `brew install ffmpeg`

If `ffmpeg` isn't installed: `brew install ffmpeg`.

## The four-step workflow

### Step 1 — Identify the video and timestamp

You need two things:

1. The YouTube video URL (or video ID)
2. The timestamp (as `HH:MM:SS` or `MM:SS`)

If the user only gives you a vague reference ("the part where MortMort talks about second-shading colors"), check the video description or first comment — YouTube creators often pin a chapter list with timestamps. You can `WebFetch` the watch page to see chapters.

### Step 2 — Download just the segment you need (preferred)

`yt-dlp` supports `--download-sections` to grab just a slice of the video. This is faster, smaller, and the kindest path:

```bash
# Download 10 seconds around the timestamp you care about
yt-dlp \
  --download-sections "*02:25-02:35" \
  -f "bv*[height<=1080]+ba/b[height<=1080]" \
  -o "/tmp/ref-%(id)s.%(ext)s" \
  "https://www.youtube.com/watch?v=VIDEO_ID"
```

- `--download-sections "*02:25-02:35"` — download from 2:25 to 2:35 (the asterisk means "use ffmpeg to cut the section after download"; required for accurate cuts)
- `-f "bv*[height<=1080]+ba/b[height<=1080]"` — cap at 1080p (no need for 4K to grab a single frame, and saves bandwidth)
- `-o "/tmp/ref-%(id)s.%(ext)s"` — write to `/tmp` so you don't pollute the repo

### Step 2 (alternate) — Download the full video

If you need multiple frames from different parts, or the section-download is being weird, just grab the whole thing:

```bash
yt-dlp \
  -f "bv*[height<=1080]+ba/b[height<=1080]" \
  -o "/tmp/ref-%(id)s.%(ext)s" \
  "https://www.youtube.com/watch?v=VIDEO_ID"
```

### Step 3 — Extract the frame with ffmpeg

```bash
# Pull a single frame at exactly 02:30 from the downloaded video
ffmpeg \
  -ss 00:02:30 \
  -i /tmp/ref-VIDEO_ID.mp4 \
  -frames:v 1 \
  -q:v 2 \
  /tmp/frame-VIDEO_ID-02-30.png
```

- `-ss 00:02:30` — seek to 2:30. Putting `-ss` *before* `-i` is fast (it seeks first, then decodes); putting it after is slow but more accurate. Both work for static-frame use cases.
- `-i <input>` — the file you just downloaded
- `-frames:v 1` — emit exactly one video frame
- `-q:v 2` — high quality (PNG is lossless but `q:v` still affects internal sampling)
- Output `.png` is preferred for pixel-perfect reference; use `.jpg` if you need smaller files for a multi-frame sheet

### Step 3 (alternate) — Extract a contact sheet (every Nth second)

If you don't know the exact timestamp and need to scan:

```bash
# One frame every 5 seconds, named sequentially
ffmpeg \
  -i /tmp/ref-VIDEO_ID.mp4 \
  -vf "fps=1/5" \
  -q:v 2 \
  /tmp/sheet-VIDEO_ID-%04d.png
```

Then open the folder and skim visually for the frame you actually want.

### Step 4 — Use it or attach it

- **For your own reference (the agent):** use the `Read` tool — it accepts PNG/JPG and you can describe what's in the frame to the user
- **For the user:** open the file with `open /tmp/frame-VIDEO_ID-02-30.png` (macOS), and they can drag it into wherever they need it (a design tool, a doc, another chat with image input)
- **For inclusion in a sauce-hunt deliverable:** copy the frame into `assets/references/<topic>/<video-id>-<timestamp>.png` and reference it by relative path in your final answer

## Cleanup

Frames and clips can pile up fast. Default storage is `/tmp/` which the OS will clear on reboot, but be explicit:

```bash
# After you're done with a sauce hunt that used frame extraction
rm -f /tmp/ref-*.mp4 /tmp/ref-*.webm /tmp/frame-*.png /tmp/sheet-*.png
```

If you're keeping a frame for the repo, move it to `assets/references/` *before* cleanup.

## Worked example — MortMort tutorial

Say the user asks: _"In MortMort's pixel-art coloring tutorial, what does the canvas look like right after he adds the second shade?"_

You'd:

```bash
# 1. Find the video — let's say it's at https://www.youtube.com/watch?v=ABC123XYZ
# 2. Find the chapter — say "Adding the second shade" starts at 03:15

# 3. Download a 5-second window
yt-dlp \
  --download-sections "*03:13-03:18" \
  -f "bv*[height<=1080]+ba/b[height<=1080]" \
  -o "/tmp/ref-%(id)s.%(ext)s" \
  "https://www.youtube.com/watch?v=ABC123XYZ"

# 4. Extract the frame at 03:15
ffmpeg \
  -ss 00:03:15 \
  -i /tmp/ref-ABC123XYZ.mp4 \
  -frames:v 1 \
  -q:v 2 \
  /tmp/frame-mortmort-second-shade.png

# 5. View it
open /tmp/frame-mortmort-second-shade.png
```

Now you have a static reference image of MortMort's canvas at exactly the moment the second shade is applied. You can describe it, save it to `assets/references/topics/pixel-art/`, or hand it to the user.

## Gotchas

- **Some videos are age-restricted or region-locked.** `yt-dlp` may need a cookies file (`--cookies-from-browser chrome`) to access them. Don't burn cycles fighting it — fall back to asking the user to grab the frame themselves with a browser screenshot.
- **YouTube Shorts** sometimes don't accept `--download-sections` cleanly. Download the full Short (they're tiny) and seek with `ffmpeg`.
- **Aspect ratio**: if the source is 9:16 and you're extracting to a 16:9 context, frame composition will look off. Note the source aspect in your handoff.
- **Frame-accuracy isn't perfect.** If you must hit *exactly* the right frame, put `-ss` AFTER `-i` for accurate-but-slow seeking, or use the contact-sheet approach to scan.
- **Copyright.** Single frames for reference / criticism / education fall under fair use in most jurisdictions, but **do not** redistribute downloaded full videos. Treat the MP4 as ephemeral working storage.

## See also

- [`youtube-transcripts.md`](youtube-transcripts.md) — the verbal-content path; use this when transcripts are the right tool
- [`topics/pixel-art.md`](topics/pixel-art.md) — the topic where frame extraction is most often needed
