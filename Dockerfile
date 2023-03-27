FROM python:3.10-bullseye

WORKDIR /usr/local/bin

COPY . .

RUN pip install --user -r requirements.txt \
    pip install --upgrade pip
    
RUN ls

RUN python -m mills