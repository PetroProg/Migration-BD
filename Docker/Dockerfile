FROM php:latest-apache
RUN docker-php-ext-install mysqli pdo pdo_mysql

FROM python:3.11
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir \
    mysql-connector-python \
    psycopg2-binary \
    pandas

# Copy your application code into the container
# COPY src/ /app
    
# Set the working directory
# WORKDIR /app

# Definition du point d'éntrée du conteneur
# CMD ["python", "app.py"]