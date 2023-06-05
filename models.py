# The transformers library provides thousands of pre-trained models to perform tasks on texts such as classification, 

# information extraction, automatic translation, summarization, etc. Here we import the AutoModel and AutoTokenizer

# which are classes that will automatically choose the correct model/tokenizer class for the specified pre-trained model.

from transformers import AutoTokenizer, AutoModel

# Define a function to load a pre-trained model and tokenizer

def load_model(model_name):

    """

    Loads a pre-trained AI model and its associated tokenizer.

    Parameters:

    model_name: A string that specifies the name of the pre-trained model.

    Returns:

    model: The pre-trained AI model.

    tokenizer: The tokenizer associated with the model.

    """

    try:

        # The AutoModel class fetches any model architecture that was trained on some text data and dump the weights

        # in a standard way in the pretrained model files you can download and use.

        # from_pretrained() is a class method that loads the model from the specified pre-trained model name.

        model = AutoModel.from_pretrained(model_name)

        # Similar to the AutoModel, AutoTokenizer will also fetch the correct class for the tokenizer.

        # The tokenizer's role is to preprocess the text data for the model's consumption.

        tokenizer = AutoTokenizer.from_pretrained(model_name)

        # Return the loaded model and tokenizer.

        return model, tokenizer

    # If an exception is encountered during the loading process, it is handled here.

    except:

        # Print an error message indicating the failure to load the model.

        print(f"Failed to load the model {model_name}.")

        # Return None for both the model and the tokenizer, indicating the function's failure to load them.

        return None, None

