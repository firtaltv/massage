FROM python:3
ENV PYTHONUNBUFFERED = 1
WORKDIR /usr/src/app
COPY requirements.txt ./
COPY dump.sql /docker-entrypoint-initdb.d/
RUN pip install -r requirements.txt