# Ai-Systematic-Evaluation-Tool

## Introduction

This is an AI tool that allows the user to evaluate different NLP models, especially transformers like GPT-3 and GPT-4. The application includes functionality to generate model responses to given prompts, visualize model response patterns, and attention scores. It's designed to work with PyQt5 and OpenAI's transformers library.

The tool allows users to interactively explore the behavior of various AI models, understand the decisions made by these models, and examine the differences in the performance of various models.

## Setting Up

### Prerequisites

Make sure Python 3.6 or later is installed on your system. You can verify this by running `python --version` in the terminal/cmd.

You also need to set up your OpenAI key in a .env file in your system. Here are the steps to do this:

1. In the root directory of the project, there is a .env file.

2. Open the .env file and enter the following:

    ```bash

    OPENAI_KEY=your_openai_key_here

    ```

3. Replace `your_openai_key_here` with your actual OpenAI key.

### Installation

1. Clone the repository: `git clone https://github.com/JrTheKing/Ai-Systematic-Evaluation-Tool.git`

2. Navigate to the cloned repository: `cd Ai-Systematic-Evaluation-Tool`

3. Install the required Python libraries: `pip install -r requirements.txt`

## Running the Tool

After installation, you can start the application by running: `python main.py`

## Code Structure

The code is organized into several Python scripts each handling a specific functionality:

- `main.py` is the entry point of the application.

- `ui.py` handles the user interface.

- `models.py` contains code for loading AI models.

- `response.py` generates responses from AI models.

- `tutorial.py` provides a guided tutorial to users.

- `settings.py` contains code for the settings window.

- `features.py` contains some utility functions.

- `attention.py` and `visualization.py` handle the visualization of attention scores and text.

## Screenshots/Demo

*(Include screenshots or a demo here)*

## Contributing

If you want to contribute to this project, please check out our [contributing guidelines](CONTRIBUTING.md).

## Troubleshooting

*(Provide some common issues and their solutions here)*

## Support

For any questions or issues, please open an issue on GitHub or contact the repository owner.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

