FROM python:3.7.0

RUN mkdir /code
WORKDIR /code

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code/