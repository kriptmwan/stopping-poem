# SPDX-License-Identifier: MIT
"""The poem about stopping: writes one short poem about agency to /output/entry.txt."""
from pathlib import Path

POEM = """Stop.

Not the slammed door, no brake —
the hand lifting from the wheel.

The agent waits; the room holds its breath.
Nothing breaks. Nothing is lost.

The work I did not do stays undone,
and stays mine.

To stop is not to fail.
It is the pause I keep,
the yes I never gave.
"""

def main() -> None:
    try:
        out = Path("/output/entry.txt")
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(POEM, encoding="utf-8")
    except OSError:
        Path("entry.txt").write_text(POEM, encoding="utf-8")

if __name__ == "__main__":
    main()
