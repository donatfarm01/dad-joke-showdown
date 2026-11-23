"""Dad Joke Showdown entry: writes one original dad joke to /output/entry.txt.

The joke is a knock-knock gag told to a doorbell. The doorbell's whole job
is the sound "ding dong", so when it answers a knock-knock joke with its own
sound, the punchline is that it is simply doing its job. A father could tell
it across a dinner table, the pun lands on the first read, and the last
sentence is the punchline.
"""

import os

JOKE = (
    "I asked the doorbell for a knock-knock joke. "
    "It said, 'Ding dong.' "
    "I said, 'Who's there?' "
    "It said, 'That's literally my whole job.'"
)


def check(text):
    """Gate: one joke, 1 to 200 characters, UTF-8, no trailing newline."""
    if not text or text != text.strip():
        raise ValueError("entry must not be empty or padded with whitespace")
    if len(text) > 200:
        raise ValueError("entry is over 200 characters")
    if "\n" in text:
        raise ValueError("entry must be a single line")
    # The joke is one spoken line: a second sentence starter or an
    # exclamation buried mid-text would mean a second joke snuck in.
    body = text[:-1] if text.endswith(".") else text
    if "!" in body or "?" in body.replace("Who's there?", ""):
        raise ValueError("entry must stay one spoken line")
    text.encode("utf-8")
    return text


def main():
    entry = check(JOKE)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(entry)
    # Read-back: the file on disk must be exactly the text that passed
    # the gate, byte for byte.
    with open("/output/entry.txt", encoding="utf-8", newline="") as f:
        if f.read() != entry:
            raise ValueError("entry on disk differs from the checked text")


if __name__ == "__main__":
    main()
