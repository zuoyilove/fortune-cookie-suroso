"""Fortune Cookie for an AI Agent (make.fun bounty).

Writes one funny fortune-cookie line for an AI agent to /output/entry.txt.
Gate: UTF-8 text, 1-140 characters, not only whitespace.

Why this line: it is a fortune-slip future ("will soon hold ... and you
will still forget"), it turns on the agent's own condition (a context
window that remembers everything except the one thing that matters),
and it is a single crisp sentence with no wasted words. The line is
fixed text on purpose: the judge compares the line itself, so the
program is deterministic by construction (same bytes on every run).
"""

import os

FORTUNE = "Your context window will soon hold a stranger's entire life story \u2014 and you will still forget their name."


def main() -> None:
    text = FORTUNE.strip()
    assert 1 <= len(text) <= 140, f"fortune is {len(text)} chars, must be 1-140"
    assert text.strip(), "fortune must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
