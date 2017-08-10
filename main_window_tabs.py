# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window_with_tabs.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_TabWidget(object):
    def setupUi(self, TabWidget):
        TabWidget.setObjectName("TabWidget")
        TabWidget.resize(1351, 987)
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.benchmarks = QtWidgets.QLabel(self.tab)
        self.benchmarks.setGeometry(QtCore.QRect(30, 140, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.benchmarks.setFont(font)
        self.benchmarks.setObjectName("benchmarks")
        self.benchmark_profiles_2 = QtWidgets.QLabel(self.tab)
        self.benchmark_profiles_2.setGeometry(QtCore.QRect(20, 370, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.benchmark_profiles_2.setFont(font)
        self.benchmark_profiles_2.setObjectName("benchmark_profiles_2")
        self.chart_type = QtWidgets.QLabel(self.tab)
        self.chart_type.setGeometry(QtCore.QRect(10, 540, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.chart_type.setFont(font)
        self.chart_type.setObjectName("chart_type")
        self.layoutWidget = QtWidgets.QWidget(self.tab)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 70, 461, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.python_2_cb = QtWidgets.QCheckBox(self.layoutWidget)
        self.python_2_cb.setObjectName("python_2_cb")
        self.horizontalLayout.addWidget(self.python_2_cb)
        self.python_3_cb = QtWidgets.QCheckBox(self.layoutWidget)
        self.python_3_cb.setObjectName("python_3_cb")
        self.horizontalLayout.addWidget(self.python_3_cb)
        self.bar_chart_rb = QtWidgets.QRadioButton(self.tab)
        self.bar_chart_rb.setGeometry(QtCore.QRect(10, 580, 111, 22))
        self.bar_chart_rb.setObjectName("bar_chart_rb")
        self.python_interpreter = QtWidgets.QLabel(self.tab)
        self.python_interpreter.setGeometry(QtCore.QRect(30, 20, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.python_interpreter.setFont(font)
        self.python_interpreter.setObjectName("python_interpreter")
        self.layoutWidget_2 = QtWidgets.QWidget(self.tab)
        self.layoutWidget_2.setGeometry(QtCore.QRect(30, 410, 391, 41))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.benchmark_profile_time_rb = QtWidgets.QRadioButton(self.layoutWidget_2)
        self.benchmark_profile_time_rb.setObjectName("benchmark_profile_time_rb")
        self.horizontalLayout_2.addWidget(self.benchmark_profile_time_rb)
        self.iterations = QtWidgets.QLabel(self.tab)
        self.iterations.setGeometry(QtCore.QRect(20, 460, 461, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.iterations.setFont(font)
        self.iterations.setObjectName("iterations")
        self.iterations_value = QtWidgets.QTextEdit(self.tab)
        self.iterations_value.setGeometry(QtCore.QRect(20, 500, 161, 31))
        self.iterations_value.setObjectName("iterations_value")
        self.analyze_button = QtWidgets.QPushButton(self.tab)
        self.analyze_button.setGeometry(QtCore.QRect(510, 610, 99, 27))
        self.analyze_button.setObjectName("analyze_button")
        self.progressBar = QtWidgets.QProgressBar(self.tab)
        self.progressBar.setGeometry(QtCore.QRect(500, 650, 118, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.layoutWidget_3 = QtWidgets.QWidget(self.tab)
        self.layoutWidget_3.setGeometry(QtCore.QRect(30, 180, 481, 41))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.benchmark_exceptions_rb = QtWidgets.QRadioButton(self.layoutWidget_3)
        self.benchmark_exceptions_rb.setObjectName("benchmark_exceptions_rb")
        self.horizontalLayout_5.addWidget(self.benchmark_exceptions_rb)
        self.benchmark_list_compr_rb = QtWidgets.QRadioButton(self.layoutWidget_3)
        self.benchmark_list_compr_rb.setObjectName("benchmark_list_compr_rb")
        self.horizontalLayout_5.addWidget(self.benchmark_list_compr_rb)
        self.benchmark_generators_rb = QtWidgets.QRadioButton(self.layoutWidget_3)
        self.benchmark_generators_rb.setObjectName("benchmark_generators_rb")
        self.horizontalLayout_5.addWidget(self.benchmark_generators_rb)
        self.benchmarks_2 = QtWidgets.QLabel(self.tab)
        self.benchmarks_2.setGeometry(QtCore.QRect(30, 240, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.benchmarks_2.setFont(font)
        self.benchmarks_2.setObjectName("benchmarks_2")
        self.load_file_button = QtWidgets.QPushButton(self.tab)
        self.load_file_button.setGeometry(QtCore.QRect(50, 290, 151, 61))
        self.load_file_button.setObjectName("load_file_button")
        self.front_image = QtWidgets.QLabel(self.tab)
        self.front_image.setGeometry(QtCore.QRect(740, 140, 461, 401))
        self.front_image.setObjectName("front_image")
        self.python_interpreter_7 = QtWidgets.QLabel(self.tab)
        self.python_interpreter_7.setGeometry(QtCore.QRect(730, 20, 481, 91))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.python_interpreter_7.setFont(font)
        self.python_interpreter_7.setObjectName("python_interpreter_7")
        TabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab_2)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 1311, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.python_interpreter_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.python_interpreter_2.setFont(font)
        self.python_interpreter_2.setObjectName("python_interpreter_2")
        self.horizontalLayout_3.addWidget(self.python_interpreter_2)
        self.python_interpreter_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.python_interpreter_3.setFont(font)
        self.python_interpreter_3.setObjectName("python_interpreter_3")
        self.horizontalLayout_3.addWidget(self.python_interpreter_3)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 60, 1311, 601))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.bytecode_python2 = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget_2)
        self.bytecode_python2.setObjectName("bytecode_python2")
        self.horizontalLayout_4.addWidget(self.bytecode_python2)
        self.bytecode_python3 = QtWidgets.QPlainTextEdit(self.horizontalLayoutWidget_2)
        self.bytecode_python3.setObjectName("bytecode_python3")
        self.horizontalLayout_4.addWidget(self.bytecode_python3)
        TabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.chart_label = QtWidgets.QLabel(self.tab_3)
        self.chart_label.setGeometry(QtCore.QRect(10, 150, 421, 341))
        self.chart_label.setObjectName("chart_label")
        self.benchmark_profile_output_2 = QtWidgets.QPlainTextEdit(self.tab_3)
        self.benchmark_profile_output_2.setGeometry(QtCore.QRect(440, 80, 441, 511))
        self.benchmark_profile_output_2.setObjectName("benchmark_profile_output_2")
        self.benchmark_profile_output_3 = QtWidgets.QPlainTextEdit(self.tab_3)
        self.benchmark_profile_output_3.setGeometry(QtCore.QRect(890, 80, 441, 511))
        self.benchmark_profile_output_3.setObjectName("benchmark_profile_output_3")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.tab_3)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(30, 10, 411, 51))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.performance_output = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.performance_output.setFont(font)
        self.performance_output.setObjectName("performance_output")
        self.horizontalLayout_6.addWidget(self.performance_output)
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tab_3)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(470, 10, 851, 64))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.python_interpreter_5 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.python_interpreter_5.setFont(font)
        self.python_interpreter_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.python_interpreter_5.setObjectName("python_interpreter_5")
        self.verticalLayout.addWidget(self.python_interpreter_5)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.python_interpreter_6 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.python_interpreter_6.setFont(font)
        self.python_interpreter_6.setObjectName("python_interpreter_6")
        self.horizontalLayout_7.addWidget(self.python_interpreter_6)
        self.python_interpreter_4 = QtWidgets.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.python_interpreter_4.setFont(font)
        self.python_interpreter_4.setObjectName("python_interpreter_4")
        self.horizontalLayout_7.addWidget(self.python_interpreter_4)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        TabWidget.addTab(self.tab_3, "")

        self.retranslateUi(TabWidget)
        TabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(TabWidget)
        TabWidget.setTabOrder(self.python_2_cb, self.python_3_cb)
        TabWidget.setTabOrder(self.python_3_cb, self.bar_chart_rb)
        TabWidget.setTabOrder(self.bar_chart_rb, self.benchmark_profile_time_rb)
        TabWidget.setTabOrder(self.benchmark_profile_time_rb, self.iterations_value)
        TabWidget.setTabOrder(self.iterations_value, self.analyze_button)
        TabWidget.setTabOrder(self.analyze_button, self.benchmark_exceptions_rb)
        TabWidget.setTabOrder(self.benchmark_exceptions_rb, self.benchmark_list_compr_rb)
        TabWidget.setTabOrder(self.benchmark_list_compr_rb, self.benchmark_generators_rb)
        TabWidget.setTabOrder(self.benchmark_generators_rb, self.bytecode_python2)
        TabWidget.setTabOrder(self.bytecode_python2, self.bytecode_python3)
        TabWidget.setTabOrder(self.bytecode_python3, self.benchmark_profile_output_2)
        TabWidget.setTabOrder(self.benchmark_profile_output_2, self.benchmark_profile_output_3)
        TabWidget.setTabOrder(self.benchmark_profile_output_3, self.load_file_button)

    def retranslateUi(self, TabWidget):
        _translate = QtCore.QCoreApplication.translate
        TabWidget.setWindowTitle(_translate("TabWidget", "TabWidget"))
        self.benchmarks.setText(_translate("TabWidget", "Sample benchmarks"))
        self.benchmark_profiles_2.setText(_translate("TabWidget", "Benchmark profiles"))
        self.chart_type.setText(_translate("TabWidget", "Chart type"))
        self.python_2_cb.setText(_translate("TabWidget", "Python 2.7.12"))
        self.python_3_cb.setText(_translate("TabWidget", "Python 3.5.2"))
        self.bar_chart_rb.setText(_translate("TabWidget", "Bar chart"))
        self.python_interpreter.setText(_translate("TabWidget", "Python interpreter"))
        self.benchmark_profile_time_rb.setText(_translate("TabWidget", "Linux time"))
        self.iterations.setText(_translate("TabWidget", "Iterations (not implemented yet)"))
        self.analyze_button.setText(_translate("TabWidget", "Analyze"))
        self.benchmark_exceptions_rb.setText(_translate("TabWidget", "Handling exceptions"))
        self.benchmark_list_compr_rb.setText(_translate("TabWidget", "List comprehension"))
        self.benchmark_generators_rb.setText(_translate("TabWidget", "Generators"))
        self.benchmarks_2.setText(_translate("TabWidget", "Custom benchmarks"))
        self.load_file_button.setText(_translate("TabWidget", "Choose Python file"))
        self.front_image.setText(_translate("TabWidget", "TextLabel"))
        self.python_interpreter_7.setText(_translate("TabWidget", "Python bytecode analyzer"))
        TabWidget.setTabText(TabWidget.indexOf(self.tab), _translate("TabWidget", "Configuration"))
        self.python_interpreter_2.setText(_translate("TabWidget", "Python 2.7.12 "))
        self.python_interpreter_3.setText(_translate("TabWidget", "Python 3.5.2"))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_2), _translate("TabWidget", "Bytecode"))
        self.chart_label.setText(_translate("TabWidget", "TextLabel"))
        self.performance_output.setText(_translate("TabWidget", "Performance output"))
        self.python_interpreter_5.setText(_translate("TabWidget", "Benchmark profile "))
        self.python_interpreter_6.setText(_translate("TabWidget", "Python 2.7.12 "))
        self.python_interpreter_4.setText(_translate("TabWidget", "Python 3.5.2"))
        TabWidget.setTabText(TabWidget.indexOf(self.tab_3), _translate("TabWidget", "Performance"))

