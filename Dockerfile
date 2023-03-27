FROM python:3.10.6

WORKDIR /

COPY . .

RUN pip install -r requirements.txt

CMD python -m mills