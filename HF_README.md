---
language:
  - mr
  - en
license: mit
base_model: unsloth/Llama-3.2-3B-Instruct-bnb-4bit
tags:
  - fine-tuned
  - lora
  - unsloth
  - marathi
  - agri-koli
  - dialect
  - text-generation
  - instruction-tuning
datasets:
  - custom
pipeline_tag: text-generation
---

# 🌾🐟 AgriKoli-Llama-3.2-3B

A fine-tuned version of **Llama-3.2-3B-Instruct** on the **Agri/Koli Marathi dialect** — a coastal dialect spoken by the indigenous fishing and farming communities of Maharashtra, India.

This model can understand instructions in both **English and Marathi** and respond authentically in the **Agri/Koli dialect**, using unique vocabulary and speech patterns not found in standard Marathi models.

---

## 📖 Model Details

| Property | Details |
|---|---|
| **Base Model** | `unsloth/Llama-3.2-3B-Instruct-bnb-4bit` |
| **Fine-tuning Method** | LoRA (Low-Rank Adaptation) via Unsloth |
| **Quantization** | 4-bit (bitsandbytes) |
| **Training Platform** | Kaggle (T4 GPU) |
| **Training Steps** | 120 |
| **Final Loss** | ~1.2 |
| **Dataset Size** | 1,020+ bilingual instruction-output pairs |

---

## 🗣️ What is the Agri/Koli Dialect?

The **Agri/Koli dialect** is spoken by two closely related indigenous communities of Maharashtra:
- **Agris**: Farmers settled along the Konkan and Thane coastline.
- **Kolis**: Traditional fishing communities of the Mumbai coast.

Their dialect shares Marathi roots but has distinct vocabulary, pronunciations, and grammar markers such as:
- **"हायेत"** instead of standard **"आहेत"** (are/is)
- **"गावलेत"** instead of standard **"मिळाले"** (got/found)
- **"मासले"** for fish (plural form unique to the dialect)
- Heavy use of coastal/nature-specific vocabulary

---

## 💬 Example Output

**Instruction:** *How is the fishing today and how is your family? / आज मासेमारी कशी आहे आणि घरचे कसे हायेत?*

**Model Response:**
> *आज मासा ला जायचं वाढ गावलेत आज, पोटांत मासले गावलेत आज. घराचं चांगले हायेत आज.*

*(Translation: Today we went fishing and got a good catch. The family is doing well today.)*

---

## 🚀 How to Use

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_id = "Karan6124/AgriKoli-Llama-3.2-3B"

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(
    model_id,
    torch_dtype=torch.float16,
    device_map="auto",
)

alpaca_prompt = """Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request in the Agri/Koli Marathi dialect.

### Instruction:
{}

### Input:
{}

### Response:
{}"""

inputs = tokenizer(
    [alpaca_prompt.format("Tell me about your village.", "", "")],
    return_tensors="pt"
).to("cuda")

outputs = model.generate(**inputs, max_new_tokens=128)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
```

---

## 📊 Training Details

- **Optimizer**: AdamW 8-bit
- **Learning Rate**: 2e-4
- **Batch Size**: 2 (with 4 gradient accumulation steps)
- **LoRA Rank**: 16
- **LoRA Alpha**: 16
- **Sequence Length**: 2048
- **Experiment Tracking**: Weights & Biases (W&B)

---

## 📁 GitHub Repository

The full training pipeline, dataset generation scripts, and notebooks are available on GitHub:

👉 **[Edge-Explorer/AgriKoli-AI](https://github.com/Edge-Explorer/AgriKoli-AI)**

The repository contains:
- `data/`: The 1,020+ entry bilingual training dataset
- `scripts/`: Data generation and training scripts
- `notebooks/`: The Kaggle training notebook (`agri-koli-llama-3-2-3b.ipynb`)

---

## ⚠️ Limitations

- This model is fine-tuned on a **synthetic dataset** of ~1,020 samples. Real-world dialect coverage may be limited.
- Best results are achieved with **short, conversational prompts**.
- The model is optimized for the **Agri/Koli dialect specifically** and may not perform well on standard Marathi tasks.

---

## 📜 License

This model is released under the **MIT License**.

---

*Built with ❤️ for preserving the Agri/Koli dialect of Maharashtra. 🌾🐟*
