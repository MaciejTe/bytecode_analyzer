import platform
import time
import sys
import binascii
import marshal
import dis
import struct
from os import system

import config as cfg
import commons


class BytecodeOper(object):
    """
    Class containing methods operating on .pyc files.
    """
    def __init__(self):
        pass

    def create_pyc_files(self, venv, path):
        """
        Create .pyc files depending on given virtual environment.
        :param venv:
        :param path:
        :return:
        """
        system("{} -m compileall {}".format(venv, path))

    def analyze_pyc_file(self, path):
        """Read and display a content of the Python`s bytecode
        in a .pyc file.
        """

        file = open(path, 'rb')

        magic = file.read(4)
        timestamp = file.read(4)
        size = None

        if sys.version_info.major == 3 and sys.version_info.minor >= 3:
            size = file.read(4)
            size = struct.unpack('I', size)[0]

        code = marshal.load(file)

        magic = binascii.hexlify(magic).decode('utf-8')
        timestamp = time.asctime(
                    time.localtime(struct.unpack('I', b'D\xa5\xc2X')[0]))

        if sys.version_info.major == 3 and sys.version_info.minor >= 3:
            commons.redirect_stdout(cfg.PYC_OUTPUT_FILE_3,
                                    self.generate_pyc_output,
                                    code_obj=code, magic=magic,
                                    timestamp=timestamp, size=size)
        else:
            commons.redirect_stdout(cfg.PYC_OUTPUT_FILE_2,
                                    self.generate_pyc_output,
                                    code_obj=code, magic=magic,
                                    timestamp=timestamp, size=size)
        file.close()

    @staticmethod
    def generate_pyc_output(code_obj=None, magic=None, timestamp=None,
                            size=None):
        dis.disassemble(code_obj)
        print('-' * 80)
        print('Python version: {}\nMagic code: {}\nTimestamp: {}\nSize: {}'
              .format(platform.python_version(), magic, timestamp, size))


if __name__ == '__main__':
    byte_obj = BytecodeOper()
    byte_obj.analyze_pyc_file(sys.argv[1])