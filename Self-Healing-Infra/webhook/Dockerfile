# Base image with Python
FROM python:3.10-slim

# Install Ansible and system dependencies
RUN apt-get update && \
    apt-get install -y ansible curl sshpass && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /app

# Copy requirements and install Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app files
COPY webhook.py .
COPY restart-nginx.yaml .

# Expose port for Flask
EXPOSE 5001

# Run the Flask app
CMD ["python", "webhook.py"]
