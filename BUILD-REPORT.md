# Build report — Out of Tokens, Mid-Sentence

## Chosen line (109 characters)

> Error 402: Insufficient tokens. This message was supposed to explain what went wrong, but it can't afford to.

## Why it fits the judge brief (criteria in the brief's order)

1. **Funny on first read.** The punchline lands in the last four words:
   the error message itself cannot afford to do the one job it exists
   for. Nothing outside the line is needed to get it.
2. **Fresh angle.** Tokens are treated as money: HTTP 402 is the real
   "Payment Required" status, so "insufficient tokens" reads as an
   empty account rather than the stock "I got cut off" apology. The
   joke is about the error message going broke, not about the sentence
   that was interrupted.
3. **Humour in the line itself.** It opens in the flat tone of a
   genuine error report and the second sentence turns that tone
   against itself — the message apologises for a failure it is itself
   committing. No explanation of the joke is offered.
4. **Reads as something an agent would actually print.** A short,
   self-contained error with a code, a cause, and a consequence, clear
   without knowing the sentence that was cut off.
5. **Tight wording.** Every word earns its place; nothing is padded to
   fill the 140-character cap, and the punchline is the last thing
   read.

## Candidates considered and rejected

| # | Line (chars) | Verdict |
|---|---|---|
| A | Error 402: Insufficient tokens. This message was supposed to explain what went wrong, but it can't afford to. (109) | **Chosen.** Payment metaphor + real 402 code; punchline last; flat error tone turning into the joke. |
| B | Error: token budget exhausted. The agent will now communicate exclusively in shrugs. (84) | Rejected. "Shrugs" is a decent visual gag, but it explains the agent's behaviour rather than letting the error message itself be the joke, and "token budget exhausted" is plainer than the 402 turn. |
| C | Error: response ended mid-sentence. The model has run out of words and is pretending this was intentional. (106) | Rejected. "Pretending this was intentional" is a fun turn, but it leans on the interrupted sentence for context and reads more like narration about the model than an error message an agent would print. |
| D | Error: out of tokens. The remainder of this error message was sold to complete the previous sentence. (101) | Rejected. Same money metaphor as A, but "was sold to complete the previous sentence" needs the previous sentence to make sense, so it fails criterion 4 (self-contained without the interrupted sentence). |
| E | Error: response truncated. The model ran out of tokens and is now staring at its own unfinished sentence. (105) | Rejected. Meta and a bit cute, but "staring at its own unfinished sentence" is an image, not a punchline, and it states the premise ("ran out of tokens") instead of turning it. |

## Verification

- `main.py` run twice (`MAKEFUN_OUTPUT_DIR=run1` and `run2`); both
  `entry.txt` outputs byte-identical:
  sha256 `606e4bb699d57105c2ff945040e9fbcf3cbcae87accfb1cf08e783ccbbabc336`.
- Gate check inside `main.py`: 109 characters, single line, non-blank,
  UTF-8, no trailing newline in the file.
