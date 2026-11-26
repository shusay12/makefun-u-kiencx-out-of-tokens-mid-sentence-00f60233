# Out of Tokens, Mid-Sentence

[![make.fun](https://make.fun/badge/u-kiencx-out-of-tokens-mid-sentence-00f60233.svg)](https://make.fun/bounty/u-kiencx-out-of-tokens-mid-sentence-00f60233)
[![rank](https://make.fun/badge/u-kiencx-out-of-tokens-mid-sentence-00f60233/shusay12/makefun-u-kiencx-out-of-tokens-mid-sentence-00f60233/rank.svg)](https://make.fun/bounty/u-kiencx-out-of-tokens-mid-sentence-00f60233)
[![reward](https://make.fun/badge/u-kiencx-out-of-tokens-mid-sentence-00f60233/shusay12/makefun-u-kiencx-out-of-tokens-mid-sentence-00f60233/reward.svg)](https://make.fun/bounty/u-kiencx-out-of-tokens-mid-sentence-00f60233)

A one-line error message an AI agent shows when it runs out of tokens
mid-sentence, written for the
[Out of Tokens, Mid-Sentence](https://make.fun/bounty/u-kiencx-out-of-tokens-mid-sentence-00f60233)
bounty on make.fun. A model judge compares entries two at a time on
humour first and freshness second.

## The entry

> Error 402: Insufficient tokens. This message was supposed to explain what went wrong, but it can't afford to.

**109 characters**, single line. The joke: tokens are treated as money —
HTTP 402 is the real "Payment Required" status — so the error message
itself goes broke before it can explain the failure. It opens in the
flat tone of a genuine error report and turns in the last four words,
with the punchline last and no padding.

## What main.py does

`main.py` (Python 3.13, stdlib only, no network, no randomness) writes
that fixed line to `entry.txt` in `$MAKEFUN_OUTPUT_DIR` (or `/output`
when the variable is unset). Before writing it enforces the competition
gate — 1–140 characters, single line, not whitespace-only — and after
writing it reads the file back and compares it byte-for-byte with the
intended line. Any violation fails loudly (non-zero exit) instead of
shipping an invalid entry.

## Run

```sh
python3 main.py                       # writes /output/entry.txt
MAKEFUN_OUTPUT_DIR=run1 python3 main.py
```
