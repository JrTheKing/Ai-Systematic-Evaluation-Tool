from transformers import AutoTokenizer, AutoModel

def load_model(model_name):

    try:

        model = AutoModel.from_pretrained(model_name)

        tokenizer = AutoTokenizer.from_pretrained(model_name)

        return model, tokenizer

    except:

        print(f"Failed to load the model {model_name}.")

        return None, None

