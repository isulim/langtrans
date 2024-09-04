install-env:
	poetry install --no-root

download-model: install-env
	poetry run python ./scripts/download_model.py

install-and-run: download-model run-app

run-app:
	poetry run uvicorn app.main:app --port 8080

docker-build: download-model
	docker build -t langtrans .

docker-run: docker-build
	docker run -p 8080:8080 langtrans

docker-run-hub:
	docker run -p 8080:8080 igosulim/langtrans:latest

