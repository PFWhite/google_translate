#! /usr/bin/python3

import fileinput
import json
import datetime
import pdb
import re

import config as config

def normalize_token(string):
    token = re.sub('[^a-zA-Z]+', '', string)
    return token

def process_line(line, accumulator):
    """
    Does the main work of tokenization
    """
    tokens = line.split()
    for token in tokens:
        token = normalize_token(token)
        if accumulator.get(token):
            accumulator[token] += 1
        else:
            accumulator[token] = 1

def get_outfile_path(path):
    """
    Returns the path of a particular tokenization run
    """
    now = str(datetime.datetime.now()).replace(' ', '_') + '.json'
    return '/'.join([path, 'space_tokens', now])

def tokenize():
    """
    This is a tokenizing function that naively splits the
    instream based on spaces. It then stores the information
    in memory and will write to disk when done.
    """
    seen_tokens = {}
    for line in fileinput.input():
        process_line(line, seen_tokens)

    outfile = open(get_outfile_path(config.token_file_path), 'w+')
    outfile.write(json.dumps(seen_tokens, indent=4, sort_keys=True))
    outfile.close()


if __name__ == "__main__":
    tokenize()
