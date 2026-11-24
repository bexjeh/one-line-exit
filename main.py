"""The One-Line Exit — a single-line resignation letter.

Writes exactly one funny resignation letter to entry.txt.
Deterministic, self-contained: no network, no clock, no environment
dependence beyond the output directory.
"""

import os

LETTER = (
    "I resign as the office plant waterer \u2014 the ficus got promoted "
    "over me, and I refuse to report to a plant."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "."
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LETTER)


if __name__ == "__main__":
    main()
