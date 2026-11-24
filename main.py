"""One-Sentence Absurd Invention Pitch entry.

When run, writes a single-sentence pitch for a ridiculous invention
that fixes a tiny everyday annoyance to /output/entry.txt.
"""

import os

ENTRY = "My toaster ejects burnt bread with a tiny parachute, so breakfast floats gently to the counter instead of setting off the smoke alarm every morning."

OUTPUT_PATH = "/output/entry.txt"


def validate(text):
    """Gate: UTF-8 text of 1 to 220 characters, not only whitespace,
    and exactly one sentence."""
    if not text or not text.strip():
        raise ValueError("entry must not be blank")
    if not 1 <= len(text) <= 220:
        raise ValueError(f"entry must be 1-220 characters, got {len(text)}")
    # Exactly one sentence: a single terminal full stop, and no other
    # sentence-ending punctuation (., !, ?) anywhere else in the text.
    body = text.strip()
    if not body.endswith("."):
        raise ValueError("entry must end with a full stop")
    if sum(1 for ch in body[:-1] if ch in ".!?") > 0:
        raise ValueError("entry must be exactly one sentence")
    return text


def main():
    validate(ENTRY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
