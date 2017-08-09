from sys import argv
from os import path, listdir, path
from PyQt4 import QtGui
from subprocess import Popen, PIPE, STDOUT
from time import sleep

import config as cfg
import commons
import main_window_tabs
import pyqt_oper
from bytecode_oper import BytecodeOper
from parser import Parser
from plotter import Plotter


class MainWindow(QtGui.QTabWidget, main_window_tabs.Ui_TabWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowIcon(QtGui.QIcon('images/python.png'))
        self.setupUi(self)
        pyqt_obj = pyqt_oper.PyQtOper()
        pyqt_obj.load_image(self.front_image, 'images/python.png')
        self.bar_chart_rb.setChecked(True)  # TEMPORARILY
        self.benchmark_profile_time_rb.setChecked(True)  # TEMPORARILY
        self.load_file_button.clicked.connect(self.select_file)
        self.analyze_button.clicked.connect(self.app_workflow)

    def app_workflow(self):
        """
        Method setting the application workflow.
        """
        self.entry_sequence()
        self.choose_an_interpreter()
        self.choose_sample_benchmark()
        self.choose_benchmark_profile()
        count = self.set_iterations_count()
        self.run_test()
        self.create_chart()
        self.exit_sequence()

    def choose_an_interpreter(self):
        """
        Choose wanted Python interpreter.
        """
        if self.python_2_cb.isChecked():
            cfg.INTERPRETERS.update({'venv_analyzer2/bin/python':
                                     'python_2_examples/'})
            if 'Python 2.7.12' not in cfg.PLOT_OBJECTS:
                cfg.PLOT_OBJECTS.append('Python 2.7.12')
            print('Python2.7 added to dictionary')
        if self.python_3_cb.isChecked():
            cfg.INTERPRETERS.update({'venv_analyzer3/bin/python':
                                     'python_3_examples/'})
            if 'Python 3.5.2' not in cfg.PLOT_OBJECTS:
                cfg.PLOT_OBJECTS.append('Python 3.5.2')
            print('Python3.5 added to dictionary')

    def choose_sample_benchmark(self):
        """
        Choose wanted sample benchmark.
        """
        if self.benchmark_exceptions_rb.isChecked():
            cfg.TEST_FILE = 'handling_exceptions.py'
        elif self.benchmark_list_compr_rb.isChecked():
            cfg.TEST_FILE = 'comprehension_list.py'
        elif self.benchmark_generators_rb.isChecked():
            cfg.TEST_FILE = 'next.py'

    def choose_benchmark_profile(self):
        """
        Choose wanted benchmark / performance profile.
        """
        if self.benchmark_profile_time_rb.isChecked():
            cfg.BENCHMARK_PROFILES.update({'time': 'time'})

    def set_iterations_count(self):
        return self.iterations_value.toPlainText()

    def run_test(self, iterations=None):
        """
        Test running algorithm.
        :param iterations: Not implemented yet.
        """
        if iterations == '':
            iterations = str(100)
        for venv, example_path in cfg.INTERPRETERS.items():
            if cfg.BENCHMARK_PROFILES.values() == ['time']:
                process = Popen(['time', '-v', '{}'.format(venv),
                                '{}{}'.format(example_path, cfg.TEST_FILE)],
                                stdin=PIPE, stdout=PIPE, stderr=STDOUT)
                benchmark_output = process.stdout.read()
                # PARSE TIME OUTPUT
                parse_obj = Parser(benchmark_output)
                parse_output = commons.redirect_stdout(
                                         filename=cfg.BENCHMARK_PROFILE_OUTPUT,
                                         func=parse_obj.parse_time_output)
                self.save_interpreter_performace(python_venv=venv,
                                                 parse_output=parse_output)
            pyqt_obj = pyqt_oper.PyQtOper(
                benchmark_profile_output_2=self.benchmark_profile_output_2,
                benchmark_profile_output_3=self.benchmark_profile_output_3)
            if '3' in venv:
                pyqt_obj.write_to_plain_text(benchmark_output, python_ver='3')
            else:
                pyqt_obj.write_to_plain_text(benchmark_output, python_ver='2')
            # CREATE PYC FILES
            bytecode_obj = BytecodeOper()
            bytecode_obj.create_pyc_files(venv, example_path)
            # GENERATE OUTPUT FROM PYC FILES
            self.generate_pyc_output_to_pyqt(bytecode_obj, example_path,
                                             venv)

    def generate_pyc_output_to_pyqt(self, bytecode_obj, example_path, venv):
        """

        :param bytecode_obj:
        :param example_path:
        :param venv:
        :return:
        """
        if '3' in example_path:
            for filename in listdir(cfg.PYC_FILES_PYTHON_3_RELATIVE):
                if cfg.TEST_FILE[:-2] in filename and filename.endswith(
                        '.pyc'):
                    pyc = path.join(cfg.EXAMPLES_PATH_3, '__pycache__',
                                    filename)
                    Popen([venv, 'bytecode_oper.py', pyc],
                          stdin=PIPE, stdout=PIPE, stderr=STDOUT)
                    pyqt_obj = pyqt_oper.PyQtOper(self.bytecode_python2,
                                                  self.bytecode_python3)
                    sleep(0.1)
                    pyqt_obj.write_to_plain_text_edit_from_file(
                                                         cfg.PYC_OUTPUT_FILE_3,
                                                         python_ver='3')
        else:
            for filename in listdir(cfg.PYC_FILES_PYTHON_2_RELATIVE):
                if cfg.TEST_FILE in filename and filename.endswith('.pyc'):
                    pyc = path.join(cfg.EXAMPLES_PATH_2, filename)
                    bytecode_obj.analyze_pyc_file(pyc)
                    pyqt_obj = pyqt_oper.PyQtOper(self.bytecode_python2,
                                                  self.bytecode_python3)
                    pyqt_obj.write_to_plain_text_edit_from_file(
                                                         cfg.PYC_OUTPUT_FILE_2,
                                                         python_ver='2')

    @staticmethod
    def save_interpreter_performace(python_venv=None, parse_output=None):
        cfg.PERFORMANCE_DICT.update({python_venv:
                                     parse_output['User time (seconds)']})

    def select_file(self):
        """
        Select .py file to analyze. Warning!
        1. Custom files to analyze have to be located in  python_2_examples and
        python_3_examples directories
        2. If you want to analyze Python 2 and 3 files, their filenames in
        directories python_2_examples and python_3_examples have to be the same
        """
        self.clear_sample_benchmarks_rbs()
        filename_list = map(str, QtGui.QFileDialog.getOpenFileNames(self,
                                                          'Choose Python file',
                                                          cfg.EXAMPLES_PATH_2,
              filter='Python files (*.py *.pyw *.pyc *.pyo);;All files (*.*)'))
        cfg.TEST_FILE = path.basename(filename_list[0])

    def create_chart(self):
        plotter_obj = Plotter()
        if self.bar_chart_rb.isChecked():
            plotter_obj.generate_bar_chart()
        pyqt_obj = pyqt_oper.PyQtOper()
        pyqt_obj.load_image(self.chart_label, cfg.IMAGES_PATH +
                            '/performance.png')

    def entry_sequence(self):
        """
        Sequence to execute before running test.
        """
        self.bytecode_python3.clear()
        self.bytecode_python2.clear()
        self.benchmark_profile_output_2.clear()
        self.benchmark_profile_output_3.clear()

    @staticmethod
    def exit_sequence():
        """
            Sequence to execute after test was run.
        """
        cfg.INTERPRETERS.clear()
        cfg.BENCHMARK_PROFILES.clear()
        cfg.PERFORMANCE_DICT.clear()
        del cfg.PLOT_OBJECTS[:]

    def clear_sample_benchmarks_rbs(self):
        self.benchmark_exceptions_rb.setChecked(False)
        self.benchmark_list_compr_rb.setChecked(False)
        self.benchmark_generators_rb.setChecked(False)


def main():
    app = QtGui.QApplication(argv)
    form = MainWindow()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()
