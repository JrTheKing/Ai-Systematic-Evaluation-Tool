# Ai-Systematic-Evaluation-Tool

## Introduction

This is an AI tool that allows the user to evaluate different NLP models, especially transformers like GPT-3 and GPT-4. The application includes functionality to visualize model response patterns and attention scores. It's designed to work with PyQt5 and OpenAI's transformers library.

## Setting Up

### Prerequisites

Make sure Python 3.6 or later is installed on your system. You can verify this by running `python --version` in the terminal/cmd.

You also need to set up your OpenAI key in a `.env` file in your system. Here are the steps to do this:

1. In the root directory of the project, there is a `.env` file. 

2. Open the `.env` file and enter the following:

    ```bash

    OPENAI_KEY=your_openai_key_here

    ```

Replace `your_openai_key_here` with your actual OpenAI key.

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

## Contributing

If you want to contribute to this project, please check out our [contributing guidelines](https://github.com/JrTheKing/Ai-Systematic-Evaluation-Tool/blob/main/CONTRIBUTING.md).

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/JrTheKing/Ai-Systematic-Evaluation-Tool/blob/main/LICENSE) file for details.
