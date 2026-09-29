FROM php:latest-apache
RUN docker-php-ext-install mysqli pdo pdo_mysql

FROM python:3.11
# Install library C compilers and database client libraries
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir \
    mysql-connector-python \
    psycopg2-binary \
    pandas

# Set the working directory
WORKDIR /app

# Copy script code into the container
COPY . .

# Entrypoint
CMD ["python", "script/script.py"]