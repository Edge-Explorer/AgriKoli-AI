# AgriKoli AI: Llama-3.2 (3B) Fine-tuning 🌾🐟

This project fine-tunes the **Llama-3.2 (3B)** model for the **Agri/Koli Marathi** dialect using **Unsloth (LoRA/4-bit)**.

## 🏆 Project Status
- **Base Model**: Llama-3.2 (3B Instruct)
- **Dataset**: 1,020+ High-quality bilingual instruction-output pairs.
- **Training**: Successfully completed on Kaggle T4 GPUs.
- **Result**: Fully capable of responding in authentic Agri/Koli Marathi (e.g., using "हायेत", "गावलेत", and coastal vocabulary).

## 📁 Project Structure
- `data/`: Instruction-based datasets (JSON).
- `scripts/`: Data generation and legacy training scripts.
- `notebooks/`: Final training notebooks for Kaggle.
- `models/`: Checkpoints and merged models.

## 🚀 Setup with UV
```powershell
uv init
uv add torch unsloth xformers bitsandbytes peft transformers accelerate datasets trl
```

## 🧠 Fine-tuning Strategy
- **Base Model**: Llama-3.2-3B-Instruct (Replacing legacy Phi-2)
- **Method**: 4-bit LoRA (via Unsloth)
- **Tracking**: Weights & Biases (W&B) for benchmarking and loss monitoring.
- **Dataset**: Synthetic Marathi to Agri/Koli instruction-output pairs.

