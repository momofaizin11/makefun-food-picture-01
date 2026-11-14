#!/usr/bin/env python3
"""Publish the entry image: copy entry.png from this repository to the output dir.

The image is finished artwork: it is never decoded, re-encoded, resized or
touched in any way. Only the raw bytes travel, so the file the judge sees is
bit-for-bit the file that is committed here.

Environment:
    MAKEFUN_OUTPUT_DIR  where to write (default: /output)
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SOURCE = os.path.join(HERE, "entry.png")
IMAGE_NAME = "entry.png"
DEFAULT_OUTPUT_DIR = "/output"


def fail(message):
    sys.stderr.write("main.py: %s\n" % message)
    return 1


def main():
    if not os.path.isfile(SOURCE):
        return fail("entry image not found next to main.py: %s" % SOURCE)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR
    out_dir = os.path.abspath(out_dir)
    if not os.path.isdir(out_dir):
        os.makedirs(out_dir)
    destination = os.path.join(out_dir, IMAGE_NAME)

    with open(SOURCE, "rb") as src, open(destination, "wb") as dst:
        shutil.copyfileobj(src, dst)
        dst.flush()
        os.fsync(dst.fileno())

    written = os.path.getsize(destination)
    expected = os.path.getsize(SOURCE)
    if written != expected:
        return fail("short write: %d of %d bytes" % (written, expected))

    sys.stderr.write("wrote %s (%d bytes)\n" % (destination, written))
    return 0


if __name__ == "__main__":
    sys.exit(main())
