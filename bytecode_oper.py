import platform
import time
import sys
import binascii
import marshal
import dis
import struct
from os import system, path
from bytecode_graph import bytecode_graph, render

import config as cfg
import commons


class BytecodeOper(object):
    """
    Class containing methods operating on .pyc files.
    """
    def __init__(self):
        pass

    @staticmethod
    def create_pyc_files(venv, path):
        """
        Create .pyc files depending on given virtual environment.
        :param venv:
        :param path:
        :return:
        """
        system("{} -m compileall {}".format(venv, path))

    def analyze_pyc_file(self, path):
        """Read and redirect a content of the Python`s bytecode
        in a .pyc filename to output file.
        """
        filename = open(path, 'rb')

        magic = filename.read(4)
        timestamp = filename.read(4)
        size = None

        if sys.version_info.major == 3 and sys.version_info.minor >= 3:
            size = filename.read(4)
            size = struct.unpack('I', size)[0]

        code = marshal.load(filename)
        self.serialize(code)

        magic = binascii.hexlify(magic).decode('utf-8')
        timestamp = time.asctime(
                    time.localtime(struct.unpack('I', b'D\xa5\xc2X')[0]))
        print('Python version: ', sys.version_info.major, sys.version_info.minor)
        if sys.version_info.major == 3 and sys.version_info.minor >= 3:
            commons.redirect_stdout(filename=cfg.PYC_OUTPUT_FILE_3,
                                    func=self.generate_pyc_output,
                                    code_obj=code, magic=magic,
                                    timestamp=timestamp, size=size)
            self.bytecode_graph(code, '3')
        else:
            commons.redirect_stdout(filename=cfg.PYC_OUTPUT_FILE_2,
                                    func=self.generate_pyc_output,
                                    code_obj=code, magic=magic,
                                    timestamp=timestamp, size=size)
            self.bytecode_graph(code, '2')
        filename.close()

    @staticmethod
    def generate_pyc_output(code_obj=None, magic=None, timestamp=None,
                            size=None):
        dis.disassemble(code_obj)
        print('-' * 80)
        print('Python version: {}\nMagic code: {}\nTimestamp: {}\nSize: {}'
              .format(platform.python_version(), magic, timestamp, size))

    @staticmethod
    def serialize(obj):
        print(marshal.dump(obj, open(cfg.SERIALIZED_OBJECT, 'wb')))

    @staticmethod
    def deserialize(serialized_file):
        return marshal.load(open(serialized_file, 'rb'))

    def bytecode_graph(self, code_obj, python_ver):
        print('graph')
        bcg = bytecode_graph.BytecodeGraph(code_obj)
        graph = render.Render(bcg, code_obj).dot()
        print('Wynik graph_write: ', graph.write_png('CFG_%s.png' % python_ver))


if __name__ == '__main__':
    byte_obj = BytecodeOper()
    byte_obj.analyze_pyc_file(sys.argv[1])
    # byte_obj.bytecode_graph(BytecodeOper.create_pyc_files.__code__, '2')
