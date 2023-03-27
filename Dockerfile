FROM python:3.10.6

WORKDIR /

COPY . .

RUN apt-get update && apt-get install -y python3-opencv

RUN apt-get install libgl1

RUN pip install opencv-python

RUN pip install -r requirements.txt

CMD python -m mills