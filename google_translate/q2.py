#! /usr/bin/python3

"""
Usage: q2.py [-v] <file> <seed> <epochs>
"""

import yaml

from docopt import docopt
import numpy as np

from network import Network

# args
_f = '<file>'
_c = '<config>'
_s = '<seed>'
_e = '<epochs>'

# config strings

def numpyify(data):
    return np.array(data)

def main():
    args = docopt(__doc__)

    network_config = {
        'input_dim': 2,
        'target_index': 2,
        'learning_rate': 1,
        'seed': args[_s],
        'layers': {
            'input': 2,
            'hidden': [10],
            'output': 1
        }
    }

    network = Network(network_config)

    with open(args[_f], 'r') as data_file:
        data = numpyify(yaml.load(data_file.read()))

    train = True
    test = False

    verbose = args.get('-v')

    epoch_num = int(args[_e]) if args.get(_e) else 1

    if train:
        output = network.train(data, epoch_num)
        output = np.array(output)

    if verbose:
        print(yaml.dump({
            'network':network.serialize(),
            'guesses': list(zip(data.tolist(), output.tolist()))
        }))


    if test:
        print(network.test(data))



if __name__ == '__main__':
    main()
