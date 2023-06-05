# Import the necessary libraries.

# The sys module provides access to some variables used or maintained by the Python interpreter and to functions that interact strongly with the interpreter.

import sys

# PyQt5 is a comprehensive set of Python bindings for Qt libraries which allows us to create GUI applications.

from PyQt5 import QtWidgets

from PyQt5.QtWidgets import QApplication, QMainWindow

# Importing the specific functions from our defined modules.

from features import first_time_check

from ui import initUI

from response import generate_response

from visualization import visualize_text, plot_attention_scores

from models import load_model

from tutorial import start_tutorial

from settings import SettingsWindow

# This class represents the main application window.

class MyWindow(QMainWindow):

    def __init__(self):

        # Call the constructor of QMainWindow

        super(MyWindow, self).__init__()

        # Initialize the user interface for the main window.

        initUI(self)

    # Function to start the tutorial.

    def start_tutorial(self):

        """This function starts the tutorial for the application."""

        start_tutorial(self)

    # Function to handle button click event.

    def clicked(self):

        """

        This function is triggered when a button is clicked.

        It loads the selected AI model, generates a response for the input prompt, and displays the result and visualization.

        """

        # Get the input text from the textbox.

        prompt = self.textbox.text()

        # Get the selected model name from the combobox.

        model_name = self.combo_box.currentText()

        # Load the selected AI model and its tokenizer.

        model, tokenizer = load_model(model_name)

        # Generate a response and attention scores using the model.

        response, attention_scores = generate_response(model, tokenizer, prompt)

        # Display the generated response in the output text field.

        self.output.setPlainText(response)

        # Visualize the input text and plot the attention scores.

        visualize_text(self.figure, self.ax, self.canvas, tokenizer, prompt)

        plot_attention_scores(self.figure, self.ax, self.canvas, tokenizer, prompt, attention_scores)

if __name__ == '__main__':

    # The main function of the script.

    

    # Check if it's the first time running the application and install necessary libraries.

    first_time = first_time_check()

    

    # QApplication manages the GUI application's control flow and main settings.

    app = QApplication(sys.argv)

    # Get the screen details.

    screen = app.primaryScreen()

    screen_size = screen.size()

    # Initialize and display the main window.

    win = MyWindow()

    # Resize the window to 90% of the screen size.

    win.resize(screen_size * 0.9)  # 90% of screen size

    win.show()

    # Start the tutorial if it's the first time running the application.

    if first_time:

        win.start_tutorial()

    # Execute the application's main loop.

    sys.exit(app.exec_())

