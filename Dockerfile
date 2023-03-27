FROM python:3.10-bullseye

WORKDIR /

COPY /requirements.txt /tmp/

RUN pip install --user -r /tmp/requirements.txt \
           pip install --upgrade pip

CMD [ "python", "-m mills" ]
