#!/usr/bin/python3
"""
Usage: parse.py [-v] (<input>) [-o <output>]
"""
import re
import json

from docopt import docopt

blacklist = [
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
            if len(token):
                if seen.get(token):
                    seen[token] += 1
                else:
                    seen[token] = 1

    infile.close()

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

if __name__ == "__main__":
    main(docopt(__doc__))
    exit()

