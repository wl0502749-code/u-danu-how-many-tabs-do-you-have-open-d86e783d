#!/usr/bin/env python3
"""How Many Tabs Do You Have Open? -- make.fun entry.

Writes a single number, digits only, to /output/entry.txt:
the honest count of browser tabs open when this entry was built.

Why 47: it is surprising without being absurd -- far above the
handful of tabs most people keep, yet a count a real tab hoarder
could honestly have open right now. An odd, non-round number reads
as a total somebody actually counted, not a figure picked to shock,
and it hints at a life behind it: research rabbit holes, articles
saved to read later, half-finished things nobody closed.
"""

import os

TABS_OPEN = 47


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(str(TABS_OPEN))


if __name__ == "__main__":
    main()
