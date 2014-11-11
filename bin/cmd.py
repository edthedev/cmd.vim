#!/usr/bin/env python2
"""Creates and manages a folder full of reminder files.

Usage: 
    cmd.py [--selection=<selection>]

Options:
    -h --help               Show this help.
    -s --selection=<selection>         Selected text to apply formatting to.
    --version               Show version.

Supported file types:
    rst - ReStructuredText

Supported tags:
    h1 - Header 1
    h2 - Header 2
    h3 - Header 3
    img - Image
    blockquote - Block Quote
"""
#import os
#import sys

# DocOpt is awesome. https://github.com/docopt/docopt
from docopt import docopt

def parse_line(line):
    """Parse out some dictionary keys from the current line.
    """

    data = {}
    parts = line.split(' ')
    leftovers = []
    for part in parts:
        if '=>' in part:
            key, value = tuple(part.split('=>', 1))
            data[key] = value
        else:
            leftovers.append(part)

    return ' '.join(leftovers), data

if __name__ == '__main__':

    args = docopt(__doc__, version='1.0')

    selection = ''
    if '--selection' in args:
        selection = args['--selection']

    print "Hello World" + selection
