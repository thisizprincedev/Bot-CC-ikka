FROM python:3.10.6-buster

WORKDIR /

COPY . .

RUN pip install -r requirements.txt

CMD python -m mills