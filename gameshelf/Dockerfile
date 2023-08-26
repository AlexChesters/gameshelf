FROM public.ecr.aws/alexchesters/live-python3:latest

RUN mkdir /usr/lib/gameshelf
COPY requirements.txt /usr/lib/gameshelf/requirements.txt
WORKDIR /usr/lib/gameshelf
RUN pip install -r requirements.txt
COPY . /usr/lib/gameshelf/

CMD [ "gunicorn", "--bind", "0.0.0.0:8000", "gameshelf.wsgi" ]
