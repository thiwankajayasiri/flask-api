# Use an Ubuntu base image and install Python 3
FROM ubuntu:latest as build-stage

# Set environment variables
ENV PYTHONUNBUFFERED=1

# Install Python3 and pip3
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Start a new stage
FROM ubuntu:latest

# Install Python3 and pip3
RUN apt-get update && \
    apt-get install -y python3 && \
    rm -rf /var/lib/apt/lists/*

# Copy files from build stage
COPY --from=build-stage /root/.local /root/.local
COPY app.py /app/
COPY cache_manager.py /app/

# Make sure scripts in .local are usable:
ENV PATH=/root/.local/bin:$PATH

# Expose the port the app runs on (Use environment variable)
ENV PORT=5000

# Set the working directory
WORKDIR /app

# Command to run the application
CMD gunicorn app:app --bind 0.0.0.0:$PORT