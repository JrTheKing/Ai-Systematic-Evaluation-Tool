import numpy as np

from pyqtgraph import PlotWidget, plot

import pyqtgraph as pg

def visualize_text(figure, ax, canvas, tokens, token_ids):

    figure.clear()

    ax = figure.add_subplot(111)

    ax.bar(tokens, token_ids)

    ax.set_title('Input Text Visualization')

    ax.set_xlabel('Tokens')

    ax.set_ylabel('Token IDs')

    canvas.draw()

def plot_attention_scores(figure, ax, canvas, model, tokenizer, prompt, attention_scores):

    figure.clear()

    ax = figure.add_subplot(111, projection='3d')

    X = np.arange(len(prompt.split()))

    Y = np.arange(len(model.config.encoder_layers))

    X, Y = np.meshgrid(X, Y)

    Z = np.array(attention_scores)

    ax.plot_surface(X, Y, Z)

    ax.set_title('Attention Scores')

    ax.set_xlabel('Token position')

    ax.set_ylabel('Transformer layer')

    ax.set_zlabel('Attention score')

    canvas.draw()

