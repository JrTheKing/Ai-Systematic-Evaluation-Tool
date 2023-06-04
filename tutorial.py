from PyQt5 import QtWidgets, QtCore

from PyQt5.QtGui import QColor

def start_tutorial(self):

    """

    Starts a tutorial guiding the user through the application.

    Darkens the rest of the screen and focuses on specific areas.

    """

    opacity_effect = QtWidgets.QGraphicsOpacityEffect()

    opacity_effect.setOpacity(0.5)

    self.setGraphicsEffect(opacity_effect)

    

    self.focusOn(self.textbox, "This is where you input the prompt for the AI.")

    self.focusOn(self.combo_box, "Here, you can select the AI model.")

    self.focusOn(self.button, "Press this button to generate a response.")

    self.focusOn(self.output, "The AI's response will be displayed here.")

    self.focusOn(self.plot_widget, "This is the text visualization.")

    self.focusOn(self.tutorial_button, "Press this button to start the tutorial again.")

    self.setGraphicsEffect(None)

def focusOn(self, widget, message):

    """

    Highlights a specific widget and displays a message about it.

    """

    highlight = QtWidgets.QGraphicsDropShadowEffect(self)

    highlight.setBlurRadius(50)

    highlight.setColor(QColor('yellow'))

    highlight.setOffset(0)

    widget.setGraphicsEffect(highlight)

    QtWidgets.QMessageBox.information(self, "Tutorial", message)

    widget.setGraphicsEffect(None)

    QtCore.QCoreApplication.processEvents()

