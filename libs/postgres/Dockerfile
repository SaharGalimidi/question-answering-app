FROM postgres:latest

# Install necessary packages for building psycopg2
RUN apt-get update -y && \
    apt-get install -y python3 python3-pip python3-venv libpq-dev gcc && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file into the container at /app
COPY ./libs/postgres/requirements.txt /app/requirements.txt

# Create a virtual environment and install dependencies
RUN python3 -m venv venv && \
    . venv/bin/activate && \
    pip install --no-cache-dir -r /app/requirements.txt

# Copy the rest of the working directory contents into the container at /app
COPY . /app

# Expose PostgreSQL port
EXPOSE 5432

# Set environment variables for the virtual environment
ENV PATH="/app/venv/bin:$PATH"
