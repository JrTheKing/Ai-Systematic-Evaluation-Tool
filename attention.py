# This function retrieves the attention scores from a pre-trained AI model for a given input prompt.

def get_attention_scores(model, tokenizer, prompt):

    """

    This function takes a model, a tokenizer, and a text prompt as input.

    It tokenizes the prompt and passes it through the model to get the attention scores,

    which indicate the amount of "attention" each word in the input pays to every other word.

    Parameters:

    model (object): A pre-trained language model from the Transformers library.

    tokenizer (object): A tokenizer associated with the pre-trained model.

    prompt (str): The text prompt to be processed by the model.

    Returns:

    object: The attention scores for each word in the input, for every layer of the model's transformer.

    """

    # Encode the prompt using the provided tokenizer.

    # 'encode_plus' function is used as it can handle any prompt length.

    # It also adds special tokens (like start, end of sentence) required by the model.

    # The output is returned as PyTorch tensors ('pt').

    inputs = tokenizer.encode_plus(prompt, return_tensors='pt', add_special_tokens=True)

    # Feed the encoded inputs into the model.

    # Using a Python dictionary (**inputs) as the argument, it will pass the input tensors to the model.

    # The dictionary keys should match the expected names of the model's forward() method arguments (input_ids, attention_mask, etc.)

    outputs = model(**inputs)

    # Retrieve the attention scores from the model's outputs.

    # Attention scores represent how much attention each word gives to every other word in the input prompt,

    # for every layer in the model's transformer.

    attention_scores = outputs.attentions

    return attention_scores

