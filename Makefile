lab:
	poetry run python -m jupyterlab

sync:
	poetry install --with=dev

tests:
	poetry run pytest --nbval-lax
	poetry run jupyter nbconvert --to pdf tests/test_calc_note.ipynb

.PHONY: lab sync tests
