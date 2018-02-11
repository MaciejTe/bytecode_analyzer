from sys import version_info
if not version_info.major == 3:
    from bytecode_graph import *
    from render import *
