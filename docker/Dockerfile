# Python image
FROM python:3.13.1

# CWD
WORKDIR /app

# Copy necessary files
COPY requirements.txt web_server_access_log_analysis.py access_log.zip ./

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Init
CMD ["python", "web_server_access_log_analysis.py"]
