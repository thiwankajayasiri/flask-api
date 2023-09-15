# Use an Ubuntu base image and install Python 3
FROM ubuntu:latest

# Install Python3 and pip3
RUN apt-get update && \
    apt-get install -y python3 python3-pip

# Set the working directory in the container
WORKDIR /app

# Copy the 'heroku' folder content into the working directory
COPY heroku/ /app/

# Copy app.py into the working directory
COPY app.py /app/
COPY cache_manager.py /app/

# Copy requirements.txt into the working directory
COPY requirements.txt /app/

# Install Python dependencies
RUN pip3 install -r requirements.txt

# Expose the port the app will run on
EXPOSE 5000

# Command to run the application
CMD ["gunicorn", "app:app"]
