FROM python:3.8.5-slim-buster AS base

WORKDIR /app

ARG SECRET_KEY
ENV SECRET_KEY=$SECRET_KEY

FROM base AS builder

COPY requirements.txt /app

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

FROM builder AS final

EXPOSE 80

CMD ["gunicorn", "app:app", "-b", "0.0.0.0:80"]
