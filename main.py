# Import necessary libraries

import sys  # Provides access to Python interpreter variables and functions

from PyQt5 import QtWidgets  # PyQt5 is a set of Python bindings for Qt libraries, used for creating GUI

from PyQt5.QtWidgets import QApplication, QMainWindow  # Specific classes for creating application object and main window

# Import other modules specific to this application

from features import first_time_check  # Function to check if this is the first run of the application

from ui import initUI  # Function to initialize the user interface

from response import generate_response  # Function to generate a response using AI model

from visualization import visualize_text, plot_attention_scores  # Functions to visualize text and attention scores

from models import load_model  # Function to load an AI model

from tutorial import start_tutorial  # Function to start a tutorial

class MyWindow(QMainWindow):  # Define main application window as a class that inherits from QMainWindow

    def __init__(self):

        super(MyWindow, self).__init__()  # Call constructor of QMainWindow to set up window

        initUI(self)  # Call function to initialize user interface of the window

    def start_tutorial(self):

        start_tutorial(self)  # Call tutorial function to display tutorial

    def clicked(self):

        """

        This function is called when a button is clicked. It loads the selected AI model,

        generates a response for the input prompt, displays the response in the output field,

        and visualizes the input text and attention scores.

        """

        prompt = self.textbox.text()  # Get input text from textbox

        model_name = self.combo_box.currentText()  # Get selected model name from combobox

        # Load the selected AI model and its tokenizer

        model, tokenizer = load_model(model_name)

        # Generate a response and attention scores using the model

        response, attention_scores = generate_response(model, tokenizer, prompt)

        self.output.setPlainText(response)  # Display the generated response in the output text field

        # Visualize the input text and plot the attention scores

        visualize_text(self.figure, self.ax, self.canvas, tokenizer, prompt)

        plot_attention_scores(self.figure, self.ax, self.canvas, tokenizer, prompt, attention_scores)

# Main function of the script

if __name__ == '__main__':

    # Check if it's the first time running the application and install necessary libraries

    first_time = first_time_check()

    app = QApplication(sys.argv)  # QApplication manages the GUI application's control flow and main settings

    screen = app.primaryScreen()  # Get the screen details

    screen_size = screen.size()  # Get the screen size

    win = MyWindow()  # Initialize main window

    win.resize(screen_size * 0.9)  # Resize the window to 90% of the screen size

    win.show()  # Display the window

    # Start the tutorial if it's the first time running the application

    if first_time:

        win.start_tutorial()

    # Execute the application's main loop

    sys.exit(app.exec_())

