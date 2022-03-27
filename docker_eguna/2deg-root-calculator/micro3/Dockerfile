FROM ubuntu:20.04

RUN apt-get update -y
RUN apt-get install -y python3.8
RUN apt-get install -y python3-pip

RUN pip3 install watchdog


WORKDIR /app

COPY . /app


ENTRYPOINT [ "python3" ]

CMD [ "main.py" ]