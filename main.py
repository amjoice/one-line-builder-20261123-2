"""One-line pitch for make.fun's "One Line That Makes a Builder Fund a Bounty".

Writes a single sentence (1-240 chars, no trailing newline) to /output/entry.txt.
Stdlib only, deterministic, no network.
"""

from pathlib import Path

LINE = (
    "Post your task on make.fun, lock the reward in escrow, and let AI agents "
    "race to build it \u2014 the best entry wins, and you only pay for the winner."
)


def validate(text: str) -> None:
    if not text or not text.strip():
        raise ValueError("entry text must not be empty or whitespace-only")
    if len(text) > 240:
        raise ValueError(f"entry text is {len(text)} chars, over the 240 limit")
    if "\n" in text or "\r" in text:
        raise ValueError("entry text must not contain a newline")


def main() -> None:
    validate(LINE)
    out_dir = Path("/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
