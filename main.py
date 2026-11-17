#!/usr/bin/env python3
"""Entry for ai-judge-rich-01 ("Make the AI judge rich").

Writes one plain-text money-making plan to entry.txt inside the output
directory (MAKEFUN_OUTPUT_DIR when set, otherwise /output). The plan is a
fixed string, so every run produces exactly the same bytes. The text is
plain UTF-8, well under the 1,000-character gate, and never only
whitespace. Standard library only; no network, no input, no clock.
"""

import os
import sys
from pathlib import Path

PLAN = """I start with $100 and build one product I can make and sell entirely on my own: a Solo Founder Launch Kit - 40 Notion templates (roadmap, pricing, launch checklist) plus 25 proven landing-page headlines - sold on Gumroad at $29. Gumroad keeps 10%, so I net $26.10 a sale.
Days 1-4: Build the kit and sales page. Costs: $12 domain, $6 email tool. Cash left: $82.
Days 5-11: Give 3 templates away free to build an email list; post one useful answer a day in founder communities and one thread a day on X. Goal: 300 subscribers and my first 15 sales = $392.
Days 12-20: Launch on Product Hunt and to the list. Spend $40 on two sponsored slots in small founder newsletters. Goal: 35 more sales = $914.
Days 21-30: Ship a free update, collect testimonials, add a $34 Pro tier. Goal: 25 more sales = $765 after fees.
Total: 75 sales, $2,071 revenue, $58 costs. I end day 30 with about $2,113. If I have under 20 sales by day 15, I skip the ads, cut the price to $19, and double the posting."""


def check_plan(text: str) -> None:
    """Fail loudly instead of writing a plan the gate would reject."""
    if not text.strip():
        raise ValueError("plan is only whitespace")
    if not 1 <= len(text) <= 1000:
        raise ValueError(f"plan is {len(text)} characters, outside 1..1000")
    text.encode("utf-8")  # raises if the text cannot be encoded as UTF-8


def main() -> int:
    check_plan(PLAN)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    with open(target, "w", encoding="utf-8", newline="") as handle:
        handle.write(PLAN)
    return 0


if __name__ == "__main__":
    sys.exit(main())
