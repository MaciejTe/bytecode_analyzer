from subprocess import Popen, PIPE, STDOUT


class BytecodeOper(object):
    def __init__(self):
        pass

    def create_pyc_file(path):

        # res = os.popen("python -m compileall {}".format(path))