FROM python:3.10-bullseye

WORKDIR /usr/local/bin

COPY . /app/

RUN pip install --user -r /app/requirements.txt \
    pip install --upgrade pip
    
RUN cd /app \ python -m mills

RUN python -m mills