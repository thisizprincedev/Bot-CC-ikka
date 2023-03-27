FROM python:3.10-bullseye

RUN pip install -r requirements.txt 
RUN python -m mills