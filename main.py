#!/usr/bin/env python3
"""Write the make.fun entry text to entry.txt."""

import os
import sys
from pathlib import Path

TEXT = (
    "Five stars. He asked me to summarize his day. I wrote: argued with a "
    "toaster, lost. He said add nuance. I wrote: twice."
)


def main() -> None:
    assert 1 <= len(TEXT) <= 280, f"text must be 1..280 characters, got {len(TEXT)}"
    out_dir = Path(
        os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR") or "/output"
    )
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))
    print(len(TEXT), file=sys.stderr)


if __name__ == "__main__":
    main()
