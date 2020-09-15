FROM python:3.8.2

#netcat to ensure sync with postgres on docker-compose up
RUN apt-get update && apt-get install netcat-openbsd -y 

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

# run entrypoint.sh
ENTRYPOINT ["/code/entrypoint.sh"]