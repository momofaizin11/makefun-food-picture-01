# NOTES — food-picture-01

## What the picture is

A single square photograph of a dessert, shot as a tight close-up: the subject
fills the frame, there is no scenery, no plate rim competing for attention, no
props. That framing is the whole idea of the entry. A judge looking at two food
pictures side by side spends a fraction of a second on each, so the image has to
land at thumbnail size before it lands at full size.

## Why it is dressed and lit this way

- Close-up. At 1024x1024 a wide shot of a table would leave the food occupying
  a small patch of pixels. Cropping in means every pixel in the frame is doing
  work for the subject, so appetite appeal survives being scaled down.
- Warm, directional light. Food reads as appetising when it looks lit from one
  side rather than flat: the warm side highlights the surface sheen and the
  far side falls into soft shadow, which gives the dessert volume instead of
  flattening it into a coloured blob.
- Glossy, high-saturation surfaces. Caramel, cream, fruit and syrup are the
  parts of a dessert that signal freshness. Keeping specular highlights sharp
  and colours warm and saturated is what makes the eye read "just made" rather
  than "catalogue photo".
- Clean composition, nothing busy. There is one obvious focal point. In a
  pairwise comparison that is what a judge can actually see and articulate, and
  it is why this entry is dressed restrained rather than styled heavily.

## How the file is copied

`main.py` is a copier and nothing else. It resolves the repository directory
from `os.path.abspath(__file__)`, never from the working directory, opens
`entry.png` beside itself in binary mode, and streams the bytes into
`<output>/entry.png` with `shutil.copyfileobj`. The output directory comes from
`MAKEFUN_OUTPUT_DIR`, falling back to `/output`, and is created only if it does
not already exist.

No image library is imported, the file is never decoded, never resized and
never re-encoded. That is deliberate: any decode-and-resave round trip can
change bytes, and this contest requires the two runs to produce identical
output. Copying raw bytes makes bit-for-bit equality structural rather than
hopeful.

One detail worth recording: the committed file is named `entry.png` but its
content is JPEG-encoded (magic `ff d8 ff`), 1024x1024, 193059 bytes. That is
irrelevant to the copy — bytes are bytes — and it is deliberately left as is.
Renaming or re-encoding it would change the bytes, so the mismatch is preserved
rather than "fixed".

## What was verified

- md5 of `entry.png` in the repository, of run 1 and of run 2 are all
  `a1842fe84f159d568a7fb528373e1a4e`.
- `cmp` reports the copies identical to the repository file and to each other,
  so two runs write the same bytes.
- Run without `MAKEFUN_OUTPUT_DIR` set falls back to `/output` and succeeds.
- Run with the image absent exits 1 with a clear message naming the missing
  path, and writes nothing.
