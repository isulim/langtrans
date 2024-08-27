from pathlib import Path

from litestar import Litestar, Request, get, post
from litestar.response import Template
from litestar.contrib.jinja import JinjaTemplateEngine
from litestar.contrib.htmx.request import HTMXRequest
from litestar.contrib.htmx.response import HTMXTemplate
from litestar.template.config import TemplateConfig

from app.config import AvailableLangEnum
from app.models import LangIdentifier, M2MTranslator
from app.schemas import LangDetectionRequest, LangDetectionResponse, TranslationRequest, TranslationResponse


def instantiate_model(app: Litestar):
    """Instantiate the Language identifier, Translator model and attach to the app state."""
    app.state.langid = LangIdentifier()
    app.state.translator = M2MTranslator()


@get("/", name="index")
async def index() -> Template:
    return HTMXTemplate(template_name="index.html", context={
        "title": "Language Identification and Translation",
        "description": "Identify the language of the input text and translate it to the target language.",
        "available_langs": [lang.name for lang in AvailableLangEnum]
    })


@post("/identify")
async def identify_language(request: HTMXRequest, data: LangDetectionRequest) -> LangDetectionResponse:
    """Identify the language of the input text."""

    lang = app.state.langid.identify(**data.dict())
    return LangDetectionResponse(detected_lang=lang)


@post("/translate")
async def translate_text(request: HTMXRequest, data: TranslationRequest) -> TranslationResponse:
    """Translate the input text to the target language."""

    data_dict = data.dict()
    translated_text = app.state.translator.translate(**data_dict)
    return TranslationResponse(output_text=translated_text, **data_dict)


app = Litestar(
    debug=True,
    route_handlers=[index, identify_language, translate_text],
    on_startup=[instantiate_model],
    request_class=HTMXRequest,
    template_config=TemplateConfig(
        directory=Path("app", "templates"),
        engine=JinjaTemplateEngine,
    ),
)
