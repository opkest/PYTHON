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
total_material = ''
'''Loop for reading files from specified directory, calcuating their'''
'''statistics and writing them to specified statistics file'''
for i, filename in enumerate(file_list):
    file_dir = str(path_to_directory) + '/' + str(filename)
    file_text = open(file_dir, 'r')
    material = file_text.read()
    total_material += material
    file_text.close()
    symbol_statistics = calc_symbols(material)
    words_statistics = calc_words(material)
    stat_file_dir = str(path_to_directory) + '/' + str(sys.argv[2])
    statistics_file = open(stat_file_dir, 'a')
    statistics_file.write('Simboliu statistika failo: ' + str(filename) + '\n')
    for key, value in symbol_statistics.items():
        statistics_file.write(str(key) + ' : ' + str(value) + '; ' + '\n')
    statistics_file.write('Zodziu statistika failo: ' + str(filename) + '\n')
    for key, value in words_statistics.items():
        statistics_file.write(str(key) + ' : ' + str(value) + '; ' + '\n')
    statistics_file.close()
'''Code to calcuate overall statistics of files in specified directory and'''
'''write them to specified statistics file'''
total_symbol_statistics = calc_symbols(total_material)
total_words_statistics = calc_words(total_material)
statistics_file = open(stat_file_dir, 'a')
statistics_file.write('Bendra visu failu simboliu statistika: ' + '\n')
for key, value in total_symbol_statistics.items():
    statistics_file.write(str(key) + " : " + str(value) + "; " + '\n')
statistics_file.write('Bendra visu failu zodziu statistika: ' + '\n')
for key, value in total_words_statistics.items():
    statistics_file.write(str(key) + " : " + str(value) + "; " + '\n')
statistics_file.close()
