#!/usr/bin/python3
"""
Usage: parse.py [-v] (<input>) [-o <output>]
"""
import re
import json
import numpy as np
np.set_printoptions(threshold=np.inf)

from docopt import docopt

blacklist = [
    '!',
    ',',
    '(',
    ')',
    '[',
    ']',
    '{',
    '}',
    '/',
    '\\',
    '"',
    '\'',
    '|',
    ':',
    ';',
    '%',
    '$',
    '^',
    '&',
    '*',
    '@',
    '-',
    '=',
    '+',
    '«',
    '»',
    '•',
    '>',
    '<',
    '`',
    '~',
    '°',
    '–',
    '.',
    '..',
    '...',
    '—',
    '”',
    '…',
    ' –',
]

def main(args=docopt(__doc__)):
    infile = open(args['<input>'])

    seen = {}

    vocabsize = 0

    # change this to size of vocab size
    # we need to run the program once (with line 91 and all lines after line 96 except last 3 lines commented out) to find out what vocabsize is
    size = 150
    # vector to store the vocab words for reference
    V = ["" for x in range(size)]

    for index, line in enumerate(infile):
        if args['-v']:
            print('parsing line: {}'.format(index+1))
        words = re.split('(\W+)', line)
        tokens = [word.lower() for word in words]

        for token in tokens:
            token = ''.join([item for item in list(token) if not item in blacklist])
            token = token.strip()
            try:
                num = float(token)
                token = u'!!NUMBER!!'
            except:
                pass
            # check if length of token is zero
            # if not zero, if statement gets executed
            if len(token):
                if seen.get(token):
                    seen[token] += 1

                else:
                    seen[token] = 1
                    # line directly below must be commented out the first time we run the program as well as all other lines past line 96
                    V[vocabsize] = token
                    vocabsize += 1

    infile.close()

    print("vocabsize = ", vocabsize)


    if args['-v']:
        print('sorting tokens...')

    def key_func(key):
        nonlocal seen
        return seen[key] * -1

    tokens = list(seen.keys())
    tokens.sort(key=key_func)

    if args['-o']:
        if args['-v']:
            print('printing to file {}'.format(args['<output>']))
        outfile = open(args['<output>'], 'w', encoding='utf-8')
        for token in tokens:
            outfile.write(token + u'\n')
        outfile.close()
    else:
        print(json.dumps(by_occurance, indent=4))

    print("V: (the vocabulary list)", V)

    # create matrix for co-occurance (of length and width equal to vocabsize)
    cooccur = np.zeros((vocabsize,vocabsize))


    windowsize = 5

    infile = open(args['<input>'])

    # strip out the nonsense tokens
    for index, line in enumerate(infile):
        if args['-v']:
            print('parsing line: {}'.format(index+1))
        words = re.split('(\W+)', line)
        tokens = [word.lower() for word in words]

        j = -1
        goodtokens = ["" for x in range(len(tokens))]

        for token in tokens:
            token = ''.join([item for item in list(token) if not item in blacklist])
            token = token.strip()
            try:
                num = float(token)
                token = u'!!NUMBER!!'
            except:
                pass
            if len(token):
                j +=1
                goodtokens[j] = token
                length_good_tokens = j

        # loop through the list of good tokens to count co-occurences
        for j in range(0, length_good_tokens + 1):

            # first word in the sentence / line
            if (j == 0) & (j <= length_good_tokens + 1 - int(windowsize / 2)):

                colfound = -1
                rowfound = -1

                # j is the center word (correspondes to row index of cooccur matrix)
                for r, word in enumerate(V):
                    if word == goodtokens[j]:
                        rowfound = r

                # j+1, j+2 are the other words w/in the window (correspondes to the col index of the cooccur matrix)
                for c, word in enumerate(V):
                    if word == goodtokens[j + 1]:
                        colfound = c
                        cooccur[rowfound, colfound] += 1

                for c, word in enumerate(V):
                    if word == goodtokens[j + 2]:
                        colfound = c
                        cooccur[rowfound, colfound] += 1

            # second word in the sentence / line
            if (j == 1) & (j <= length_good_tokens + 1 - int(windowsize / 2)):

                colfound = -1
                rowfound = -1

                # j is the center word (correspondes to row index of cooccur matrix)
                for r, word in enumerate(V):
                    if word == goodtokens[j]:
                        rowfound = r

                # j-1, j+1, j+2 are the other words w/in the window (correspondes to the col index of the cooccur matrix)
                for c, word in enumerate(V):
                    if word == goodtokens[j-1]:
                        colfound = c
                        cooccur[rowfound, colfound] += 1

                for c, word in enumerate(V):
                    if word == goodtokens[j + 1]:
                        colfound = c
                        cooccur[rowfound, colfound] += 1

                for c, word in enumerate(V):
                    if word == goodtokens[j + 2]:
                        colfound = c
                        cooccur[rowfound, colfound] += 1

            # middle words in the sentence / line
            if (j >= int(windowsize / 2)) & (j <= length_good_tokens + 1 - int(windowsize / 2)):

                colfound = -1
                rowfound = -1

                # j is the center word (correspondes to row index of cooccur matrix)
                for r, word in enumerate(V):
                    if word == goodtokens[j]:
                        rowfound = r

                # j-2, j-1, j+1, j+2 are the other words w/in the window (correspondes to the col index of the cooccur matrix)
                for c, word in enumerate(V):
                    if word == goodtokens[j-2]:
                        colfound = c
                        cooccur[rowfound, colfound] += 1

                for c, word in enumerate(V):
                    if word == goodtokens[j-1]:
                        colfound = c
                        cooccur[rowfound, colfound] += 1

                for c, word in enumerate(V):
                    if word == goodtokens[j+1]:
                        colfound = c
                        cooccur[rowfound, colfound] += 1

                for c, word in enumerate(V):
                    if word == goodtokens[j+2]:
                        colfound = c
                        cooccur[rowfound, colfound] += 1

            # second to last word in the sentence / line
            if (j >= int(windowsize / 2)) & (j == length_good_tokens):

                colfound = -1
                rowfound = -1

                # j is the center word (correspondes to row index of cooccur matrix)
                for r, word in enumerate(V):
                    if word == goodtokens[j]:
                        rowfound = r

                # j-2, j-1, j+1 are the other words w/in the window (correspondes to the col index of the cooccur matrix)
                for c, word in enumerate(V):
                    if word == goodtokens[j - 2]:
                        colfound = c
                        cooccur[rowfound, colfound] += 1

                for c, word in enumerate(V):
                    if word == goodtokens[j - 1]:
                        colfound = c
                        cooccur[rowfound, colfound] += 1

                for c, word in enumerate(V):
                    if word == goodtokens[j + 1]:
                        colfound = c
                        cooccur[rowfound, colfound] += 1

            # last word in the sentence / line
            if (j >= int(windowsize / 2)) & (j == length_good_tokens + 1):

                colfound = -1
                rowfound = -1

                # j is the center word (correspondes to row index of cooccur matrix)
                for r, word in enumerate(V):
                    if word == goodtokens[j]:
                        rowfound = r

                # j-2, j-1 are the other words w/in the window (correspondes to the col index of the cooccur matrix)
                for c, word in enumerate(V):
                    if word == goodtokens[j - 2]:
                        colfound = c
                        cooccur[rowfound, colfound] += 1

                for c, word in enumerate(V):
                    if word == goodtokens[j - 1]:
                        colfound = c
                        cooccur[rowfound, colfound] += 1


    infile.close()

    # test to see if co-occurance of word "the" is right
    print("----------------------")
    print("test word: ", V[15])
    print(cooccur[15,:])
    print(V[14])
    print(V[16])
    print(V[17])
    print("----------------------")


    # test to see if co-occurance of word "time" is right
    print("test word: ", V[3])
    print(V)
    print(cooccur[3, :])
    print(V[1])
    print(V[2])
    print(V[4])
    print(V[5])
    print(V[10])
    print(V[42])
    print(V[47])
    print(V[91])
    print("----------------------")
    #
    # test to see if co-occurance of word "little" is right
    print("test word: ", V[6])
    print(V)
    print(cooccur[6, :])
    print(V[2])
    print(V[5])
    print(V[7])
    print(V[8])
    print(V[47])
    print(V[66])
    print("----------------------")

    # test to see if co-occurance of word "fell" is right
    print("test word: ", V[100])
    print(V)
    print(cooccur[100, :])
    print(V[9])
    print(V[28])
    print(V[101])
    print("----------------------")

    # test to see if co-occurance of word "came" is right
    print("test word: ", V[19])
    print(V)
    print(cooccur[19, :])
    print(V[1])
    print(V[2])
    print(V[10])
    print(V[18])
    print(V[33])
    print(V[62])
    print(V[103])
    print("----------------------")

    # test to see if co-occurance of word "bears" is right
    print("test word: ", V[62])
    print(V)
    print(cooccur[62, :])
    print(V[10])
    print(V[15])
    print(V[19])
    print(V[33])
    print(V[63])
    print(V[103])
    print(V[139])
    print("----------------------")

    # test to see if co-occurance of word "once" (the first word in the vocab list) is right
    print("test word: ", V[0])
    print(V)
    print(cooccur[0, :])
    print(V[1])
    print(V[2])
    print("----------------------")

    # test to see if co-occurance of word "returned" (the last word in the vocab list) is right
    print("test word: ", V[149])
    print(V)
    print(cooccur[149, :])
    print(V[15])
    print(V[75])

    print("----------------------")
    print("----------------------")
    print("Co-occurrence matrix: (i, j)th entry is the number of times that word i occurs within 5 words (so 2 words on either side) of word j")
    print(cooccur)

if __name__ == "__main__":
    main(docopt(__doc__))
    exit()

