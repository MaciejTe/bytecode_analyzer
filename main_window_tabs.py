# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window_with_tabs.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_TabWidget(object):
    def setupUi(self, TabWidget):
        TabWidget.setObjectName(_fromUtf8("TabWidget"))
        TabWidget.resize(983, 733)
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.benchmarks = QtGui.QLabel(self.tab)
        self.benchmarks.setGeometry(QtCore.QRect(20, 120, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.benchmarks.setFont(font)
        self.benchmarks.setObjectName(_fromUtf8("benchmarks"))
        self.benchmark_profiles_2 = QtGui.QLabel(self.tab)
        self.benchmark_profiles_2.setGeometry(QtCore.QRect(30, 200, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.benchmark_profiles_2.setFont(font)
        self.benchmark_profiles_2.setObjectName(_fromUtf8("benchmark_profiles_2"))
        self.chart_type = QtGui.QLabel(self.tab)
        self.chart_type.setGeometry(QtCore.QRect(20, 370, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.chart_type.setFont(font)
        self.chart_type.setObjectName(_fromUtf8("chart_type"))
        self.layoutWidget = QtGui.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 70, 831, 41))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.python_2_cb = QtGui.QCheckBox(self.layoutWidget)
        self.python_2_cb.setObjectName(_fromUtf8("python_2_cb"))
        self.horizontalLayout.addWidget(self.python_2_cb)
        self.python_3_cb = QtGui.QCheckBox(self.layoutWidget)
        self.python_3_cb.setObjectName(_fromUtf8("python_3_cb"))
        self.horizontalLayout.addWidget(self.python_3_cb)
        self.chart_type_1 = QtGui.QCheckBox(self.tab)
        self.chart_type_1.setGeometry(QtCore.QRect(20, 410, 407, 22))
        self.chart_type_1.setObjectName(_fromUtf8("chart_type_1"))
        self.python_interpreter = QtGui.QLabel(self.tab)
        self.python_interpreter.setGeometry(QtCore.QRect(30, 20, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.python_interpreter.setFont(font)
        self.python_interpreter.setObjectName(_fromUtf8("python_interpreter"))
        self.chart_type_2 = QtGui.QCheckBox(self.tab)
        self.chart_type_2.setGeometry(QtCore.QRect(20, 440, 407, 22))
        self.chart_type_2.setObjectName(_fromUtf8("chart_type_2"))
        self.layoutWidget_2 = QtGui.QWidget(self.tab)
        self.layoutWidget_2.setGeometry(QtCore.QRect(40, 240, 821, 41))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.benchmark_profile_time_rb = QtGui.QRadioButton(self.layoutWidget_2)
        self.benchmark_profile_time_rb.setObjectName(_fromUtf8("benchmark_profile_time_rb"))
        self.horizontalLayout_2.addWidget(self.benchmark_profile_time_rb)
        self.benchmark_profile_timeit_rb = QtGui.QRadioButton(self.layoutWidget_2)
        self.benchmark_profile_timeit_rb.setObjectName(_fromUtf8("benchmark_profile_timeit_rb"))
        self.horizontalLayout_2.addWidget(self.benchmark_profile_timeit_rb)
        self.iterations = QtGui.QLabel(self.tab)
        self.iterations.setGeometry(QtCore.QRect(20, 280, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.iterations.setFont(font)
        self.iterations.setObjectName(_fromUtf8("iterations"))
        self.iterations_value = QtGui.QTextEdit(self.tab)
        self.iterations_value.setGeometry(QtCore.QRect(10, 320, 161, 31))
        self.iterations_value.setObjectName(_fromUtf8("iterations_value"))
        self.analyze_button = QtGui.QPushButton(self.tab)
        self.analyze_button.setGeometry(QtCore.QRect(830, 610, 99, 27))
        self.analyze_button.setObjectName(_fromUtf8("analyze_button"))
        self.progressBar = QtGui.QProgressBar(self.tab)
        self.progressBar.setGeometry(QtCore.QRect(820, 650, 118, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        TabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.tab_2)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 961, 51))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.python_interpreter_2 = QtGui.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.python_interpreter_2.setFont(font)
        self.python_interpreter_2.setObjectName(_fromUtf8("python_interpreter_2"))
        self.horizontalLayout_3.addWidget(self.python_interpreter_2)
        self.python_interpreter_3 = QtGui.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.python_interpreter_3.setFont(font)
        self.python_interpreter_3.setObjectName(_fromUtf8("python_interpreter_3"))
        self.horizontalLayout_3.addWidget(self.python_interpreter_3)
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.tab_2)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 60, 961, 601))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.bytecode_python2 = QtGui.QTextEdit(self.horizontalLayoutWidget_2)
        self.bytecode_python2.setObjectName(_fromUtf8("bytecode_python2"))
        self.horizontalLayout_4.addWidget(self.bytecode_python2)
        self.bytecode_python3 = QtGui.QTextEdit(self.horizontalLayoutWidget_2)
        self.bytecode_python3.setObjectName(_fromUtf8("bytecode_python3"))
        self.horizontalLayout_4.addWidget(self.bytecode_python3)
        TabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab1 = QtGui.QWidget()
        self.tab1.setObjectName(_fromUtf8("tab1"))
        TabWidget.addTab(self.tab1, _fromUtf8(""))

        self.retranslateUi(TabWidget)
        TabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(TabWidget)

    def retranslateUi(self, TabWidget):
        TabWidget.setWindowTitle(_translate("TabWidget", "TabWidget", None))
        self.benchmarks.setText(_translate("TabWidget", "Benchmarks (TODO)", None))
        self.benchmark_profiles_2.setText(_translate("TabWidget", "Benchmark profiles", None))
        self.chart_type.setText(_translate("TabWidget", "Chart type", None))
        self.python_2_cb.setText(_translate("TabWidget", "Python 2.7.12", None))
        self.python_3_cb.setText(_translate("TabWidget", "Python 3.5.2", None))
        self.chart_type_1.setText(_translate("TabWidget", "Flow chart", None))
        self.python_interpreter.setText(_translate("TabWidget", "Python interpreter", None))
        self.chart_type_2.setText(_translate("TabWidget", "Whatever", None))
        self.benchmark_profile_time_rb.setText(_translate("TabWidget", "Linux time", None))
        self.benchmark_profile_timeit_rb.setText(_translate("TabWidget", "Timeit", None))
        self.iterations.setText(_translate("TabWidget", "Iterations", None))
        self.analyze_button.setText(_translate("TabWidget", "Analyze", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab), _translate("TabWidget", "Configuration", None))
        self.python_interpreter_2.setText(_translate("TabWidget", "Python 2.7.12 ", None))
        self.python_interpreter_3.setText(_translate("TabWidget", "Python 3.5.2", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_2), _translate("TabWidget", "Bytecode", None))
        TabWidget.setTabText(TabWidget.indexOf(self.tab1), _translate("TabWidget", "Performance", None))
