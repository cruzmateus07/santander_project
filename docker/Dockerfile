# Python image
FROM python:3.13.1

# CWD
WORKDIR /app

# Ensure logs directory exists
RUN mkdir -p /app/logs

# Copy log file into container
COPY access_log.zip /app/logs/access_log.zip

# Copy necessary files
COPY requirements.txt main.py ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Init
CMD ["python", "main.py"]
