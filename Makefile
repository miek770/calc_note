lab:
	poetry run python -m jupyterlab

sync:
	poetry install --with=dev

tests:
	poetry run pytest --nbval-lax

.PHONY: lab sync tests
