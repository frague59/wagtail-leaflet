#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
# COMMENT HERE #

:creationdate: 05/05/17 13:19
:moduleauthor: François GUÉRIN <fguerin@ville-tourcoing.fr>
:modulename: wagtailleaflet.__init__.py

"""
import os
import sys
import argparse
import logging

__author__ = 'fguerin'
logger = logging.getLogger('wagtailleaflet.__init__.py')


def main(arguments):
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('infile', help="Input file", type=argparse.FileType('r'))
    parser.add_argument('-o', '--outfile', help="Output file",
                        default=sys.stdout, type=argparse.FileType('w'))

    args = parser.parse_args(arguments)

    print args


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
