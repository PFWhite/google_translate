#! /usr/bin/python3

"""
Usage: q2.py [-v] <file> <seed> <epochs>
"""
from docopt import docopt

from theano_network import Network

import numpy as np

# args
_f = '<file>'
_c = '<config>'
_s = '<seed>'
_e = '<epochs>'

# config strings

def main():
    args = docopt(__doc__)

    network_config = {
        'input_dim': 2,
        'target_index': 2,
        'learning_rate': 1,
        'seed': args[_s],
        'layers': [2, 3]
    }


    train = True
    test = True

    verbose = args.get('-v')


    network = Network(network_config, args[_f])

    epoch_num = int(args[_e]) if args.get(_e) else 1

    if train:
        # output = network.train(data, epoch_num)
        pass

    if test:
        pass



if __name__ == '__main__':
    main()
