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

class Ui_Bytecode_analyzer(object):
    def setupUi(self, Bytecode_analyzer):
        Bytecode_analyzer.setObjectName(_fromUtf8("Bytecode_analyzer"))
        Bytecode_analyzer.resize(2205, 1080)
        self.configuration_tab = QtGui.QWidget()
        self.configuration_tab.setObjectName(_fromUtf8("configuration_tab"))
        self.benchmarks = QtGui.QLabel(self.configuration_tab)
        self.benchmarks.setGeometry(QtCore.QRect(30, 140, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.benchmarks.setFont(font)
        self.benchmarks.setObjectName(_fromUtf8("benchmarks"))
        self.benchmark_profiles_2 = QtGui.QLabel(self.configuration_tab)
        self.benchmark_profiles_2.setGeometry(QtCore.QRect(20, 370, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.benchmark_profiles_2.setFont(font)
        self.benchmark_profiles_2.setObjectName(_fromUtf8("benchmark_profiles_2"))
        self.chart_type = QtGui.QLabel(self.configuration_tab)
        self.chart_type.setGeometry(QtCore.QRect(10, 540, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.chart_type.setFont(font)
        self.chart_type.setObjectName(_fromUtf8("chart_type"))
        self.layoutWidget = QtGui.QWidget(self.configuration_tab)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 70, 461, 41))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.python_2_cb = QtGui.QCheckBox(self.layoutWidget)
        self.python_2_cb.setObjectName(_fromUtf8("python_2_cb"))
        self.horizontalLayout.addWidget(self.python_2_cb)
        self.python_3_cb = QtGui.QCheckBox(self.layoutWidget)
        self.python_3_cb.setObjectName(_fromUtf8("python_3_cb"))
        self.horizontalLayout.addWidget(self.python_3_cb)
        self.bar_chart_rb = QtGui.QRadioButton(self.configuration_tab)
        self.bar_chart_rb.setGeometry(QtCore.QRect(10, 580, 111, 22))
        self.bar_chart_rb.setObjectName(_fromUtf8("bar_chart_rb"))
        self.python_interpreter = QtGui.QLabel(self.configuration_tab)
        self.python_interpreter.setGeometry(QtCore.QRect(30, 20, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.python_interpreter.setFont(font)
        self.python_interpreter.setObjectName(_fromUtf8("python_interpreter"))
        self.layoutWidget_2 = QtGui.QWidget(self.configuration_tab)
        self.layoutWidget_2.setGeometry(QtCore.QRect(30, 410, 391, 41))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout(self.layoutWidget_2)
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.benchmark_profile_time_rb = QtGui.QRadioButton(self.layoutWidget_2)
        self.benchmark_profile_time_rb.setObjectName(_fromUtf8("benchmark_profile_time_rb"))
        self.horizontalLayout_2.addWidget(self.benchmark_profile_time_rb)
        self.iterations = QtGui.QLabel(self.configuration_tab)
        self.iterations.setGeometry(QtCore.QRect(20, 460, 461, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.iterations.setFont(font)
        self.iterations.setObjectName(_fromUtf8("iterations"))
        self.iterations_value = QtGui.QTextEdit(self.configuration_tab)
        self.iterations_value.setGeometry(QtCore.QRect(20, 500, 161, 31))
        self.iterations_value.setObjectName(_fromUtf8("iterations_value"))
        self.analyze_button = QtGui.QPushButton(self.configuration_tab)
        self.analyze_button.setGeometry(QtCore.QRect(510, 610, 99, 27))
        self.analyze_button.setObjectName(_fromUtf8("analyze_button"))
        self.progressBar = QtGui.QProgressBar(self.configuration_tab)
        self.progressBar.setGeometry(QtCore.QRect(500, 650, 118, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName(_fromUtf8("progressBar"))
        self.layoutWidget_3 = QtGui.QWidget(self.configuration_tab)
        self.layoutWidget_3.setGeometry(QtCore.QRect(30, 180, 481, 41))
        self.layoutWidget_3.setObjectName(_fromUtf8("layoutWidget_3"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.layoutWidget_3)
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.benchmark_exceptions_rb = QtGui.QRadioButton(self.layoutWidget_3)
        self.benchmark_exceptions_rb.setObjectName(_fromUtf8("benchmark_exceptions_rb"))
        self.horizontalLayout_5.addWidget(self.benchmark_exceptions_rb)
        self.benchmark_list_compr_rb = QtGui.QRadioButton(self.layoutWidget_3)
        self.benchmark_list_compr_rb.setObjectName(_fromUtf8("benchmark_list_compr_rb"))
        self.horizontalLayout_5.addWidget(self.benchmark_list_compr_rb)
        self.benchmark_generators_rb = QtGui.QRadioButton(self.layoutWidget_3)
        self.benchmark_generators_rb.setObjectName(_fromUtf8("benchmark_generators_rb"))
        self.horizontalLayout_5.addWidget(self.benchmark_generators_rb)
        self.benchmarks_2 = QtGui.QLabel(self.configuration_tab)
        self.benchmarks_2.setGeometry(QtCore.QRect(30, 240, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.benchmarks_2.setFont(font)
        self.benchmarks_2.setObjectName(_fromUtf8("benchmarks_2"))
        self.load_file_button = QtGui.QPushButton(self.configuration_tab)
        self.load_file_button.setGeometry(QtCore.QRect(50, 290, 151, 61))
        self.load_file_button.setObjectName(_fromUtf8("load_file_button"))
        self.front_image = QtGui.QLabel(self.configuration_tab)
        self.front_image.setGeometry(QtCore.QRect(740, 140, 771, 551))
        self.front_image.setObjectName(_fromUtf8("front_image"))
        self.python_interpreter_7 = QtGui.QLabel(self.configuration_tab)
        self.python_interpreter_7.setGeometry(QtCore.QRect(910, 10, 741, 91))
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.python_interpreter_7.setFont(font)
        self.python_interpreter_7.setObjectName(_fromUtf8("python_interpreter_7"))
        Bytecode_analyzer.addTab(self.configuration_tab, _fromUtf8(""))
        self.bytecode_tab = QtGui.QWidget()
        self.bytecode_tab.setObjectName(_fromUtf8("bytecode_tab"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.bytecode_tab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(40, -10, 1311, 51))
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
        self.horizontalLayoutWidget_2 = QtGui.QWidget(self.bytecode_tab)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 60, 1311, 601))
        self.horizontalLayoutWidget_2.setObjectName(_fromUtf8("horizontalLayoutWidget_2"))
        self.horizontalLayout_4 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.bytecode_python2 = QtGui.QPlainTextEdit(self.horizontalLayoutWidget_2)
        self.bytecode_python2.setObjectName(_fromUtf8("bytecode_python2"))
        self.horizontalLayout_4.addWidget(self.bytecode_python2)
        self.bytecode_python3 = QtGui.QPlainTextEdit(self.horizontalLayoutWidget_2)
        self.bytecode_python3.setObjectName(_fromUtf8("bytecode_python3"))
        self.horizontalLayout_4.addWidget(self.bytecode_python3)
        Bytecode_analyzer.addTab(self.bytecode_tab, _fromUtf8(""))
        self.bytecode_graph_tab = QtGui.QWidget()
        self.bytecode_graph_tab.setObjectName(_fromUtf8("bytecode_graph_tab"))
        self.layoutWidget1 = QtGui.QWidget(self.bytecode_graph_tab)
        self.layoutWidget1.setGeometry(QtCore.QRect(50, 0, 2141, 51))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.horizontalLayout_8 = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.python_interpreter_9 = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.python_interpreter_9.setFont(font)
        self.python_interpreter_9.setObjectName(_fromUtf8("python_interpreter_9"))
        self.horizontalLayout_8.addWidget(self.python_interpreter_9)
        self.python_interpreter_8 = QtGui.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.python_interpreter_8.setFont(font)
        self.python_interpreter_8.setObjectName(_fromUtf8("python_interpreter_8"))
        self.horizontalLayout_8.addWidget(self.python_interpreter_8)
        self.layoutWidget2 = QtGui.QWidget(self.bytecode_graph_tab)
        self.layoutWidget2.setGeometry(QtCore.QRect(-10, 50, 2061, 991))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.horizontalLayout_9 = QtGui.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.graph_2 = QtGui.QLabel(self.layoutWidget2)
        self.graph_2.setObjectName(_fromUtf8("graph_2"))
        self.horizontalLayout_9.addWidget(self.graph_2)
        self.graph_3 = QtGui.QLabel(self.layoutWidget2)
        self.graph_3.setObjectName(_fromUtf8("graph_3"))
        self.horizontalLayout_9.addWidget(self.graph_3)
        Bytecode_analyzer.addTab(self.bytecode_graph_tab, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.chart_label = QtGui.QLabel(self.tab_3)
        self.chart_label.setGeometry(QtCore.QRect(10, 110, 621, 611))
        self.chart_label.setObjectName(_fromUtf8("chart_label"))
        self.benchmark_profile_output_2 = QtGui.QPlainTextEdit(self.tab_3)
        self.benchmark_profile_output_2.setGeometry(QtCore.QRect(640, 80, 571, 641))
        self.benchmark_profile_output_2.setObjectName(_fromUtf8("benchmark_profile_output_2"))
        self.benchmark_profile_output_3 = QtGui.QPlainTextEdit(self.tab_3)
        self.benchmark_profile_output_3.setGeometry(QtCore.QRect(1230, 80, 581, 641))
        self.benchmark_profile_output_3.setObjectName(_fromUtf8("benchmark_profile_output_3"))
        self.horizontalLayoutWidget_3 = QtGui.QWidget(self.tab_3)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(30, 10, 411, 51))
        self.horizontalLayoutWidget_3.setObjectName(_fromUtf8("horizontalLayoutWidget_3"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.performance_output = QtGui.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.performance_output.setFont(font)
        self.performance_output.setObjectName(_fromUtf8("performance_output"))
        self.horizontalLayout_6.addWidget(self.performance_output)
        self.verticalLayoutWidget = QtGui.QWidget(self.tab_3)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(640, 0, 1181, 64))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.python_interpreter_5 = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.python_interpreter_5.setFont(font)
        self.python_interpreter_5.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.python_interpreter_5.setObjectName(_fromUtf8("python_interpreter_5"))
        self.verticalLayout.addWidget(self.python_interpreter_5)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.python_interpreter_6 = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.python_interpreter_6.setFont(font)
        self.python_interpreter_6.setObjectName(_fromUtf8("python_interpreter_6"))
        self.horizontalLayout_7.addWidget(self.python_interpreter_6)
        self.python_interpreter_4 = QtGui.QLabel(self.verticalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.python_interpreter_4.setFont(font)
        self.python_interpreter_4.setObjectName(_fromUtf8("python_interpreter_4"))
        self.horizontalLayout_7.addWidget(self.python_interpreter_4)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        Bytecode_analyzer.addTab(self.tab_3, _fromUtf8(""))

        self.retranslateUi(Bytecode_analyzer)
        Bytecode_analyzer.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Bytecode_analyzer)
        Bytecode_analyzer.setTabOrder(self.python_2_cb, self.python_3_cb)
        Bytecode_analyzer.setTabOrder(self.python_3_cb, self.bar_chart_rb)
        Bytecode_analyzer.setTabOrder(self.bar_chart_rb, self.benchmark_profile_time_rb)
        Bytecode_analyzer.setTabOrder(self.benchmark_profile_time_rb, self.iterations_value)
        Bytecode_analyzer.setTabOrder(self.iterations_value, self.analyze_button)
        Bytecode_analyzer.setTabOrder(self.analyze_button, self.benchmark_exceptions_rb)
        Bytecode_analyzer.setTabOrder(self.benchmark_exceptions_rb, self.benchmark_list_compr_rb)
        Bytecode_analyzer.setTabOrder(self.benchmark_list_compr_rb, self.benchmark_generators_rb)
        Bytecode_analyzer.setTabOrder(self.benchmark_generators_rb, self.bytecode_python2)
        Bytecode_analyzer.setTabOrder(self.bytecode_python2, self.bytecode_python3)
        Bytecode_analyzer.setTabOrder(self.bytecode_python3, self.benchmark_profile_output_2)
        Bytecode_analyzer.setTabOrder(self.benchmark_profile_output_2, self.benchmark_profile_output_3)
        Bytecode_analyzer.setTabOrder(self.benchmark_profile_output_3, self.load_file_button)

    def retranslateUi(self, Bytecode_analyzer):
        Bytecode_analyzer.setWindowTitle(_translate("Bytecode_analyzer", "Bytecode_analyzer", None))
        self.benchmarks.setText(_translate("Bytecode_analyzer", "Sample benchmarks", None))
        self.benchmark_profiles_2.setText(_translate("Bytecode_analyzer", "Benchmark profiles", None))
        self.chart_type.setText(_translate("Bytecode_analyzer", "Chart type", None))
        self.python_2_cb.setText(_translate("Bytecode_analyzer", "Python 2.7.12", None))
        self.python_3_cb.setText(_translate("Bytecode_analyzer", "Python 3.5.2", None))
        self.bar_chart_rb.setText(_translate("Bytecode_analyzer", "Bar chart", None))
        self.python_interpreter.setText(_translate("Bytecode_analyzer", "Python interpreter", None))
        self.benchmark_profile_time_rb.setText(_translate("Bytecode_analyzer", "Linux time", None))
        self.iterations.setText(_translate("Bytecode_analyzer", "Iterations (not implemented yet)", None))
        self.analyze_button.setText(_translate("Bytecode_analyzer", "Analyze", None))
        self.benchmark_exceptions_rb.setText(_translate("Bytecode_analyzer", "Handling exceptions", None))
        self.benchmark_list_compr_rb.setText(_translate("Bytecode_analyzer", "List comprehension", None))
        self.benchmark_generators_rb.setText(_translate("Bytecode_analyzer", "Generators", None))
        self.benchmarks_2.setText(_translate("Bytecode_analyzer", "Custom benchmarks", None))
        self.load_file_button.setText(_translate("Bytecode_analyzer", "Choose Python file", None))
        self.front_image.setText(_translate("Bytecode_analyzer", "TextLabel", None))
        self.python_interpreter_7.setText(_translate("Bytecode_analyzer", "Python bytecode analyzer", None))
        Bytecode_analyzer.setTabText(Bytecode_analyzer.indexOf(self.configuration_tab), _translate("Bytecode_analyzer", "Configuration", None))
        self.python_interpreter_2.setText(_translate("Bytecode_analyzer", "Python 2.7.12 ", None))
        self.python_interpreter_3.setText(_translate("Bytecode_analyzer", "Python 3.5.2", None))
        Bytecode_analyzer.setTabText(Bytecode_analyzer.indexOf(self.bytecode_tab), _translate("Bytecode_analyzer", "Bytecode", None))
        self.python_interpreter_9.setText(_translate("Bytecode_analyzer", "Python 2.7.12 ", None))
        self.python_interpreter_8.setText(_translate("Bytecode_analyzer", "Python 3.5.2", None))
        self.graph_2.setText(_translate("Bytecode_analyzer", "TextLabel", None))
        self.graph_3.setText(_translate("Bytecode_analyzer", "TextLabel", None))
        Bytecode_analyzer.setTabText(Bytecode_analyzer.indexOf(self.bytecode_graph_tab), _translate("Bytecode_analyzer", "Bytecode graph", None))
        self.chart_label.setText(_translate("Bytecode_analyzer", "TextLabel", None))
        self.performance_output.setText(_translate("Bytecode_analyzer", "Performance output", None))
        self.python_interpreter_5.setText(_translate("Bytecode_analyzer", "Benchmark profile ", None))
        self.python_interpreter_6.setText(_translate("Bytecode_analyzer", "Python 2.7.12 ", None))
        self.python_interpreter_4.setText(_translate("Bytecode_analyzer", "Python 3.5.2", None))
        Bytecode_analyzer.setTabText(Bytecode_analyzer.indexOf(self.tab_3), _translate("Bytecode_analyzer", "Performance", None))

