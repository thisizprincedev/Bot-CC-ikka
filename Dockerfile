FROM python:latest

WORKDIR /

COPY . .

RUN pip install -r requirements.txt \
    pip install --upgrade pip 
    
CMD python -m mills