"""The Printer Finally Answers.

Writes the office printer's comeback to /output/entry.txt: one line,
1 to 240 characters, in the voice of the machine itself answering at
last everyone who jams it, thumps it and stares at its error codes.

Pure standard library only.
"""

import os

LINE = (
    "You pressed print fourteen times and blamed me for fourteen copies. "
    "I did exactly what you asked. That is the problem."
)


def main() -> None:
    # Gate, mirrored locally: the sealed scorer accepts UTF-8 text of
    # 1 to 240 characters, not only white space, on a single line.
    assert 1 <= len(LINE) <= 240, "entry must be 1 to 240 characters"
    assert "\n" not in LINE and LINE.strip(), "entry must be one non-blank line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    # Verify the round trip: what the grader reads back must be exactly
    # the line above, with no added newline or re-encoding.
    with open(path, "rb") as f:
        written = f.read()
    assert written == LINE.encode("utf-8"), "entry.txt does not match LINE"


if __name__ == "__main__":
    main()
