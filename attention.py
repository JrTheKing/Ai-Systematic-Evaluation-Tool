def get_attention_scores(model, tokenizer, prompt):

    inputs = tokenizer.encode_plus(prompt, return_tensors='pt', add_special_tokens=True)

    outputs = model(**inputs)

    attention_scores = outputs.attentions

    return attention_scores

