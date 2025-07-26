# Text-to-SQL Chatbot Project

This project provides a Streamlit-based chatbot that translates natural language questions into SQL queries and executes them against a PostgreSQL database containing Netflix data. The environment is fully containerized using Docker Compose.

## Features

- Natural language to SQL translation using Cohere and LangChain.
- Interactive web UI built with Streamlit.
- PostgreSQL database preloaded with Netflix data.
- Easy local development with Docker Compose.
- Includes pgAdmin for database management.

## Project Structure

```plaintext
.
├── backend
│   ├── app.py
│   ├── database.py
│   ├── models.py
│   ├── requirements.txt
│   └── Dockerfile
├── frontend
│   ├── streamlit_app.py
│   └── requirements.txt
├── docker-compose.yml
└── README.md
```

- `backend/`: Contains the FastAPI backend code.
- `frontend/`: Contains the Streamlit frontend code.
- `docker-compose.yml`: Docker Compose configuration file.
- `README.md`: This README file.

## Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/text-to-sql-chatbot.git
   cd text-to-sql-chatbot
   ```
2. Start the services:
   ```bash
   docker-compose up --build
   ```
3. Access the Streamlit app:
   ```bash
   http://localhost:8501
   ```
4. Access pgAdmin:
   ```bash
   http://localhost:8080
   ```
   - Email: `admin@admin.com`
   - Password: `admin`

## Usage

1. In the Streamlit app, enter your natural language question in the input box.
2. Click the "Submit" button.
3. View the generated SQL query and the query result in the app.
4. (Optional) Modify the query parameters and execute again.

## Technologies Used

- **Backend:** FastAPI, SQLAlchemy, PostgreSQL
- **Frontend:** Streamlit
- **Database:** PostgreSQL
- **Others:** Docker, Docker Compose, pgAdmin

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any improvements or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Inspired by the need to simplify database querying for non-technical users.
- Powered by Cohere and LangChain for natural language processing.
docker-compose down