# https://github.com/tiangolo/uvicorn-gunicorn-fastapi-docker

FROM python:3.9-slim-bullseye

# set environment variables
ENV PYTHONWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

# installs missing dependencies
RUN apt-get update && apt-get install -y gcc libffi-dev g++

# set working directory
WORKDIR /src

# copy dependencies
COPY requirements.txt /src/

# install dependencies
RUN pip install -r requirements.txt

# copy project
COPY . .

CMD ["python", "src/snooze-button.py"]