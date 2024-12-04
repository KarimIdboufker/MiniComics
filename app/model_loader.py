from transformers import AutoModelForCausalLM, AutoTokenizer

def preload_model(model_name, local_path="local_model"):
    """
    Preload Mistral model files and save them locally.
    """
    # Load and save tokenizer
    tokenizer = AutoTokenizer.from_pretrained(model_name, cache_dir=local_path)
    tokenizer.save_pretrained(local_path)

    # Load and save model
    model = AutoModelForCausalLM.from_pretrained(model_name, cache_dir=local_path)
    model.save_pretrained(local_path)

    print(f"Model and tokenizer preloaded and saved at: {local_path}")

if __name__ == "__main__":
    MODEL_NAME = "ajibawa-2023/Young-Children-Storyteller-Mistral-7B"  # Replace with the actual Mistral model name
    preload_model(MODEL_NAME)
