.PHONY: rs
rs:
	poetry run python3 manage.py runserver

.PHONY: ch
ch:
	poetry run python3 manage.py check
