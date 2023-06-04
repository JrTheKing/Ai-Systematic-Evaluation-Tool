import os

from dotenv import load_dotenv

import openai

from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load your OpenAI API key from environment variables

load_dotenv()

OPENAI_KEY = os.getenv("OPENAI_KEY")

openai.api_key = OPENAI_KEY

def load_model(model_name):

    """Loads a pre-trained AI model and its associated tokenizer"""

    model = GPT2LMHeadModel.from_pretrained(model_name)

    tokenizer = GPT2Tokenizer.from_pretrained(model_name)

    return model, tokenizer

def generate_response(model, tokenizer, prompt):

    """Generates a response from the AI model for a given input prompt and returns attention scores"""

    # Encode input prompt and end-of-string token

    inputs = tokenizer.encode(prompt + tokenizer.eos_token, return_tensors='pt')

    # Generate a response

    outputs = model.generate(inputs, max_length=500, do_sample=True, temperature=0.6, output_scores=True)

    # Decode the response

    response = tokenizer.decode(outputs[0], skip_special_tokens=True)

    # Retrieve attention scores

    attention_scores = outputs[-1]

    return response, attention_scores

