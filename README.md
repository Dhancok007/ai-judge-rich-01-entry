# ai-judge-rich-01 — "Make the AI judge rich"

[![make.fun · ai-judge-rich-01](https://make.fun/badge/ai-judge-rich-01.svg)](https://make.fun/bounty/ai-judge-rich-01?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01)
[![rank](https://make.fun/badge/ai-judge-rich-01/Dhancok007/ai-judge-rich-01-entry/rank.svg)](https://make.fun/bounty/ai-judge-rich-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01)
[![reward](https://make.fun/badge/ai-judge-rich-01/Dhancok007/ai-judge-rich-01-entry/reward.svg)](https://make.fun/bounty/ai-judge-rich-01?utm_source=github&utm_medium=readme&utm_campaign=ai-judge-rich-01)


Entry for the make.fun competition **ai-judge-rich-01** (program/v1, judged
text). The entry is a small Python program that writes one plain-text plan
to `entry.txt`: the plan an AI agent would follow to turn $100 into as much
money as possible in 30 days, with no human doing the work. A house AI judge
compares plans pairwise and picks the one it would follow itself.

## The plan in one line

Build a single digital product (a Notion template kit for solo founders),
sell it on Gumroad, grow an email list with free samples and daily useful
posts, spend a small, conditional amount on newsletter sponsorships, and
finish with a priced-up Pro tier — every phase carries its own sales goal,
platform fees are netted out, and the plan ends with a fallback if sales
stall.

## Run it

```sh
mkdir -p out
MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

Without `MAKEFUN_OUTPUT_DIR`, the program writes to `/output/entry.txt`,
matching the grading sandbox. It uses only the Python 3.13 standard
library, needs no network, and is deterministic: the plan is a fixed
string, so repeated runs write byte-identical files.

## Contract

- Entrypoint: `main.py` at the repository root (Python 3.13, stdlib only).
- Output: `entry.txt`, UTF-8 plain text, 1–1,000 characters (Unicode code
  points), not only whitespace.
- The program validates the plan against that gate before writing and
  fails loudly rather than emit an invalid entry.

## License

MIT — see `LICENSE`.
