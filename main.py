from PyQt4 import QtGui
from subprocess import Popen, PIPE, STDOUT
import sys

from parser import Parser
import config as cfg
import main_window, main_window_tabs

class MainWindow(QtGui.QTabWidget, main_window_tabs.Ui_TabWidget):
#class MainWindow(QtGui.QMainWindow, main_window.Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setWindowTitle('Bytecode analyzer')
        self.setWindowIcon(QtGui.QIcon('images/python.jpeg'))  # does not work
        self.setupUi(self)
        # self.resize(1024, 768)
        # self.setAcceptDrops(True)
        self.analyze_button.clicked.connect(self.app_workflow)

    def app_workflow(self):
        self.choose_an_interpreter()
        self.choose_benchmark_profile()
        count = self.set_iterations_count()
        # self.run_test(interpreter=cfg.INTERPRETERS, benchmark=cfg.BENCHMARK_PROFILES,
        #               example='python2_examples/next.py')
        self.run_test(interpreter=cfg.INTERPRETERS, benchmark=cfg.BENCHMARK_PROFILES,
                      command='"[i for i in range(10000)]"', iterations=count)
        self.exit_sequence()

    def choose_an_interpreter(self):
            if self.python_3_cb.isChecked():
                cfg.INTERPRETERS.update({'python3': 'python3'})
                print 'Python3.5 added to dictionary'
            if self.python_2_cb.isChecked():
                cfg.INTERPRETERS.update({'python2': 'python'})
                print 'Python2.7 added to dictionary'

    def choose_benchmark_profile(self):
        if self.benchmark_profile_time_rb.isChecked():
            cfg.BENCHMARK_PROFILES.update({'time': 'time'})
        elif self.benchmark_profile_timeit_rb.isChecked():
            cfg.BENCHMARK_PROFILES.update({'timeit': 'timeit'})

    def set_iterations_count(self):
        return self.iterations_value.toPlainText()

    @staticmethod
    def run_test(interpreter=None, benchmark=None, example=None,
                 command=None, iterations=None):
        if iterations == '':
            iterations = str(100)
        for version in interpreter.values():
            if benchmark.values() == ['time']:
                process = Popen(['time', '-v', '{}'.format(version),
                                '{}'.format(example)],
                                stdin=PIPE, stdout=PIPE, stderr=STDOUT)
                output = process.stdout.read()
                parse_obj = Parser(output)
                parse_obj.parse_time_output()

            elif benchmark.values() == ['timeit']:
                process = Popen(['{}'.format(version), '-m', 'timeit', '-v',
                                 '-n', '{}'.format(iterations), '{}'.format(command)],
                                stdin=PIPE, stdout=PIPE, stderr=STDOUT)
                output = process.stdout.read()
                print output
                # parse_obj = Parser(output)
                # parse_obj.parse_timeit_output()

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
