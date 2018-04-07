#!/usr/bin/env python3
import argparse
import os
import re

# Argument processing
version = "0.0.1"
parser = argparse.ArgumentParser(
    description="file search with regular expressions!",
    epilog="(C) 2018 Fabio 'Monte' Sant'Anna")
parser.add_argument("PATTERN", help="Regular Expression for file name")
parser.add_argument("PATH", help="Start PATH for search")
parser.add_argument(
    "-r", "--recursive", help="search recursively", action="store_true")
parser.add_argument(
    "--version", action="version", version="%(prog)s " + version)
args = parser.parse_args()

walker = os.walk(os.path.abspath(args.PATH))
if not args.recursive:
    walker = (x for x in [next(walker)])

c = 0
for directory in walker:
    path, dirs, files = directory
    found = list(map(
        lambda x: path + "/" + x,
        filter(lambda x: re.search(args.PATTERN, x, 0) is not None,
        files)))
    c = c + len(found)
    for name in found:
        print(name)

print ("{} files found".format(c))

