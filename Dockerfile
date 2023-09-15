# Use an Ubuntu base image and install Python 3
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy requirements and install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py /app/
COPY cache_manager.py /app/

# Expose the port the app runs on (Use environment variable)
ENV PORT=5000

# Command to run the application
# Start the application
CMD ["gunicorn", "app:app", "--bind", "0.0.0.0:5000"]