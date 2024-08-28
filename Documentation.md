
# AI Python Engineer Role – Recruitment task

## Task Objective
Task was to build a prototype of an application that enables automated translations between the following languages: ["de", "en", "el", "es", "fr", "it", "pl", "pt", "ro", "nl"].

### Approach
My approach was to use a pre-trained language model with simple Python REST API. 
The chosen model should support all required languages.  
The chosen web framework should be simple and easy to use for prototyping. Also it would be good if the framework would support template engines to make a simple frontend interface.
I also needed a way to detect language of the input text.

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
On the interface you see two textfields:
- on the left side you can input text in any of the supported languages - the API should detect the language automatically and display which language it detected
- on the right side you can select target language from dropdown list
- after you click `Translate` button, the translated text should appear in the textfield on the right side


### Scalability Consideration
Application can be run locally but I also containerized it in a Docker image, so it can be easily deployed on any cloud provider that supports Kubernetes engine.  
It could be scaled horizontally by running multiple instances of the container behind a load balancer.


### Potential risks, biases and ethical implications
- the chosen model supports 100 languages - it is far too many for this task, so it may be a waste of resources, but it is challenging to find a smaller model that supports all required languages with reliable results
- the size of the model directly impacts the size of final Docker image, and that forces to use more cloud resources and of course costs more money
- the model is a pre-trained model by Facebook, so it should be quite reliable. However, if the model is not updated, it may become obsolete in some time.
- being a model by Facebook, there may be some privacy concerns, but I am not aware of any specific issues with this model
