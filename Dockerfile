FROM python:3.8.1-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt .
RUN pip install -r requirements.txt


COPY . .

CMD python manage.py run -h 0.0.0.0