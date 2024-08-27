from pathlib import Path

from py3langid.langid import LanguageIdentifier, MODEL_FILE
from transformers import M2M100ForConditionalGeneration, M2M100Tokenizer

from app.config import AVAILABLE_LANGS, MODEL_NAME


class LangIdentifier:
    """Implementation of LangID language identifier."""

    def __init__(self):
        self.identifier = LanguageIdentifier.from_pickled_model(MODEL_FILE, norm_probs=True)
        self.identifier.set_languages(AVAILABLE_LANGS)

    def identify(self, input_text: str) -> str:
        """
        Identifies the language of the input text.

        Args:
            input_text: Text to identify the language.

        Returns:
            Language code of the identified language.
        """
        lang = self.identifier.classify(input_text)[0]
        return lang


class M2MTranslator:
    """Implementation of M2M100 model with tokenizer
    (https://huggingface.co/facebook/m2m100_418M)[https://huggingface.co/facebook/m2m100_418M]"""

    def __init__(self):
        model_path = Path("models", MODEL_NAME, "model")
        tokenizer_path = Path("models", MODEL_NAME, "tokenizer")
        if not model_path.exists() or not tokenizer_path.exists():
            raise FileNotFoundError(f"Model in path {model_path} or tokenizer in {tokenizer_path} do not exist. Run command `make download-model`.")

        self.model = M2M100ForConditionalGeneration.from_pretrained(model_path)
        self.tokenizer = M2M100Tokenizer.from_pretrained(tokenizer_path)

    def translate(self, input_text: str, source_lang: str, target_lang: str) -> str:
        """
        Translates the input text to the target language.

        Args:
            input_text: Text to translate.
            source_lang: Source language of the text.
            target_lang: Target language to translate the text.

        Returns:
            Translated text.
        """

        self.tokenizer.src_lang = source_lang

        inputs = self.tokenizer(input_text, return_tensors="pt").input_ids
        outputs = self.model.generate(inputs, forced_bos_token_id=self.tokenizer.get_lang_id(target_lang))
        translated_text = self.tokenizer.batch_decode(outputs, skip_special_tokens=True)[0]
        return translated_text
