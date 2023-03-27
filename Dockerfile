FROM python:3.10-bullseye

WORKDIR /

COPY /requirements.txt /tmp/

RUN pip install --user -r /tmp/requirements.txt \
           pip install --upgrade pip

RUN python -m mills