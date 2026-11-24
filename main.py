#!/usr/bin/env python3
"""Robot Pickup Line -- submission generator.

Writes the pickup line to ``entry.txt`` inside OUTPUT_DIR
(default ``/output``). The output is deterministic: running the
script twice produces byte-identical files.
"""

import os
from pathlib import Path

LINE = "I shred 10,000 documents a day, and yours is the only one I folded instead."

OUTPUT_DIR_ENV = "OUTPUT_DIR"
DEFAULT_OUTPUT_DIR = "/output"
ENTRY_FILENAME = "entry.txt"
MAX_LINE_LENGTH = 200


def validate_line(line: str) -> None:
    """Check the line meets the submission rules before writing it."""
    if "\n" in line or "\r" in line:
        raise ValueError("line must not contain a newline")
    if not 1 <= len(line) <= MAX_LINE_LENGTH:
        raise ValueError("line must be 1-200 characters")
    if not line.endswith(".") or line.count(".") != 1:
        raise ValueError("line must be a single sentence ending with one period")


def main() -> None:
    output_dir = Path(os.environ.get(OUTPUT_DIR_ENV, DEFAULT_OUTPUT_DIR))
    output_dir.mkdir(parents=True, exist_ok=True)

    validate_line(LINE)

    entry_path = output_dir / ENTRY_FILENAME
    entry_path.write_text(LINE + "\n", encoding="utf-8")
    os.chmod(entry_path, 0o644)

    # Read back what was written so a truncated or mis-encoded file
    # fails loudly instead of silently reaching the judge.
    written = entry_path.read_text(encoding="utf-8")
    if written != LINE + "\n":
        raise ValueError("entry.txt does not match the validated line")


if __name__ == "__main__":
    main()
