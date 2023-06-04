from PyQt5 import QtWidgets, QtCore, QtGui

class SettingsWindow(QtWidgets.QMainWindow):

    def __init__(self, parent=None):

        super(SettingsWindow, self).__init__(parent)

        self.setWindowTitle('Settings')

        self.dark_mode_checkbox = QtWidgets.QCheckBox("Dark Mode", self)

        self.dark_mode_checkbox.move(20, 20)

        self.dark_mode_checkbox.stateChanged.connect(self.toggle_dark_mode)

        self.tutorial_button = QtWidgets.QPushButton("Tutorial", self)

        self.tutorial_button.move(20, 60)

        self.tutorial_button.clicked.connect(self.start_tutorial)

    def toggle_dark_mode(self, state):

        if state == QtCore.Qt.Checked:

            self.setStyleSheet("background-color: #555555;")

        else:

            self.setStyleSheet("")

    def start_tutorial(self):

        self.parent().start_tutorial()

