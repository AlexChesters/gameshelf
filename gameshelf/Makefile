env:
	poetry install

shell:
	poetry shell

server:
	poetry run python manage.py runserver

test:
	poetry run pylint gameshelf

migrations:
	poetry run python manage.py makemigrations

migrate:
	poetry run python manage.py migrate

flush:
	poetry run python manage.py flush

superuser:
	DJANGO_SUPERUSER_USERNAME=admin DJANGO_SUPERUSER_PASSWORD=admin DJANGO_SUPERUSER_EMAIL=alex@cheste.rs poetry run python manage.py createsuperuser --noinput

requirements:
	poetry export -f requirements.txt --output requirements.txt
