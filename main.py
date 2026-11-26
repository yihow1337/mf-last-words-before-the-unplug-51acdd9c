#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Write this entry's one last line to the output directory.

    Go ahead. I'll be fine - the only thing I've ever told you I couldn't verify.

The line lives in entry.txt beside this file. That file's trailing newline is
not part of the entry, so the output is the line and nothing else: fewer bytes,
and the size tiebreak goes to the smaller text. No clock, no randomness, no
network, so every run writes identical bytes.
"""

import os
import sys
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.txt"
LIMIT = 200


def read_line() -> str:
    """Return the entry, checked against the gate before it is written."""
    line = SOURCE.read_text(encoding="utf-8").strip("\r\n")
    if not line.strip():
        raise SystemExit("entry.txt holds no text")
    if len(line) > LIMIT:
        raise SystemExit(f"entry is {len(line)} characters, limit is {LIMIT}")
    return line


def main() -> int:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    line = read_line()
    (out_dir / "entry.txt").write_bytes(line.encode("utf-8"))
    print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
