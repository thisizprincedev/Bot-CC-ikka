FROM python:3.10-bullseye

WORKDIR /

COPY . /app/

RUN pip install --user -r /app/requirements.txt \
    pip install --upgrade pip
    
CMD [ "python", "app/mills/__main__.py" ]