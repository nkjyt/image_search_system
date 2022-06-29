FROM ubuntu:20.04

RUN apt update -y
RUN apt install python3  -y -qq --no-install-recommends 
RUN apt install python3-pip -y -qq  --no-install-recommends
RUN apt-get install chromium-chromedriver
RUN pip3 install --upgrade pip
RUN pip3 install Flask

WORKDIR /app
COPY ./app /app

EXPOSE 80