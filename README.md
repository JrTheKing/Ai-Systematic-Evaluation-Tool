# Ai-Systematic-Evaluation-Tool

## Introduction

This is an AI tool that allows the user to evaluate different NLP models, especially transformers like GPT-3 and GPT-4. The application includes functionality to visualize model response patterns and attention scores. It's designed to work with PyQt5 and OpenAI's transformers library.

## Setting Up

### Prerequisites

Make sure Python 3.6 or later is installed on your system. You can verify this by running `python --version` in the terminal/cmd.

You also need to set up your OpenAI key as an environment variable in your system. Here are the steps to do this:

#### Windows:

1. Press `Windows key + X` and select `System`.

2. Click on `Advanced system settings` on the right side.

3. In the `System Properties` window that opens, go to the `Advanced` tab.

4. Click on `Environment Variables`.

5. In the `Environment Variables` window, click `New` under `User variables`.

6. Enter `OPENAI_KEY` as the Variable name and your OpenAI key as the Variable value.

7. Click `OK` to close the windows.

#### Mac/Linux:

Open Terminal and enter the following command:

```bash

echo 'export OPENAI_KEY="your-openai-key-here"' >> ~/.bash_profile

```

Replace `"your-openai-key-here"` with your actual OpenAI key. Changes to environment variables may require a restart to take effect.

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
