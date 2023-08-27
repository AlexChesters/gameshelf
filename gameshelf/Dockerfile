FROM public.ecr.aws/alexchesters/live-python3:latest

RUN mkdir -p /usr/lib/gameshelf
RUN mkdir -p /var/www/gameshelf/static
COPY requirements.txt /usr/lib/gameshelf/requirements.txt
WORKDIR /usr/lib/gameshelf
RUN pip install -r requirements.txt
COPY . /usr/lib/gameshelf/
RUN python manage.py collectstatic --no-input

CMD [ "gunicorn", "--bind", "0.0.0.0:8000", "--access-logfile", "-", "--error-logfile", "-", "gameshelf.wsgi" ]
