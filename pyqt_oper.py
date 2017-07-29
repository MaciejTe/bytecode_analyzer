import os
from sys import version_info

import config


class PyQtOper(object):
    """
    Class containing methods working with PyQt objects.
    """
    def __init__(self, bytecode2=None, bytecode3=None):
        self.bytecode_python2 = bytecode2
        self.bytecode_python3 = bytecode3

    def write_to_plain_text_edit(self, filename, python_ver=None):
        path = os.path.join(config.HOME_PATH, filename)
        with open(path, 'r') as dis_output:
            lines_list = dis_output.readlines()
            for line in lines_list:
                if python_ver == '3':
                    self.bytecode_python3.insertPlainText(line)
                else:
                    self.bytecode_python2.insertPlainText(line)
