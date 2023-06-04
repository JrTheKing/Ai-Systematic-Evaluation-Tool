import sys

from PyQt5 import QtWidgets

from PyQt5.QtWidgets import QApplication, QMainWindow

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

        super(MyWindow, self).__init__()

        initUI(self)

    # Function to start the tutorial.

    def start_tutorial(self):

        """Starts the tutorial"""

        start_tutorial(self)

    # Function to handle button click event.

    def clicked(self):

        """Loads the selected AI model, generates a response for the input prompt, and displays the result and visualization"""

        prompt = self.textbox.text()

        model_name = self.combo_box.currentText()

        model, tokenizer = load_model(model_name)

        response, attention_scores = generate_response(model, tokenizer, prompt)

        self.output.setPlainText(response)

        visualize_text(self.figure, self.ax, self.canvas, tokenizer, prompt)

        plot_attention_scores(self.figure, self.ax, self.canvas, tokenizer, prompt, attention_scores)

if __name__ == '__main__':

    # Check if it's the first time running the application and install necessary libraries.

    first_time = first_time_check()

    

    app = QApplication(sys.argv)

    screen = app.primaryScreen()

    screen_size = screen.size()

    # Initialize and display the main window.

    win = MyWindow()

    win.resize(screen_size * 0.9)  # 90% of screen size

    win.show()

    # Start tutorial if it's the first time running the application.

    if first_time:

        win.start_tutorial()

    sys.exit(app.exec_())

