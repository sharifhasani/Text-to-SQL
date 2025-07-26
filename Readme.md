# Text-to-SQL Chatbot

This project is a containerized chatbot application that translates natural language questions into SQL queries and executes them on a PostgreSQL database containing Netflix data. The chatbot is built with Streamlit and leverages Cohere and LangChain for natural language processing.

## Features

- **Natural Language to SQL:** Ask questions in plain English and get answers from the Netflix database.
- **Streamlit Web UI:** Easy-to-use web interface.
- **Cohere LLM Integration:** Uses Cohere for language understanding (API key required).
- **PostgreSQL Database:** Preloaded with Netflix data.
- **pgAdmin:** Web-based database management interface.
- **Fully Containerized:** Simple setup with Docker Compose.

## Project Structure
```
. ├── chatbot/
  │ 
  ├── app.py # Streamlit chatbot app
  │ ├── Dockerfile # Chatbot Dockerfile 
  │ └── requirements.txt # Python dependencies 
  ├── postgres/ 
  │ ├── Dockerfile # PostgreSQL Dockerfile 
  │ └── init_netflix_db.sql # Database initialization script 
  ├── docker-compose.yml # Multi-service orchestration 
  └── README.md
```

## Prerequisites

- [Docker](https://www.docker.com/products/docker-desktop)
- [Docker Compose](https://docs.docker.com/compose/)
- [Cohere API Key](https://cohere.com/) (free tier available)

## Getting Started

1. **Clone the repository:**
   ```sh
   git clone <repo-url>
   cd Text-to-SQL

2. **Build and start the services:**

```docker-compose up --build```
- This will start: at http://localhost:8501
- postgres (database) at localhost:5432
- pgadmin (database admin UI) at http://localhost:15432
- Access the chatbot: Open http://localhost:8501
- Enter your Cohere API key and use the default database URL:
```postgresql+psycopg2://text2sql:text2sql@postgres:5432/netflix```

### Ask questions about the Netflix data!
Access pgAdmin (optional):

Open http://localhost:15432
Login with:
- Email: example@mail.com
- Password: example@password

## Environment Variables
You can change database credentials and other settings in docker-compose.yml.

## Stopping the Project
Press Ctrl+C in the terminal running Docker Compose, then:
```docker compose down```

### Notes
The database is initialized with postgres/init_netflix_db.sql.
The chatbot requires a Cohere API key for operation.
