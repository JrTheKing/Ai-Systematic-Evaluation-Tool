import os

import sys

import ctypes

import subprocess

def check_for_admin_privileges():

    """

    Checks if the program has administrative privileges. 

    Returns True if the program has administrative privileges, False otherwise.

    """

    try:

        admin = os.getuid() == 0

    except AttributeError:

        admin = ctypes.windll.shell32.IsUserAnAdmin() != 0

    return admin

def first_time_check():

    """

    Checks if it's the first time running the application.

    If it is, creates a .first_time file and returns True.

    If it's not the first time (i.e., .first_time file exists), returns False.

    """

    if not os.path.isfile('.first_time'):

        with open('.first_time', 'w') as f:

            pass

        return True

    return False

def install_libraries():

    """

    Installs necessary Python libraries. 

    It's assumed that Python (with pip) is already installed on the system.

    """

    subprocess.check_call([sys.executable, "-m", "pip", "install", "torch", "transformers", "matplotlib", "PyQt5", "pyqtgraph", "numpy"])

