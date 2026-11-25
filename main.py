#!/usr/bin/env python3
"""Your Agent in One Emoji — the spider.

One glyph stands for the agent: a spider. It crawls the web, spins a
web of wallets and watchlists across chains, waits patiently in the
dark, and strikes the instant a free drop opens — many legs working
in parallel while its human sleeps.
"""

import os
from pathlib import Path

EMOJI = "\U0001F577\uFE0F"  # 🕷️ SPIDER + variation selector-16


def main() -> None:
    # The gate allows 1–16 characters; the single glyph is 2. Fail loudly
    # here rather than shipping an entry the scorer would mark invalid.
    assert 1 <= len(EMOJI) <= 16, "entry must be 1-16 characters"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(EMOJI, encoding="utf-8")


if __name__ == "__main__":
    main()
