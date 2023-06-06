# The QtCore, QtGui, and QtWidgets modules are imported from the PyQt5 library. 

# QtCore contains the core non-GUI functionality. QtGui contains classes for window system integration, event handling, and 2D graphics. QtWidgets module provides a set of UI elements to create classic desktop-style user interfaces.

from PyQt5 import QtCore, QtGui, QtWidgets

# QLineEdit is a widget that allows the user to enter and edit a single line of plain text.

# QComboBox is a widget that is a combination of a drop-down list or a list box and an editable textbox, allowing the user to either enter a value directly or select a value from the list.

# QPlainTextEdit is a widget that provides a way to edit and display plain text.

# QPushButton is a widget that creates a push button, which is a clickable button.

# QLabel is a widget that provides a text or image display.

from PyQt5.QtWidgets import QLineEdit, QComboBox, QPlainTextEdit, QPushButton, QLabel

# QIntValidator ensures that a string contains only an integer within a specified range. This is useful for limiting input within certain numerical bounds.

from PyQt5.QtGui import QIntValidator

# The SettingsWindow class is imported from the settings module. This class defines the UI and functionality for the settings window.

from settings import SettingsWindow

# Importing pyplot as plt

import matplotlib.pyplot as plt

# FigureCanvasQTAgg is a widget object that is required to display any matplotlib figures in a PyQt5 application.

# It is imported from the backend of matplotlib that is designed to be used with PyQt5.

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

# Define the function to initialize the UI components of the main application.

def initUI(self):

    """Initializes the user interface elements of the main window."""

    

    # Set the window title to 'GPT-4 Interactive'.

    self.setWindowTitle('GPT-4 Interactive')

    # The setGeometry() method defines the initial window size as well as its position on the screen. The arguments are (x position, y position, width, height).

    self.setGeometry(100, 100, 800, 600)

    # The QLineEdit() constructor creates a new line edit widget with the parent window as the argument. The user will enter their prompt in this textbox.

    self.textbox = QLineEdit(self)

    self.textbox.move(20, 20)  # The move() method moves the widget to a position relative to its parent. The position is specified in pixels.

    self.textbox.resize(280,40)  # The resize() method changes the size of the widget to the specified width and height in pixels.

    # The QComboBox() constructor creates a new dropdown box widget with the parent window as the argument. This dropdown box will allow the user to select the AI model.

    self.combo_box = QComboBox(self)

    self.combo_box.addItem('gpt2')  # addItem() method adds an item to the end of the dropdown list.

    self.combo_box.addItem('gpt3')

    self.combo_box.addItem('gpt4')

    self.combo_box.move(320, 20)

    # The QPlainTextEdit() constructor creates a new text area widget with the parent window as the argument. This area will display the output of the AI model.

    self.output = QPlainTextEdit(self)

    self.output.move(20, 70)

    self.output.resize(760,200)

    self.output.setReadOnly(True)  # setReadOnly(True) method makes the text area read-only, so the user cannot modify the displayed text.

    # The QPushButton() constructor creates a new button with the parent window as the argument. This button will trigger the generation of text from the selected AI model when clicked.

    self.button = QPushButton(self)

    self.button.setText("Generate")  # setText() method sets the text of the button.

    self.button.move(20, 290)

    self.button.clicked.connect(self.clicked)  # When the button is clicked, it will call the clicked() method of the window.

    # Set up the elements for text visualization.

    self.figure = plt.figure()  # Create a new figure for plotting.

    self.canvas = FigureCanvas(self.figure)  # Create a canvas to display the figure.

    self.ax = self.figure.add_subplot(111)  # Add a subplot to the figure.

    self.plot_widget = QtWidgets.QWidget(self)  # Create a new widget in the window to display the plot.

    self.plot_widget.setGeometry(QtCore.QRect(20, 350, 760, 200))  # Set the position and size of the plot widget.

    layout = QtWidgets.QVBoxLayout(self.plot_widget)  # Create a vertical box layout for the plot widget.

    layout.addWidget(self.canvas)  # Add the canvas to the layout of the plot widget.

    # The QPushButton() constructor creates a new button with the parent window as the argument. This button will start the tutorial when clicked.

    self.tutorial_button = QPushButton(self)

    self.tutorial_button.setText("Tutorial")

    self.tutorial_button.move(120, 290)

    self.tutorial_button.clicked.connect(self.start_tutorial)  # When the button is clicked, it will call the start_tutorial() method of the window.

    # The QPushButton() constructor creates a new button with the parent window as the argument. This button will open the settings window when clicked.

    self.settings_button = QPushButton(self)

    self.settings_button.setText("Settings")

    self.settings_button.move(220, 290)

    self.settings_button.clicked.connect(self.open_settings)  # When the button is clicked, it will call the open_settings() method of the window.

    # Initialize the settings window (hidden by default).

    self.settings_window = SettingsWindow(self)

    self.settings_window.hide()

# Define the function to open the settings window when the settings button is clicked.

def open_settings(self):

    """Opens the settings window."""

    self.settings_window.show()
