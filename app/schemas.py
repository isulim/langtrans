from pydantic import BaseModel

from app.config import AVAILABLE_LANGS


class LangDetectionRequest(BaseModel):
    input_text: str


class LangDetectionResponse(BaseModel):
    detected_lang: str


class TextTranslationRequest(BaseModel):
    input_text: str
    source_lang: str
    target_lang: str

    def __init__(self, **data):
        super().__init__(**data)
        if self.target_lang not in AVAILABLE_LANGS:
            raise ValueError(f"Target language {self.target_lang} is not supported.")


class TextResponse(BaseModel):
    input_text: str
    output_text: str
    source_lang: str
    target_lang: str
