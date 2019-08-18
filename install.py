"""
Do not edit using from a template
"""

import os
import sys
from info import info

python = sys.executable
install_cmd = "setup.py install"
uninstall_cmd = "-m pip uninstall -y"
script_dir = os.path.dirname(os.path.realpath(__file__))

cmd_uninstall = " ".join([python, uninstall_cmd, info['name']])
os.system(cmd_uninstall)

cmd_install = " ".join([python, install_cmd, script_dir])
os.system(cmd_install)
