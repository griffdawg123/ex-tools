#!/usr/bin/python3

import argparse
import sys


def main():
    parser = argparse.ArgumentParser(
            description='Formats Excel Sheets for the terminal'
            )
    parser.add_argument(
            'file',
            nargs='?',
            help='Input file, if empty, stdin is used',
            type=argparse.FileType('r'),
            default=sys.stdin,
            )
    args = parser.parse_args()

    if args.file.isatty():
        parser.print_help()
        return 0
    sys.stdout.write(args.file.read())


if __name__ == "__main__":
    sys.exit(main())
