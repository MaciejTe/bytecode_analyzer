import sys
from os import path, walk, listdir, chdir
from PyQt4 import QtGui
from subprocess import Popen, PIPE, STDOUT

import config as cfg
import main_window_tabs
import pyqt_oper
from bytecode_oper import BytecodeOper
from parser import Parser


class MainWindow(QtGui.QTabWidget, main_window_tabs.Ui_TabWidget):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle('Bytecode analyzer')
        self.setWindowIcon(QtGui.QIcon('images/python.png'))  # does not work
        self.setupUi(self)
        # self.resize(1024, 768)
        # self.setAcceptDrops(True)
        self.analyze_button.clicked.connect(self.app_workflow)

    def app_workflow(self):
        self.choose_an_interpreter()
        self.choose_benchmark()
        self.choose_benchmark_profile()
        count = self.set_iterations_count()
        self.run_test(interpreter=cfg.INTERPRETERS, benchmark=cfg.BENCHMARK_PROFILES,
                      example=cfg.TEST_FILE)
        # self.run_test(interpreter=cfg.INTERPRETERS, benchmark=cfg.BENCHMARK_PROFILES,
        #               command='"[i for i in range(10000)]"', iterations=count)



        self.exit_sequence()

    def choose_an_interpreter(self):
            if self.python_3_cb.isChecked():
                cfg.INTERPRETERS.update({'venv_analyzer3/bin/python': 'python_3_examples/'})
                print('Python3.5 added to dictionary')
            if self.python_2_cb.isChecked():
                cfg.INTERPRETERS.update({'venv_analyzer2/bin/python': 'python_2_examples/'})
                print('Python2.7 added to dictionary')

    def choose_benchmark(self):
        if self.benchmark_exceptions_rb.isChecked():
            cfg.TEST_FILE = 'handling_exceptions.py'
        elif self.benchmark_list_compr_rb.isChecked():
            cfg.TEST_FILE = 'comprehension_list.py'
        elif self.benchmark_generators_rb.isChecked():
            cfg.TEST_FILE = 'next.py'
        else:
            print 'Something is wrong with benchmarks!'

    def choose_benchmark_profile(self):
        if self.benchmark_profile_time_rb.isChecked():
            cfg.BENCHMARK_PROFILES.update({'time': 'time'})
        elif self.benchmark_profile_timeit_rb.isChecked():
            cfg.BENCHMARK_PROFILES.update({'timeit': 'timeit'})

    def set_iterations_count(self):
        return self.iterations_value.toPlainText()

    def run_test(self, interpreter=None, benchmark=None, example=None,
                 command=None, iterations=None):
        if iterations == '':
            iterations = str(100)
        for venv, example_path in interpreter.items():
            print venv, '------------'
            if benchmark.values() == ['time']:
                process = Popen(['time', '-v', '{}'.format(venv),
                                '{}{}'.format(example_path, example)],
                                stdin=PIPE, stdout=PIPE, stderr=STDOUT)
                output = process.stdout.read()
                # PARSE TIME OUTPUT
                parse_obj = Parser(output)
                # print parse_obj.parse_time_output(), '***'
                # CREATE PYC FILES
                bytecode_obj = BytecodeOper()
                bytecode_obj.create_pyc_files(venv, example_path)
                # GENERATE OUTPUT FROM PYC FILES
                if '3' in example_path:
                    for filename in listdir(cfg.PYC_FILES_PYTHON_3_RELATIVE):
                        if cfg.TEST_FILE[:-2] in filename and filename.endswith('.pyc'):
                            pyc = path.join(cfg.EXAMPLES_PATH_3, '__pycache__',
                                            filename)
                            Popen([venv, 'bytecode_oper.py', pyc],
                                  stdin=PIPE, stdout=PIPE, stderr=STDOUT)
                            pyqt_obj = pyqt_oper.PyQtOper(self.bytecode_python2,
                                                          self.bytecode_python3)
                            pyqt_obj.write_to_plain_text_edit(cfg.PYC_OUTPUT_FILE_3,
                                                              python_ver='3')
                else:
                    for filename in listdir(cfg.PYC_FILES_PYTHON_2_RELATIVE):
                        if cfg.TEST_FILE in filename and filename.endswith('.pyc'):
                            pyc = path.join(cfg.EXAMPLES_PATH_2, filename)
                            bytecode_obj.analyze_pyc_file(pyc)
                            pyqt_obj = pyqt_oper.PyQtOper(self.bytecode_python2,
                                                          self.bytecode_python3)
                            pyqt_obj.write_to_plain_text_edit(cfg.PYC_OUTPUT_FILE_2,
                                                              python_ver='2')

            elif benchmark.values() == ['timeit']:
                process = Popen(['{}'.format(version), '-m', 'timeit', '-v',
                                 '-n', '{}'.format(iterations), '{}'.format(command)],
                                stdin=PIPE, stdout=PIPE, stderr=STDOUT)
                output = process.stdout.read()
                parse_obj = Parser(output)
                parse_obj.parse_timeit_output()

    @staticmethod
    def exit_sequence():
        cfg.INTERPRETERS.clear()
        cfg.BENCHMARK_PROFILES.clear()


def main():
    app = QtGui.QApplication(sys.argv)  # new instance of QApplication
    form = MainWindow()
    form.show()  # show the form
    app.exec_()  # execute the app

if __name__ == '__main__':
    main()
