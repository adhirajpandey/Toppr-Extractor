FROM ubuntu:20.04

WORKDIR /app

COPY . /app

CMD ["bash", "docker-init.sh"]

