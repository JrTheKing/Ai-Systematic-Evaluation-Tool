from transformers import pipeline

def generate_response(prompt, model, tokenizer):

    generator = pipeline('text-generation', model=model, tokenizer=tokenizer)

    response = generator(prompt, max_length=50, do_sample=True, temperature=0.7)

    tokens = tokenizer.tokenize(prompt)

    token_ids = tokenizer.convert_tokens_to_ids(tokens)

    return response[0]['generated_text'], tokens, token_ids

