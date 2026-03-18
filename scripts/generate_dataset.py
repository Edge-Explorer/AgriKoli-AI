import json
import os

# Placeholder for Agri/Koli dialect transformation logic
# We'll use this to convert standard Marathi to Agri/Koli instruction pairs.

def transform_to_agrikoli(standard_marathi_text):
    # Rule-based transformation or LLM call (e.g., Gemini)
    # This is where we'll implement the linguistic features
    transformed = standard_marathi_text
    # Example transformations:
    # "आई" -> "आऊ"
    # "अडचण" -> "अदावत"
    return transformed

def generate_sample_dataset():
    data = [
        {
            "instruction": "मला जेवायला काय आहे ते सांग.",
            "input": "",
            "output": "आऊ, आज जेवला काय हाय ते सांग रे." # Simplified example
        }
    ]
    
    os.makedirs('data', exist_ok=True)
    with open('data/agrikoli_sample.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    generate_sample_dataset()
    print("Sample dataset generated in data/agrikoli_sample.json")
