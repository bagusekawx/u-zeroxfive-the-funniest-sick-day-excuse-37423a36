"""Funniest Sick-Day Excuse entry: one line that gets you out of work.

The excuse starts as an ordinary sick note, then escalates past the
person to the hardware: the sneeze is not the problem, the frozen
webcam frame is, and IT has already ruled on it. The last word lands
the twist.
"""

import os

ENTRY = "Sorry, calling in sick - I sneezed so hard during the morning standup that my webcam froze on it, and IT has quarantined my laptop as a biohazard."


def entry_path() -> str:
    """Resolve the output file, creating the output directory if needed."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    return os.path.join(out_dir, "entry.txt")


def main() -> None:
    with open(entry_path(), "w", encoding="utf-8") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()
