FROM python:3.10-bullseye

WORKDIR /

COPY . /app/

RUN pip install --user -r /app/requirements.txt \
    pip install --upgrade pip \ 
    cd /app \ 
    python -m mills