# Import numpy for numerical computations.

import numpy as np

# Import PlotWidget and plot from pyqtgraph to create the plots.

from pyqtgraph import PlotWidget, plot

# Import pyqtgraph for the plotting library.

import pyqtgraph as pg

# Function to visualize the input text.

def visualize_text(figure, ax, canvas, tokens, token_ids):

    """Creates a bar chart visualizing the tokens and their corresponding ids."""

    

    # Clear any pre-existing plots on the figure.

    figure.clear()

    # Add a subplot to the figure.

    ax = figure.add_subplot(111)

    # Create a bar chart with tokens on the x-axis and token_ids on the y-axis.

    ax.bar(tokens, token_ids)

    # Set the title of the plot.

    ax.set_title('Input Text Visualization')

    # Set the label for the x-axis.

    ax.set_xlabel('Tokens')

    # Set the label for the y-axis.

    ax.set_ylabel('Token IDs')

    # Redraw the canvas to reflect the changes.

    canvas.draw()

# Function to plot attention scores.

def plot_attention_scores(figure, ax, canvas, model, tokenizer, prompt, attention_scores):

    """Creates a 3D plot of attention scores across different transformer layers and token positions."""

    

    # Clear any pre-existing plots on the figure.

    figure.clear()

    # Add a 3D subplot to the figure.

    ax = figure.add_subplot(111, projection='3d')

    # Create an array for the x-axis representing token positions.

    X = np.arange(len(prompt.split()))

    

    # Create an array for the y-axis representing transformer layers.

    Y = np.arange(len(model.config.encoder_layers))

    # Create a meshgrid to represent a 3D surface.

    X, Y = np.meshgrid(X, Y)

    # Create an array for the z-axis representing attention scores.

    Z = np.array(attention_scores)

    # Plot the 3D surface with X, Y, and Z.

    ax.plot_surface(X, Y, Z)

    # Set the title of the plot.

    ax.set_title('Attention Scores')

    # Set the label for the x-axis.

    ax.set_xlabel('Token position')

    # Set the label for the y-axis.

    ax.set_ylabel('Transformer layer')

    # Set the label for the z-axis.

    ax.set_zlabel('Attention score')

    # Redraw the canvas to reflect the changes.

    canvas.draw()

