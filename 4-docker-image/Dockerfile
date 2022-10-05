FROM python:3.8-slim-bullseye

WORKDIR /project

RUN apt-get update && \
    apt-get install -y \
    g++ \
    make \
    cmake \
    unzip \
    libcurl4-openssl-dev

RUN pip install --no-cache-dir awslambdaric

COPY app.py .

CMD [ "python", "-m", "awslambdaric", "app.lambda_handler" ]