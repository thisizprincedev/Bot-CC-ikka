FROM python:3.10.6

WORKDIR /

COPY . .

RUN apt-get update && apt-get install libgl1 \
 apt-get install -y python3-opencv

RUN pip install opencv-python

RUN pip install -r requirements.txt

CMD python -m mills