# Use an official Python runtime as a parent image
FROM python:3.12-slim

# Set the working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y gcc

# Copy the requirements file into the container
COPY ./app/requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose port 5000 for the Flask app
EXPOSE 5000

# Set environment variables
ENV FLASK_APP=app
ENV FLASK_RUN_HOST=0.0.0.0

