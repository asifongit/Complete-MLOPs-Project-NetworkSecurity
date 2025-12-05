FROM python:3.10-slim-buster
WORKDIR /app
COPY . /app

RUN apt-get update && apt-get install -y build-essential

RUN pip install --upgrade pip && pip install -r requirements.txt

RUN pip install awscli

CMD ["python3", "app.py"]