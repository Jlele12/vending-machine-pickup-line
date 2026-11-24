#!/usr/bin/env python3
"""One Line, One Minute: The Vending Machine Pickup Line Contest entry.

Writes the contest's one pickup line (<=200 chars) to /output/entry.txt.
The line is spoken by the vending machine itself: its slot, its coil,
its exact change, and the snack it has been stuck on all day.
"""

LINE = (
    "Are you exact change? Because I've been short all day - and you're "
    "the first thing in this hallway I'd never get stuck on."
)


def main() -> None:
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
