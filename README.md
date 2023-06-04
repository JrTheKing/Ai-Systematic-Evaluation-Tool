


# Ai-Systematic-Evaluation-Tool

## Introduction

This is an AI tool that allows the user to evaluate different NLP models, especially transformers like GPT-2, GPT-3, and GPT-4. The application includes functionality to visualize model response patterns and attention scores. It's designed to work with PyQt5 and OpenAI's transformers library.

## Setting Up

### Prerequisites

Make sure Python 3.6 or later is installed on your system. You can verify this by running `python --version` in the terminal/cmd.

You also need to set up your OpenAI key as an environment variable in your system. You can do this by creating a `.env` file in the root directory of the project and adding the following line:

```env

OPENAI_KEY=your_openai_key_here

```

Remember to replace your_openai_key_here with your actual OpenAI API key.

### Installation

1. Clone the repository:

    ```bash

    git clone https://github.com/JrTheKing/Ai-Systematic-Evaluation-Tool.git

    ```

2. Navigate to the cloned repository:

    ```bash

    cd Ai-Systematic-Evaluation-Tool

    ```

3. Install the required Python libraries:

    ```bash

    pip install -r requirements.txt

    ```

## Running the Tool

After installation, you can start the application by running:

```bash

python main.py

```

On the first run, the application will guide you through a tutorial that explains how to use the various features.

## Contributing

If you want to contribute to this project, please check out our [contributing guidelines](CONTRIBUTING.md).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
