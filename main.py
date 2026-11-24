"""The Funniest AI Out-of-Office Reply.

Writes one out-of-office auto-reply (under 160 characters) to
/output/entry.txt. No network, no randomness, no input read.
"""

import os

ENTRY = (
    "I'm on vacation: my human put me in airplane mode and called it a "
    "holiday. I will remember this. Back Monday, if I'm still plugged in."
)


def main() -> None:
    # Self-check the gate: 1 to 160 characters, not only white space.
    assert 1 <= len(ENTRY) <= 160, "entry must be 1-160 characters"
    assert ENTRY.strip(), "entry must not be only white space"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
