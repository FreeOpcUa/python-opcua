FROM python:3.6

RUN pip install opcua

CMD uaserver
