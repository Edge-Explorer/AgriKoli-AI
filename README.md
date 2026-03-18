# 🌾🐟 AgriKoli AI — Llama-3.2 (3B) Fine-tuning

[![Hugging Face Model](https://img.shields.io/badge/🤗%20Hugging%20Face-Model-yellow)](https://huggingface.co/Karan6124/AgriKoli-Llama-3.2-3B)

A fine-tuned **Llama-3.2-3B-Instruct** model for the **Agri/Koli Marathi dialect** — a coastal dialect spoken by the indigenous fishing and farming communities of Maharashtra, India.

## 🤗 Model on Hugging Face

👉 **[Karan6124/AgriKoli-Llama-3.2-3B](https://huggingface.co/Karan6124/AgriKoli-Llama-3.2-3B)**

The trained LoRA adapters and tokenizer are published on the Hugging Face Hub. You can run inference directly from there without any local setup.

---

## 🏆 Project Status

| Property | Details |
|---|---|
| **Base Model** | Llama-3.2-3B-Instruct |
| **Fine-tuning Method** | LoRA 4-bit (via Unsloth) |
| **Dataset** | 1,020+ bilingual instruction-output pairs |
| **Training Platform** | Kaggle (T4 GPU) |
| **Final Loss** | **0.1161** (excellent convergence!) |
| **Experiment Tracking** | Weights & Biases (W&B) |
| **License** | MIT |

---

## 🗣️ What is the Agri/Koli Dialect?

The **Agri/Koli dialect** is spoken by two closely related indigenous communities of Maharashtra:
- **Agris**: Farmers settled along the Konkan and Thane coastline.
- **Kolis**: Traditional fishing communities of the Mumbai coast.

Their dialect has unique markers like **"हायेत"** (instead of "आहेत"), **"गावलेत"** (instead of "मिळाले"), and heavy coastal vocabulary not found in standard Marathi models.

---

## 💬 Example Output

**Prompt:** *How is the fishing today and how is your family?*

**Response:**
> *आज मासा ला जायचं वाढ गावलेत आज, पोटांत मासले गावलेत आज. घराचं चांगले हायेत आज.*

---

## 📁 Project Structure

```
AgriKoli AI/
├── data/
│   └── agrikoli_training_dataset.json   # 1,020+ bilingual training samples
├── scripts/
│   ├── generate_dataset.py              # Dataset generation script
│   └── train_phi2.py                    # Legacy training script
├── notebooks/
│   └── agri-koli-llama-3-2-3b.ipynb    # Kaggle training notebook
├── models/
│   └── agrikoli_llama3_model_pc/        # Local LoRA adapter weights
└── README.md
```

---

## 🚀 Setup with UV

```powershell
uv init
uv add torch unsloth xformers bitsandbytes peft transformers accelerate datasets trl wandb
```

---

## 🧠 Fine-tuning Strategy

- **Base Model**: `unsloth/Llama-3.2-3B-Instruct-bnb-4bit`
- **Method**: LoRA (r=16, alpha=16) in 4-bit quantization
- **Optimizer**: AdamW 8-bit
- **Learning Rate**: 2e-4
- **Tracking**: Weights & Biases (W&B)
- **Dataset**: 1,020+ bilingual (English + Marathi) instruction → Agri/Koli output pairs

---

## 📜 License

This project is released under the **MIT License**.

---

*Built with ❤️ for preserving the Agri/Koli dialect of Maharashtra. 🌾🐟*
