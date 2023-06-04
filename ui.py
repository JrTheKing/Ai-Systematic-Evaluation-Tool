from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QLineEdit, QComboBox, QPlainTextEdit, QPushButton, QLabel

from PyQt5.QtGui import QIntValidator

from settings import SettingsWindow

def initUI(self):

    self.setWindowTitle('GPT-4 Interactive')

    self.setGeometry(100, 100, 800, 600)

    # Input prompt textbox

    self.textbox = QLineEdit(self)

    self.textbox.move(20, 20)

    self.textbox.resize(280,40)

    # Model selection dropdown

    self.combo_box = QComboBox(self)

    self.combo_box.addItem('gpt2')

    self.combo_box.addItem('gpt3')

    self.combo_box.addItem('gpt4')

    self.combo_box.move(320, 20)

    # Output display area

    self.output = QPlainTextEdit(self)

    self.output.move(20, 70)

    self.output.resize(760,200)

    self.output.setReadOnly(True)

    # Generate button

    self.button = QPushButton(self)

    self.button.setText("Generate")

    self.button.move(20, 290)

    self.button.clicked.connect(self.clicked)

    # Text visualization

    self.figure = plt.figure()

    self.canvas = FigureCanvas(self.figure)

    self.ax = self.figure.add_subplot(111)

    self.plot_widget = QtWidgets.QWidget(self)

    self.plot_widget.setGeometry(QtCore.QRect(20, 350, 760, 200))

    layout = QtWidgets.QVBoxLayout(self.plot_widget)

    layout.addWidget(self.canvas)

    # Start tutorial button

    self.tutorial_button = QPushButton(self)

    self.tutorial_button.setText("Tutorial")

    self.tutorial_button.move(120, 290)

    self.tutorial_button.clicked.connect(self.start_tutorial)

    # Settings button

    self.settings_button = QPushButton(self)

    self.settings_button.setText("Settings")

    self.settings_button.move(220, 290)

    self.settings_button.clicked.connect(self.open_settings)

    # Settings window (hidden by default)

    self.settings_window = SettingsWindow(self)

    self.settings_window.hide()

def open_settings(self):

    self.settings_window.show()

