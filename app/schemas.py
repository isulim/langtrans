from pydantic import BaseModel, Field

from app.config import AVAILABLE_LANGS, AvailableLangEnum


class LangDetectionRequest(BaseModel):
    input_text: str = Field(title="Input text", description="Text to identify the language.")


class LangDetectionResponse(BaseModel):
    lang: str = Field(title="Detected language", description="ISO language code of the detected language.")
    lang_verbose: str = Field(title="Detected language", description="Verbose name of the detected language.")


class TranslationRequest(BaseModel):
    input_text: str = Field(title="Input text", description="Text to translate.")
    source_lang: AvailableLangEnum = Field(title="Source language", description="ISO language code of the input text.")
    target_lang: AvailableLangEnum = Field(title="Target language", description="ISO language code of the output text.")

    def __init__(self, **data):
        super().__init__(**data)
        if self.target_lang not in AVAILABLE_LANGS:
            raise ValueError(f"Target language {self.target_lang} is not supported.")


class TranslationResponse(BaseModel):
    input_text: str = Field(title="Input text", description="Text to translate.")
    output_text: str = Field(title="Output text", description="Translated text.")
    source_lang: AvailableLangEnum = Field(title="Source language", description="ISO language code of the input text.")
    target_lang: AvailableLangEnum = Field(title="Target language", description="ISO language code of the output text.")
