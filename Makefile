download-model:
	poetry run python ./scripts/download_model.py


run-app:
	poetry run uvicorn app.main:app
