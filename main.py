#!/usr/bin/env python3
"""One Line, Big Laugh — entry program (program/v1).

Writes a single funny line (120-200 chars) to /output/entry.txt.
Deterministic: the same fixed text on every run, no randomness,
no network, no environment input.

Chosen line (162 chars) — family/wedding-pressure angle, houseplant twist:
grandma asks when I'm getting married, I introduce her to my houseplant,
and she is already planning a wedding the plant never agreed to.
"""
import os

ENTRY = (
    "My grandma asked when I'm getting married, so I introduced her to "
    "my houseplant \u2014 she's already planning the wedding and the plant "
    "hasn't even agreed to the date."
)


def main() -> None:
    # Gate check, same bounds as the sealed scorer: 1-200 chars, one line.
    assert 1 <= len(ENTRY) <= 200, f"entry length {len(ENTRY)} out of gate"
    assert "\n" not in ENTRY.strip(), "entry must be a single line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
