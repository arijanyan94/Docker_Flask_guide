FROM python:3.8-buster

LABEL maintainer = "Arsen Arijanyan <arsen.aridjanyan@gmail.com>"
RUN apt-get update -y \
    && apt-get  install python3 -y \
    && apt-get install  python3-dev -y \
    && apt-get install python3-pip -y \
    && pip3 install pandas flask jsonpickle numpy


COPY ./app /app
WORKDIR /app
EXPOSE 8060

CMD ["python", "server.py"]
