# food-picture-01 — entry

This entry is a finished photograph of a dessert, shot as a tight, warmly lit
close-up so that the food fills the frame and stays appetising even at
thumbnail size, where a judge comparing two food pictures will see it first.

`main.py` at the root of this repository is the whole program the contest runs.
It reads none of that image's content and performs no image processing at all:
it opens the committed `entry.png` beside itself in binary mode and copies the
exact bytes to `entry.png` inside the output directory, taken from
`MAKEFUN_OUTPUT_DIR` and defaulting to `/output`. The copy is byte-for-byte
identical to the committed file every run, which is what the "two runs must
write the same bytes" rule requires. Standard library only, no network, no
randomness, no clock.

Run it:

    MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py

Then, to confirm the bytes are untouched:

    md5sum entry.png /tmp/out/entry.png && cmp entry.png /tmp/out/entry.png
