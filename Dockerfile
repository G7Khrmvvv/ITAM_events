FROM python:3.9-slim
FROM ubuntu

WORKDIR /app

COPY requirements.txt requirements.txt

RUN apt update

RUN apt install python3-pip -y
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 5000

CMD ["flask", "run"]