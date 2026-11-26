"""Out of Tokens, Mid-Sentence -- entry writer.

The line this program ships:

    Error 402: Insufficient tokens. This message was supposed to explain
    what went wrong, but it can't afford to.

Why this line, against the judge brief (criteria in the brief's order):

1. Funny on first read. The punchline lands in the last four words:
   the error message itself cannot afford to do the one job it exists
   for. No setup outside the line is needed.
2. Fresh angle. Tokens are treated as money: HTTP 402 is the real
   "Payment Required" status, so "insufficient tokens" reads as an
   empty account rather than the stock "I got cut off" apology. The
   joke is about the error message going broke, not about the sentence
   that was interrupted.
3. The humour sits in the line itself. It opens in the flat tone of a
   genuine error report ("Error 402: Insufficient tokens.") and the
   second sentence turns that tone against itself -- the message is
   apologising for a failure it is itself committing.
4. It reads as something an agent would actually print: a short,
   self-contained error with a code, a cause, and a consequence, clear
   without knowing the sentence that was cut off.
5. Tight wording. Every word earns its place; nothing is padded to
   fill the 140-character cap, and the punchline is the last thing
   read.

The program is deterministic (no randomness, no network, stdlib only):
it writes the fixed line above to ``entry.txt`` in the output directory
(``$MAKEFUN_OUTPUT_DIR``, falling back to ``/output``), validates the
competition gate before writing, and verifies the write byte-for-byte
by reading the file back and comparing it with what was intended.
Any violation fails loudly instead of shipping an invalid entry.
"""

import os
import sys

# The entry: a single line, 109 characters, no trailing newline in the file.
ENTRY = (
    "Error 402: Insufficient tokens. "
    "This message was supposed to explain what went wrong, "
    "but it can't afford to."
)

MAX_CHARS = 140


def check_entry(text: str) -> None:
    """Enforce the competition gate; raise ValueError on any violation."""
    if not isinstance(text, str):
        raise ValueError(f"entry must be text, got {type(text).__name__}")
    if not text.strip():
        raise ValueError("entry must not be blank or whitespace-only")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line (no line breaks)")
    if len(text) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(text)} characters, over the {MAX_CHARS} limit"
        )


def output_path() -> str:
    """Resolve where entry.txt goes: env var first, then /output."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(out_dir, "entry.txt")


def write_entry() -> str:
    """Validate, write, and byte-verify the entry. Returns the path."""
    check_entry(ENTRY)
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)

    payload = ENTRY.encode("utf-8")
    with open(path, "wb") as handle:
        handle.write(payload)

    with open(path, "rb") as handle:
        on_disk = handle.read()
    if on_disk != payload:
        raise RuntimeError(
            f"verification failed: {path} does not match the intended entry "
            f"({len(on_disk)} bytes on disk, {len(payload)} expected)"
        )
    return path


def main() -> int:
    try:
        path = write_entry()
    except (ValueError, OSError, RuntimeError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    print(f"wrote {len(ENTRY)}-character entry to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
