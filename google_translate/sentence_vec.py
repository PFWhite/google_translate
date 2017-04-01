#!/usr/bin/python3
"""
Usage: sentence_vec.py [-v] (<input> <sorted> <size> <batch_size>) [-o <output>]
"""
import re

import numpy as np
np.seterr(divide='ignore',invalid='ignore')
from docopt import docopt

def main(args=docopt(__doc__)):
    infile = open(args['<input>'])

    seen = {}

    with open(args['<sorted>'], 'r') as word_list:
        text = word_list.read()
        text = text.split()

    if args['-o']:
        outfile = open(args['<output>'], 'w', encoding='utf-8')

    sentences = []
    for index, line in enumerate(infile):
        if args['-v']:
            print('parsing line: {}'.format(index+1))
        words = re.split('(\W+)', line)
        words = [word.lower() for word in words]

        # plus one for unknown tokens
        sentence = np.zeros([1, int(args['<size>']) + 1])

        for word in words:
            try:
                index = text.index(word)
                sentence[0,index] = 1
            except:
                sentence[0,-1] = 1

        sentences.append(sentence)

        if len(sentences) == int(args['<batch_size>']):
            s = np.sum(sentences, axis=0)
            del sentences
            sentences = []
            s = np.divide(s, s)
            def nonan(item):
                return 0 if item=='nan' else 1
            outfile.write(','.join([str(int(nonan(str(item)))) for item in s[0,:]]))
            outfile.write(u'\n')

    infile.close()
    outfile.close()


if __name__ == "__main__":
    main(docopt(__doc__))
    exit()

