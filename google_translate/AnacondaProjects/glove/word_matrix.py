import math
from copy import copy

class WordMatrix(object):

    def __init__(self, window_size, vocab_size):
        self.window_size = window_size if not window_size % 2 else window_size - 1
        matrix_row = [0.0 for item in range(0, vocab_size)]
        self.matrix = [copy(matrix_row) for item in range(0, vocab_size)]
        self.matrix_keys = []

    def add(self, tokens):
        for token in tokens:
            if not token in self.matrix_keys:
                self.matrix_keys.append(token)

        steps = self.window_size/2
        for index, token in enumerate(tokens):
            # read steps to left
            lstep = 1
            mindex = self.matrix_keys.index(token)
            while index - lstep > -1:
                try:
                    lindex = self.matrix_keys.index(tokens[index - lstep])
                    self.matrix[mindex][lindex] += (1.0/lstep)
                    self.matrix[lindex][mindex] += (1.0/lstep)
                except:
                    pass
                lstep += 1
            # read steps to right
            rstep = 1
            while index + rstep < len(tokens):
                try:
                    rindex = self.matrix_keys.index(tokens[index - rstep])
                    self.matrix[mindex][rindex] += (1.0/rstep)
                    self.matrix[rindex][mindex] += (1.0/rstep)
                except:
                    pass
                rstep += 1
            # add 1/steps to matrix value

    def matrix_serialize(self):
        text = ''
        for row in self.matrix:
            rowtext = ''
            for col in row:
                ' '.join([rowtext, col])
            '\n'.join([text, rowtext])
        return text

    def matrix_keys(self):
        return '\n'.join(self.matrix_keys)



