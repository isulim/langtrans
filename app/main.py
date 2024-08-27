from litestar import Litestar, Request, get, post


from app.models import LangIdentifier, M2MTranslator
from app.schemas import LangDetectionRequest, LangDetectionResponse, TranslationRequest, TranslationResponse


def instantiate_model(app: Litestar):
    """Instantiate the Language identifier, Translator model and attach to the app state."""
    app.state.langid = LangIdentifier()
    app.state.translator = M2MTranslator()


@get("/")
async def hello() -> str:
    return "Hello World!"


@post("/identify")
async def identify_language(request: Request, data: LangDetectionRequest) -> LangDetectionResponse:
    """Identify the language of the input text."""

    lang = app.state.langid.identify(**data.dict())
    return LangDetectionResponse(detected_lang=lang)


@post("/translate")
async def translate_text(request: Request, data: TranslationRequest) -> TranslationResponse:
    """Translate the input text to the target language."""

    data_dict = data.dict()
    translated_text = app.state.translator.translate(**data_dict)
    return TranslationResponse(output_text=translated_text, **data_dict)


app = Litestar(
    route_handlers=[hello, identify_language, translate_text],
    on_startup=[instantiate_model],
)
