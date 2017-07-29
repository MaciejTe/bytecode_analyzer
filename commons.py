import sys
from os import chdir
from subprocess import call

import config


def redirect_stdout(filename, func, *args, **kwargs):
    stdout = sys.stdout
    with open(filename, 'w') as sys.stdout:
        func(*args, **kwargs)
    sys.stdout = stdout
