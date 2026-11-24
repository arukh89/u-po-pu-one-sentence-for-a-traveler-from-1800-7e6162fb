"""One Sentence for a Traveler from 1800 — write the sentence to
/output/entry.txt.

The sentence (139 characters, 139 bytes, plain ASCII):

    It is a book that writes back: ask it a question, and it answers
    at once, and anything you write in it may be read in every house
    on earth.

One image, built only from things a person from 1800 already knows:
a book. The book answers questions at once (what the internet does),
it writes back (two-way: you can ask, and you can write in it), and
what you write in it may be read in every house on earth (everyone,
everywhere, instantly). "May be" keeps the claim literally true: a
public word can be read anywhere; nothing here claims every page or
every answer exists. No word in the sentence was coined after 1800,
no list of features is crammed in, and the sentence stands alone.
"""

import os

# One comparison carries the whole sentence: a book that writes back.
# 139 characters, 139 bytes, plain ASCII (bytes equal characters, which
# helps the size tie-break). The turn is the book answering: it covers
# asking (reading / searching), answering at once (instant), and being
# read in every house on earth (publishing to everyone).
ENTRY = (
    "It is a book that writes back: ask it a question, and it answers "
    "at once, and anything you write in it may be read in every house "
    "on earth."
).encode("utf-8")


def main():
    # The gate only accepts 1-200 characters of non-blank UTF-8 text.
    text = ENTRY.decode("utf-8")
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.strip(), "entry must not be only whitespace"
    assert text == text.strip(), "no leading/trailing whitespace"
    assert "\n" not in text, "entry must be a single sentence on one line"
    # The sentence must survive as written: one book image, the
    # question-and-answer turn, and the every-house close — no stray
    # whitespace or doubled spaces sneaking in between revisions.
    assert text.startswith("It is a book that writes back: "), "book opener must survive"
    assert text.endswith("in every house on earth."), "every-house close must survive"
    assert "  " not in text, "no doubled spaces"
    assert text.isascii(), "plain ASCII keeps bytes equal to characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(ENTRY)
    # Round-trip guard: what the grader reads back must be exactly the line.
    with open(path, "rb") as f:
        assert f.read() == ENTRY, "round-trip mismatch"


if __name__ == "__main__":
    main()
