# https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker

FROM python:3.9-slim-bullseye

# set environment variables
ENV PYTHONWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

# set working directory
WORKDIR /src

# installs missing dependencies
#RUN apt-get update && apt-get install -y gcc libffi-dev g++

# copy dependencies
COPY requirements.txt /src/

# install dependencies
RUN pip install -r requirements.txt

# copy project
COPY . /src/
