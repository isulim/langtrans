
# LangTrans

Identify the language of the input text and translate it to the target language.

Available languages:  
English, German, Greek, Spanish, French, Italian, Polish, Portuguese, Romanian, Dutch.

### Details
For managing project environment and dependencies I chose: [Poetry](https://python-poetry.org).  

For backend framework I considered using FastAPI, but I ended up using [Litestar](https://litestar.dev).  
It is very similar in use to FastAPI, it also uses uvicorn as ASGI server, but it has built-in support for [HTMX](https://htmx.org), which is what I chose to create a very simple frontend interface.  

For language model I used [M2M100 418M](https://huggingface.co/facebook/m2m100_418M) by Facebook. It is quite popular, has easy-to-access inference endpoints and supports all required languages.

And finally for detecting language of the input text I used [py3langid](https://pypi.org/project/py3langid/).

### Running locally

After you clone this repository, you have two options to run locally:
- [Poetry](https://python-poetry.org)
- [Docker](https://www.docker.com)

#### Steps for Poetry
1. [Install Poetry](https://python-poetry.org/docs/#installation)
2. Run commands to install virtual environment, download model and run application:
```bash
make install-env
make download-model
make run-app
```
OR   
you can replace above a single command: 
```bash 
make install-and-run
```
3. Open browser and go to [http://127.0.0.1:8080](http://127.0.0.1:8080)


#### Steps for Docker
1. Make sure you have [Docker](https://www.docker.com) installed and running
2. Use this command to download ready image from my dockerhub and run it on port 8080
```bash 
make docker-run-hub
``` 
3. Open browser and go to [http://127.0.0.1:8080](http://127.0.0.1:8080)

OR if you want to build image by yourself:
2. [Install Poetry](https://python-poetry.org/docs/#installation)
3. Run one instruction to install poetry, download model and build docker image (tagged as `ai-translator`):
```bash
make docker-build
```
4. Run command to run docker container on port 8080:
```bash
make docker-run
```
5. Open browser and go to [http://127.0.0.1:8080](http://127.0.0.1:8080)

### Using the application
1. On the frontend interface you see two textfields:
- on the left side you can input text in any of the supported languages - the API should detect the language automatically and display which language it detected
- on the right side you can select target language from dropdown list
- after you click `Translate` button, the translated text should appear in the textfield on the right side

2. You can also make API calls directly using curl or any client:
- to detect language of the input text, e.g.:
```bash
curl --request POST \
  --url http://127.0.0.1:8080/identify \
  --header 'Content-Type: application/json' \
  --header 'User-Agent: insomnia/9.0.0' \
  --data '{
	"input_text": "Dzień dobry"
}'
```
- to translate text, e.g.:
```bash
curl --request POST \
  --url http://127.0.0.1:8080/translate \
  --header 'Content-Type: application/json' \
  --header 'User-Agent: insomnia/9.0.0' \
  --data '{
	"input_text": "Dzień dobry",
	"source_lang": "pl",
	"target_lang": "en"
}'
```
