# The QtWidgets and QtCore modules are imported from PyQt5. QtWidgets contains a set of UI elements to create classic desktop-style user interfaces, and QtCore contains the core non-GUI functionality.

from PyQt5 import QtWidgets, QtCore

# QColor class provides colors based on RGB, HSV or CMYK values.

from PyQt5.QtGui import QColor

# This function initiates the tutorial process for the application.

def start_tutorial(self):

    """

    Starts a tutorial guiding the user through the application.

    Darkens the rest of the screen and focuses on specific areas.

    """

    # QGraphicsOpacityEffect is a class that provides an opacity effect.

    opacity_effect = QtWidgets.QGraphicsOpacityEffect()

    opacity_effect.setOpacity(0.5)  # setOpacity() method changes the opacity of the UI. Here it's set to 0.5 to darken the screen.

    # setGraphicsEffect() method applies an effect to the widget. Here the opacity effect is applied to the main window, effectively darkening the entire screen.

    self.setGraphicsEffect(opacity_effect)

    # Calls the focusOn function for each of the important widgets in the UI, explaining each in turn.

    self.focusOn(self.textbox, "This is where you input the prompt for the AI.")

    self.focusOn(self.combo_box, "Here, you can select the AI model.")

    self.focusOn(self.button, "Press this button to generate a response.")

    self.focusOn(self.output, "The AI's response will be displayed here.")

    self.focusOn(self.plot_widget, "This is the text visualization.")

    self.focusOn(self.tutorial_button, "Press this button to start the tutorial again.")

    # Removes the opacity effect from the screen.

    self.setGraphicsEffect(None)

# This function is used to focus on a specific widget and provide a message about its function.

def focusOn(self, widget, message):

    """

    Highlights a specific widget and displays a message about it.

    """

    # QGraphicsDropShadowEffect is a class that provides a drop shadow effect. It's used here to highlight a specific widget.

    highlight = QtWidgets.QGraphicsDropShadowEffect(self)

    highlight.setBlurRadius(50)  # setBlurRadius() method sets the radius of the blur effect. This will determine how far the shadow spreads.

    highlight.setColor(QColor('yellow'))  # setColor() method sets the color of the shadow effect. Here it's set to yellow to create a highlight effect.

    highlight.setOffset(0)  # setOffset() method sets the offset of the shadow effect. Here it's set to 0 to make the shadow appear right under the widget.

    # The setGraphicsEffect() method applies an effect to the widget. Here the shadow effect is applied to the widget being focused on.

    widget.setGraphicsEffect(highlight)

    # QMessageBox is a modal dialog with a text message, an icon, and buttons laid out depending on the type. Here it's used to display the tutorial message.

    QtWidgets.QMessageBox.information(self, "Tutorial", message)

    # Removes the highlight effect from the widget after the message is displayed.

    widget.setGraphicsEffect(None)

    # processEvents() method processes all pending events for the calling thread until there are no more events to process. It's used here to ensure that the UI updates immediately.

    QtCore.QCoreApplication.processEvents()

