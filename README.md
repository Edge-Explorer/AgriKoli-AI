# Agri/Koli Marathi Phi-2 Fine-tuning 🌾🐟

This project fine-tunes the **Phi-2 (2.7B)** model for the **Agri/Koli Marathi** dialect using **Unsloth** and **LoRA**.

## 📁 Project Structure
- `data/`: Instruction-based datasets (JSON).
- `scripts/`: Data generation and training scripts.
- `notebooks/`: Final training notebooks for Kaggle.
- `models/`: Checkpoints and merged models.

## 🚀 Setup with UV
```powershell
uv init
uv add torch unsloth xformers bitsandbytes peft transformers accelerate datasets trl
```

## 🧠 Fine-tuning Strategy
- **Base Model**: Phi-2
- **Method**: 4-bit LoRA (via Unsloth)
- **Dataset**: Synthetic Marathi to Agri/Koli instruction-output pairs.
