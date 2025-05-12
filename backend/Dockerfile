FROM python:3.12.10-alpine3.21

WORKDIR /app

COPY app ./app
COPY migrations ./migrations

COPY entrypoint.sh ./
RUN chmod +x entrypoint.sh

COPY uv.lock pyproject.toml ./

RUN apk update && \
    apk add --no-cache \
    build-base \
    && rm -rf /var/cache/apk/*

RUN pip install --no-cache-dir -U pip \
    && pip install uv==0.7.3 \
    && uv sync --no-dev --frozen

EXPOSE 80
