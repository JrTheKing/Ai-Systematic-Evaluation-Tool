# The PyQt5.QtWidgets module provides a set of UI elements to create classic desktop-style user interfaces.

# The PyQt5.QtCore module provides core non-GUI functionality. QtCore.Qt contains core enums and flags.

# The PyQt5.QtGui module extends QtCore with GUI functionality.

from PyQt5 import QtWidgets, QtCore, QtGui

# This class represents the settings window for the application.

class SettingsWindow(QtWidgets.QMainWindow):

    # This function initializes the SettingsWindow object. 

    # It takes an optional parameter 'parent', which refers to the parent widget. If the parent is not specified, the window will be free-floating.

    def __init__(self, parent=None):

        # Here, super() is called without any parameters to call the base class constructor. 

        # This is a way of calling the parent's methods from the child class.

        super(SettingsWindow, self).__init__(parent)

        # Set the title of the window to 'Settings'.

        self.setWindowTitle('Settings')

        # A checkbox is created for the dark mode option. The label of the checkbox is "Dark Mode".

        # The 'self' parameter makes 'SettingsWindow' the parent of this widget.

        self.dark_mode_checkbox = QtWidgets.QCheckBox("Dark Mode", self)

        self.dark_mode_checkbox.move(20, 20)  # Places the checkbox at the position (20,20) in the parent widget's coordinates.

        # The stateChanged signal of the checkbox is connected to the 'toggle_dark_mode' slot. 

        # Whenever the checkbox's state is changed, the 'toggle_dark_mode' function is called.

        self.dark_mode_checkbox.stateChanged.connect(self.toggle_dark_mode)

        # A push button is created with the label 'Tutorial'. The 'self' parameter makes 'SettingsWindow' the parent of this widget.

        self.tutorial_button = QtWidgets.QPushButton("Tutorial", self)

        self.tutorial_button.move(20, 60)  # Places the button at the position (20,60) in the parent widget's coordinates.

        # The clicked signal of the button is connected to the 'start_tutorial' slot.

        # Whenever the button is clicked, the 'start_tutorial' function is called.

        self.tutorial_button.clicked.connect(self.start_tutorial)

    # This function toggles the dark mode based on the state of the checkbox.

    def toggle_dark_mode(self, state):

        # The state is checked to see if it's equal to QtCore.Qt.Checked, which indicates that the checkbox is checked.

        if state == QtCore.Qt.Checked:

            # If the checkbox is checked, the background color of the SettingsWindow is set to a dark color using a style sheet.

            self.setStyleSheet("background-color: #555555;")

        else:

            # If the checkbox is not checked, the style sheet is set to an empty string, effectively removing the dark mode styling.

            self.setStyleSheet("")

    # This function calls the 'start_tutorial' function of the parent widget.

    def start_tutorial(self):

        # The parent() method returns the parent widget of the current widget. The 'start_tutorial' function of the parent widget is called.

        self.parent().start_tutorial()

