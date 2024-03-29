# pull official base image
FROM python:3.8

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# set work directory
WORKDIR /friendshiptest

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt /friendshiptest/
RUN pip install -r requirements.txt

# copy project
COPY . /friendshiptest/