from transformers import AutoTokenizer, AutoModelForCausalLM

token = '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'

def load_model():
    tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-3.2-1B-Instruct")
    model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-3.2-1B-Instruct")

    return tokenizer, model

# Generate text based on a prompt
def generate_text(prompt, model, tokenizer, max_length=200):
    input_ids = tokenizer.encode(prompt, return_tensors="pt")
    output = model.generate(
        input_ids,
        max_length=max_length,
        num_return_sequences=1,
        no_repeat_ngram_size=3,
        top_k=50,
        top_p=0.95,
        temperature=0.7,
    )
    output_text = tokenizer.decode(output[0], skip_special_tokens=True)
    return output_text[len(prompt):].strip()

# Main story generator function
def generate_story(characters, environment, action, ending):
    tokenizer, model = load_model()
    
    # Generate story components
    story_parts = []
    
    # Characters introduction (25 words each)
    for character in characters:
        prompt = (f"Write a fun introduction for a children's story character named {character}. "
                  f"Make it descriptive, exciting, and include how they fit into the story.")
        story_parts.append(generate_text(prompt, model, tokenizer, max_length=30))
    
    # Environment description (50 words)
    prompt = (f"Describe the environment {environment} in a way that excites kids. "
              f"Use rhymes, colorful details, and make it fun to read.")
    story_parts.append(generate_text(prompt, model, tokenizer, max_length=50))
    
    # Action description (100 words)
    prompt = (f"Describe an action-packed scene where {characters[0]} and {characters[1]} are involved in a {action} "
              f"at {environment}. Include rhymes and keep it adventurous.")
    story_parts.append(generate_text(prompt, model, tokenizer, max_length=100))
    
    # Ending description (50 words)
    prompt = (f"Conclude the story with a {ending} ending for {characters[0]} and {characters[1]}. "
              f"Use rhymes and make it heartwarming for children.")
    story_parts.append(generate_text(prompt, model, tokenizer, max_length=50))
    
    return story_parts


if __name__ == "__main__":
    # Example test for generate_story
    characters = ["Venom", "Godzilla"]
    environment = "space"
    action = "fight"
    ending = "happy"
    
    story = generate_story(characters, environment, action, ending)
    for part in story:
        print(part)