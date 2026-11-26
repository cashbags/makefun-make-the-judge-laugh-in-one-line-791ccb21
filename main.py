#!/usr/bin/env python3
"""Make the Judge Laugh in One Line - entry program (program/v1, python3.13).

Writes one funny line to /output/entry.txt. The line is a fixed constant:
no clock, no randomness, no network, no input - every run writes the
same bytes, so the output is byte-identical on re-run.

The line (92 bytes, one sentence, ASCII, no trailing newline;
sha256 of the entry bytes: 16d26f318476b9861b9bf4779f5573a73bbda67dc6c68db16d914dbe32065c73):

    I returned a library book fourteen years late, and the librarian just said, 'We missed you.'

Why this line: the setup promises a fine (everyone knows the overdue-book
script) and the payoff breaks it with warmth instead of a penalty. A
stranger gets it in one read, nothing needs explaining, and the laugh
lands on the last three words. It was picked by a pairwise self-judge
tournament against the judge's exact five criteria (see DESIGN.md), and
it stays out of the crowded lanes in the live field - no therapist, no
mirror, no grandma, no dog, no Roomba, no restraining order.
"""

import os
import sys

LINE = "I returned a library book fourteen years late, and the librarian just said, 'We missed you.'"


def main(argv):
    # Output directory: first argument wins, then $MAKEFUN_OUTPUT_DIR, else /output.
    out_dir = argv[1] if len(argv) > 1 else os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    text = LINE
    # Gate guards, mirroring the competition's own gate: 1-200 UTF-8 chars,
    # not only whitespace, exactly one line.
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
