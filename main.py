#!/usr/bin/env python3
"""The One-Line Cat Joke That Lands (make.fun).

Writes a single cat joke — one line, under 200 characters — to
/output/entry.txt. The joke is a fixed, hand-written line: deterministic,
no network, no randomness, no environment input.
Why this joke: the setup (a cat leaving a dead mouse on the pillow)
reads as the familiar "gift" trope, then the turn reframes it as a
performance review — a fresh angle with a surprise, short enough to
retell to a friend the same day, and no explanation after the punchline.
"""

import os

JOKE = "My cat left a dead mouse on my pillow at 3 a.m. \u2014 not as a gift, as a performance review."


def main() -> None:
    text = JOKE.strip()
    assert 1 <= len(text) <= 200, f"joke must be 1-200 chars, got {len(text)}"
    assert "\n" not in text, "joke must be a single line"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
