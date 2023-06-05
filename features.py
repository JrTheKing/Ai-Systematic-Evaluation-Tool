# os and sys are built-in Python modules for interacting with the operating system.

# ctypes is a Python library for calling C functions in DLLs/shared libraries and for creating,

# manipulating and managing Python C data types.

# subprocess allows you to spawn new processes, connect to their input/output/error pipes, and obtain their return codes.

import os

import sys

import ctypes

import subprocess

def check_for_admin_privileges():

    """

    This function checks if the current process has administrative privileges.

    It handles different approaches for Unix and Windows systems.

    Returns:

        bool: True if the current process has administrative privileges, False otherwise.

    """

    try:

        # In Unix systems, user ID 0 is reserved for the root user.

        # os.getuid() gets the current process’s real user id. If it equals 0, then the current process has admin privileges.

        admin = os.getuid() == 0

    except AttributeError:

        # In case of Windows, the IsUserAnAdmin function checks if the current user is a member of the Administrator's group.

        # If the function call returns a nonzero value, the current user has admin privileges.

        admin = ctypes.windll.shell32.IsUserAnAdmin() != 0

    return admin

def first_time_check():

    """

    This function checks if it's the first time running the application.

    It does this by looking for a '.first_time' file in the current directory.

    Returns:

        bool: True if it's the first time the application is being run, False otherwise.

    """

    # Checks if the .first_time file exists in the current directory

    if not os.path.isfile('.first_time'):

        # If not, it means it's the first time running the application.

        # So, creates a .first_time file and returns True.

        with open('.first_time', 'w') as f:

            pass

        return True

    # If the .first_time file exists, it's not the first time running the application, so returns False.

    return False

def install_libraries():

    """

    This function is responsible for installing the necessary Python libraries.

    It uses the subprocess module to call pip (Python's package installer) to install each library.

    Note: It's assumed that Python (with pip) is already installed on the system.

    """

    # Calls pip through subprocess to install the necessary libraries.

    # sys.executable points to the Python interpreter that's currently running the script.

    # "-m" tells Python to run the pip module as a script.

    # "install" is the command passed to pip to install the packages that follow.

    subprocess.check_call([sys.executable, "-m", "pip", "install", "torch", "transformers", "matplotlib", "PyQt5", "pyqtgraph", "numpy"])
