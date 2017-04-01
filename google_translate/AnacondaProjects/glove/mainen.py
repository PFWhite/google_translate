import re

from word_matrix import WordMatrix as WM

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

def main():
    infile = open('en/infile', 'r')
    with open('en/sorted', 'r') as sfile:
        sort_tokens = sfile.read().split()

    wm = WM(window_size=9, vocab_size=10000)
    for index, line in enumerate(infile):
        # read in a word
        sentence = line.split()
        # turn it to token
        tokens = [tokenize(word, blacklist, sort_tokens) for word in sentence if tokenize(word, blacklist, sort_tokens)]
        # if never seen put in cooccurance matrix
        wm.add(tokens)
        print(index)

    infile.close()

    with open('en/matrix', 'w') as mfile:
        mfile.write(wm.matrix_serialize())

    with open('en/matrix_key', 'w') as mkfile:
        mkfile.write(wm.matrix_keys())


def tokenize(word, blacklist, sort_tokens):
    token = ''.join([item for item in list(word) if not item in blacklist])
    token = token.strip()
    try:
        num = float(token)
        token = u'!!NUMBER!!'
    except:
        pass
    if len(token):
        return token
    else:
        return None

if __name__ == '__main__':
    main()
