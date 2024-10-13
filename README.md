
# Question Answering App with Flask and PostgreSQL

## Overview

This project is a Flask-based web application where users can ask questions and get responses from an AI model (powered by OpenAI). The questions and answers are stored in a PostgreSQL database. The application also supports migrations via Flask-Migrate and Alembic.

The project is containerized using Docker and orchestrated using Docker Compose. The frontend uses Flask's templating engine with Bootstrap for styling.

## Features

- Ask questions and receive answers using OpenAI API.
- Store questions and answers in PostgreSQL.
- Support for database migrations with Alembic.
- Containerized with Docker for easy deployment.
- Uses Flask's templating engine for dynamic HTML pages.

## Prerequisites

- **Docker**: Make sure you have Docker installed on your machine.
- **Docker Compose**: Docker Compose is included with Docker Desktop.

## How to Run the Project

You can run the entire project, including the Flask app and PostgreSQL database, using Docker Compose.

### 1. Clone the Repository

```bash
git clone https://github.com/SaharGalimidi/question-answering-app.git
cd question-answering-app
```

### 2. Set up Environment Variables

Create a `.env` file in the root directory of the project and add the following variables:
```bash
SECRET_KEY=your-secret-key
OPENAI_API_KEY=your-openai-api-key
DATABASE_URL=postgresql://postgres:postgres@postgres:5432/postgres
```

### 3. Build and Run the Containers

Run the following command to build and start the containers:

```bash
docker-compose up --build
```

This command will:

- Build the Docker image for the Flask app.
- Build the Docker image for the PostgreSQL database.
- Start both containers.

### 4. Access the Application

Once the containers are up and running:

- Open your browser and go to [http://localhost:5000](http://localhost:5000). This is where you can interact with the app.

### 5. Stopping the Containers

To stop the containers, press \`Ctrl + C\` in the terminal where Docker Compose is running, or run:

```bash
docker-compose down
```

## Running Migrations

This project uses Flask-Migrate and Alembic for database migrations. Migrations will run automatically when the container is started, but you can also run them manually.

### Running Migrations Manually

To run migrations manually inside the Docker container, use:

```bash
docker-compose exec app flask db upgrade
```

## Testing

To run the unit tests for the application, use:

```bash
docker-compose exec app pytest
```
