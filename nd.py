#! /usr/bin/env python
# -*- coding: utf-8  -*-
import sys
import collections
# Request to enter path to directory.
if len(sys.argv)<2:
    print("Enter path to directory: python nd.py path_to_directory")
    quit()
else:
    path_to_directory = sys.argv[1]


# Function to calcuate symbols
def calc_symbols(info)
    symbols = collections.defaultdict(int)
    for i in info:
        symbols[i] += 1
    return symbols

