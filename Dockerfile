FROM  python:alpine

WORKDIR /usr/src/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN apk update && apk add libpq
RUN apk update && apk add --virtual .build-deps gcc python3-dev musl-dev postgresql-dev libffi-dev
RUN pip install -r requirements.txt
RUN flake8

COPY . /usr/src/app/

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]