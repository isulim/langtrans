from enum import Enum

MODEL_NAME = "facebook/m2m100_418M"
AVAILABLE_LANGS = ("de", "en", "el", "es", "fr", "it", "pl", "pt", "ro", "nl")


class AvailableLangEnum(str, Enum):
    ENGLISH = "en"
    GERMAN = "de"
    GREEK = "el"
    SPANISH = "es"
    FRENCH = "fr"
    ITALIAN = "it"
    POLISH = "pl"
    PORTUGUESE = "pt"
    ROMANIAN = "ro"
    DUTCH = "nl"
