#!/usr/bin/env python3
"""bobersay - A cowsay-inspired CLI featuring a Polish bóbr."""

import argparse
import random
import sys
import textwrap

__version__ = "1.0.0"

QUOTES = [
    "Ale fajny bober!",
    "Bóbr, kurwa! Jakie bydlę!",
    "O kurwa, gryzie!",
    "Patrzcie jaki wielki bóbr!",
    "Ja pierdolę, jakie bydlę!",
]

BEAVER = r'''       {t}
        {t}     _.-"""-._
         {t}   ( )     ( )
             /  {e}   {e}  \
            |    (_)    |
            |  .'|_|'.  |       _..---.._
           /     '-'     \   .-'#########'-.
          |   (_     _)   |.'###############'.
          |     '---'     |###################)
           \             / '-.#############.-'
           _'-.._____..-'_    ''--.....--''
          (_____)   (_____)'''


def format_bubble(lines: list[str], think: bool = False) -> list[str]:
    """Wrap text lines in a speech or thought bubble."""
    max_len = max(len(line) for line in lines)
    top = " " + "_" * (max_len + 2)
    bottom = " " + "-" * (max_len + 2)

    if think:
        body = [f"( {line.ljust(max_len)} )" for line in lines]
    elif len(lines) == 1:
        body = [f"< {lines[0].ljust(max_len)} >"]
    else:
        body = []
        for i, line in enumerate(lines):
            padded = line.ljust(max_len)
            if i == 0:
                body.append(f"/ {padded} \\")
            elif i == len(lines) - 1:
                body.append(f"\\ {padded} /")
            else:
                body.append(f"| {padded} |")

    return [top, *body, bottom]


def bobersay(
    text: str,
    width: int = 40,
    eye: str = "o",
    think: bool = False,
) -> str:
    """Render the bóbr with a speech or thought bubble."""
    lines: list[str] = []
    for paragraph in text.splitlines() or [""]:
        lines.extend(textwrap.wrap(paragraph, width=width) or [""])

    bubble = format_bubble(lines, think=think)
    eye_char = eye[0] if eye else "o"
    thought_char = "o" if think else "\\"

    art = BEAVER.replace("{e}", eye_char).replace("{t}", thought_char)
    return "\n".join([*bubble, art])


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="bobersay",
        description="A cowsay-inspired CLI featuring an authentic Polish bóbr.",
    )
    parser.add_argument(
        "message",
        nargs="*",
        help="Message for the bóbr to say (uses a random quote if omitted)",
    )
    parser.add_argument(
        "-W",
        "--width",
        type=int,
        default=40,
        help="Max speech bubble width before wrapping (default: 40)",
    )
    parser.add_argument(
        "-e",
        "--eyes",
        default="o",
        help="Custom eye character (default: o)",
    )
    parser.add_argument(
        "-d",
        "--dead",
        action="store_true",
        help="Dead mode (x eyes)",
    )
    parser.add_argument(
        "-g",
        "--greedy",
        action="store_true",
        help="Greedy mode ($ eyes)",
    )
    parser.add_argument(
        "-t",
        "--think",
        action="store_true",
        help="Render a thought bubble instead of speech",
    )
    parser.add_argument(
        "-v",
        "--version",
        action="version",
        version=f"%(prog)s {__version__}",
    )

    args = parser.parse_args()

    if args.dead:
        eye = "x"
    elif args.greedy:
        eye = "$"
    else:
        eye = args.eyes

    if args.message:
        text = " ".join(args.message)
    elif not sys.stdin.isatty():
        text = sys.stdin.read().strip()
    else:
        text = random.choice(QUOTES)

    print(bobersay(text, width=args.width, eye=eye, think=args.think))


if __name__ == "__main__":
    main()