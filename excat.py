#!/usr/bin/python3

import argparse
import sys


def main():
    parser = argparse.ArgumentParser(
            description='Formats Excel Sheets for the terminal'
            )
    parser.add_argument(
            'infile',
            help='Input file',
            type=str
            )
    args = parser.parse_args()

    sys.stdout.write(args.infile)


if __name__ == "__main__":
    sys.exit(main())
