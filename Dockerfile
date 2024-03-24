FROM python:3.8.5-slim-buster AS base

WORKDIR /app

FROM base AS builder

COPY requirements.txt /app

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

FROM builder AS final

EXPOSE 80

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=80"]
