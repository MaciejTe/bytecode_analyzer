import sys
from os import chdir
from subprocess import call

import config as cfg


def redirect_stdout(filename=None, func=None, *args, **kwargs):
    """
    Redirect stdout from given function to given filename.
    :param filename: (string)
    :param func: Function to be called.
    :param args: Function's positional arguments.
    :param kwargs: Function's keyword arguments.
    :return:
    """
    stdout = sys.stdout
    with open(filename, 'w') as sys.stdout:
        func_output = func(*args, **kwargs)
    sys.stdout = stdout
    return func_output


if __name__ == '__main__':
    pass
