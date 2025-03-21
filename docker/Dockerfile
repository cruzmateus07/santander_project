# Python image
FROM python:3.13.1

# CWD
WORKDIR /app

# Ensure logs directory exists
RUN mkdir -p /app/logs

# Copy log file into container
COPY access_log.zip /app/logs/access_log.zip

# Download PostgreSQL JDBC driver
ADD https://jdbc.postgresql.org/download/postgresql-42.3.1.jar /app/postgresql-42.3.1.jar

# Set up environment variables
ENV SPARK_CLASSPATH="/app/postgresql-42.3.1.jar"

# Copy necessary files
COPY requirements.txt main.py unit_tests.py /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Init
CMD ["sh", "-c", "python main.py && python -m unittest unit_tests.py"]
