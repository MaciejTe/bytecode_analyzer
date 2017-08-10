import os
from PyQt5.QtGui import QPixmap
from sys import version_info

import config


class PyQtOper(object):
    """
    Class containing methods working with PyQt objects.
    """
    def __init__(self, bytecode2=None, bytecode3=None,
                 benchmark_profile_output_2=None,
                 benchmark_profile_output_3=None, chart_label=None):
        self.bytecode_python2 = bytecode2
        self.bytecode_python3 = bytecode3
        self.benchmark_profile_output_2 = benchmark_profile_output_2
        self.benchmark_profile_output_3 = benchmark_profile_output_3
        self.chart_label = chart_label

    def write_to_plain_text_edit_from_file(self, filename, python_ver=None):
        path = os.path.join(config.HOME_PATH, filename)
        with open(path, 'r') as dis_output:
            lines_list = dis_output.readlines()
            for line in lines_list:
                if python_ver == '3':
                    self.bytecode_python3.insertPlainText(line)
                else:
                    self.bytecode_python2.insertPlainText(line)

    def write_to_plain_text(self, text, python_ver=None):
        """

        :return:
        """
        if python_ver == '3':
            self.benchmark_profile_output_3.insertPlainText(text)
        else:
            self.benchmark_profile_output_2.insertPlainText(text)

    def load_image(self, img_label, path):
        pixmap = QPixmap(path)
        scaled_img_label = pixmap.scaled(img_label.size())
        img_label.setPixmap(scaled_img_label)
