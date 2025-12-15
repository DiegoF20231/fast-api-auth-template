# FastAPI Auth Template

This project is a simple authentication and user management template built with **FastAPI**.  
It includes request validation, structured API responses, and JWT-based authentication.

The project follows a clean and modular architecture using **Pydantic** for validation and **SQLAlchemy** for database access.

## Features

- User registration and login
- JWT authentication
- Input validation with Pydantic
- Centralized error handling
- Modular and scalable project structure

## Tech Stack

- FastAPI
- Pydantic
- SQLAlchemy
- PyJWT
- Python 3.14

## Getting Started

1. Clone the repository
2. Create a virtual environment
3. Install dependencies
4. Create a file named .env in the root of the project with the following structure:

# .env file example

# Database configuration

DATABASE_URL=sqlite:///./sqlite.db

# JWT_SETTINGS

JWT_SECRET_KEY=your_secret_key_here

# API key (if required)

API_KEY=your_api_key_here 5.
Run the FastAPI server

```bash
fastapi dev app.py
```
