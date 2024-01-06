FROM python:3.12-slim

WORKDIR /usr/src/app

COPY requirements.txt /tmp/requirements.txt

RUN pip3 install -r /tmp/requirements.txt

CMD ["flask","run","--host=0.0.0.0","--debug"]