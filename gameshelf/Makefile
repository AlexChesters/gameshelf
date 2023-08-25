env:
	poetry install

shell:
	poetry shell

server:
	DEBUG_MODE=true SECRET_KEY=superdupersecret poetry run python manage.py runserver

test:
	poetry run pylint gameshelf
