#! /usr/bin/env python
# -*- coding: utf-8  -*-
import sys
import os
import collections
import re

if len(sys.argv) < 3:
    '''Request to enter path to directory and statistics file name'''
    print("Enter path to directory: python nd.py path_to_directory"
          "statistics_file_name.txt")
    quit()
else:
    path_to_directory = sys.argv[1]


def calc_symbols(info):
    '''Function to count symbols'''
    symbols = collections.defaultdict(int)
    for i in info:
        symbols[i] += 1
    return symbols


def calc_words(info):
    '''Function to count words'''
    words = collections.Counter(map(str.lower, re.split('\W+', info)))
    return words


file_list = os.listdir(path_to_directory)
'''Loop for reading files from specified directory, calcuating their'''
'''statistics and writing them to specified statistics file'''
for i in range(0, len(file_list)):
    loop = file_list[i]
    file_dir = str(path_to_directory) + str(loop)
    file_text = open(file_dir, 'r')
    material = file_text.read()
    file_text.close()
    symbol_statistics = calc_symbols(material)
    words_statistics = calc_words(material)
    stat_file_dir = str(path_to_directory) + str(sys.argv[2])
    statistics_file = open(stat_file_dir, 'a')

