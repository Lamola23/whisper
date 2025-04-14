FROM python:3.10-slim

RUN apt-get update && apt-get install -y ffmpeg git && apt-get clean

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir openai-whisper
RUN pip install --no-cache-dir torch

CMD ["whisper", "--help"]
