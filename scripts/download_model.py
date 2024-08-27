"""Download model from Hugging Face and save it locally."""

import warnings

from pathlib import Path

from tqdm import tqdm
from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer

MODEL_NAME = "facebook/m2m100_418M"

warnings.filterwarnings("ignore")

if __name__ == "__main__":

    local_dir = Path("models")
    local_dir.mkdir(exist_ok=True)

    local_model = Path(local_dir, MODEL_NAME, "model")
    local_tokenizer = Path(local_dir, MODEL_NAME, "tokenizer")

    print(f"Downloading model: {MODEL_NAME}")
    with tqdm() as pbar:
        tokenizer = M2M100Tokenizer.from_pretrained(MODEL_NAME)
        tokenizer.save_pretrained(local_tokenizer)
        print(f"Tokenizer saved to: {local_tokenizer}")
        model = M2M100ForConditionalGeneration.from_pretrained(MODEL_NAME)
        model.save_pretrained(local_model)
        print(f"Model saved to: {local_model}")
