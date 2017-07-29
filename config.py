import os

HOME_PATH = os.getcwd()
EXAMPLES_PATH_2 = os.path.join(HOME_PATH, 'python_2_examples')
EXAMPLES_PATH_3 = os.path.join(HOME_PATH, 'python_3_examples')
PYC_FILES_PYTHON_2_RELATIVE = 'python_2_examples'
PYC_FILES_PYTHON_3_RELATIVE = 'python_3_examples/__pycache__'
VENV_2_PATH = os.path.join(HOME_PATH, 'venv_analyzer2', 'bin')
VENV_3_PATH = os.path.join(HOME_PATH, 'venv_analyzer3', 'bin')
PYC_OUTPUT_FILE_2 = 'dis_output_2'
PYC_OUTPUT_FILE_3 = 'dis_output_3'



TEST_FILE = str()
INTERPRETERS = dict()
BENCHMARK_PROFILES = dict()