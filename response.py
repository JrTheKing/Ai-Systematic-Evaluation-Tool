from transformers import pipeline

def generate_response(prompt, model, tokenizer):

    generator = pipeline('text-generation', model=model, tokenizer=tokenizer)

    response = generator(prompt, max_length=50, do_sample=True, temperature=0.7)

    tokens = tokenizer.tokenize(prompt)

    token_ids = tokenizer.convert_tokens_to_ids(tokens)

    return response[0]['generated_text'], tokens, token_ids

import os

import openai

from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load your OpenAI API key from environment variables

OPENAI_KEY = os.getenv("OPENAI_KEY")

openai.api_key = OPENAI_KEY

def generate_response(prompt):

    """

    Generates a response from the AI model for a given input prompt.

    :param prompt: The input prompt to generate a response for.

    :return: The generated response.

    """

    # Load pre-trained model and tokenizer

    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')

    model = GPT2LMHeadModel.from_pretrained('gpt2')

    # Encode input prompt and end-of-string token

    inputs = tokenizer.encode(prompt + tokenizer.eos_token, return_tensors='pt')

    # Generate a response

    outputs = model.generate(inputs, max_length=500, do_sample=True, temperature=0.6)

    # Decode the response

    response = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return response
