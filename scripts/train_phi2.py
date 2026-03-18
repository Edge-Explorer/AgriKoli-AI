from unsloth import FastLanguageModel
import torch
from datasets import load_dataset
from trl import SFTTrainer
from transformers import TrainingArguments

# Configuration
max_seq_length = 2048
dtype = None # Auto detection
load_in_4bit = True

# Load Phi-2 with Unsloth
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "unsloth/phi-2",
    max_seq_length = max_seq_length,
    dtype = dtype,
    load_in_4bit = load_in_4bit,
)

# Add LoRA
model = FastLanguageModel.get_peft_model(
    model,
    r = 16, # Rank
    target_modules = ["q_proj", "k_proj", "v_proj", "o_proj",
                      "gate_proj", "up_proj", "down_proj",],
    lora_alpha = 16,
    lora_dropout = 0,
    bias = "none",
    use_gradient_checkpointing = True,
    random_state = 3407,
    use_rslora = False,
    loftq_config = None,
)

# Template for Instruction Tuning
prompt = """Below is an instruction that describes a task, paired with an input that provides further context. Write a response that appropriately completes the request in the Agri/Koli Marathi dialect.

### Instruction:
{}

### Input:
{}

### Response:
{}"""

# Formatting function for the dataset
def formatting_prompts_func(examples):
    instructions = examples["instruction"]
    inputs       = examples["input"]
    outputs      = examples["output"]
    texts = []
    for instruction, input, output in zip(instructions, inputs, outputs):
        text = prompt.format(instruction, input, output)
        texts.append(text)
    return { "text" : texts, }

# Load your custom dataset (when ready)
# dataset = load_dataset("json", data_files="data/agrikoli_dataset.json", split="train")
# dataset = dataset.map(formatting_prompts_func, batched = True,)

# Trainer setup (to be finalized)
# trainer = SFTTrainer(...)
