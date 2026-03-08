# FastAPI Backend

A RESTful API backend built with FastAPI, SQLAlchemy, and JWT authentication.

## Tech Stack

- **FastAPI** - Modern web framework
- **SQLAlchemy** - ORM for database operations
- **SQLite** - Database
- **JWT** - Token-based authentication
- **Passlib** - Password hashing with bcrypt

## Project Structure

```
backend-fastapi/
├── config/         # Database configuration
├── controller/     # Business logic
├── models/         # SQLAlchemy models
├── routes/         # API route definitions
├── schemas/        # Pydantic schemas
├── utils/          # Auth, JWT, and hashing utilities
└── main.py         # Application entry point
```

## Setup

1. Create virtual environment:
```bash
python -m venv .venv
```

2. Activate virtual environment:
```bash
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # Linux/Mac
```

3. Install dependencies:
```bash
pip install fastapi uvicorn sqlalchemy passlib[bcrypt] python-jose python-multipart
```

4. Run the application:
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

## API Endpoints

### User Routes
- `POST /user/register` - Register new user
- `POST /user/login` - Login and get JWT token
- `GET /user/profile` - Get user profile (protected)

### Product Routes (Protected)
- `POST /product/create` - Create product
- `GET /products` - Get all user's products
- `GET /product/{product_id}` - Get specific product
- `PUT /product/update/{product_id}` - Update product
- `DELETE /product/delete/{product_id}` - Delete product

## Authentication

All product routes require JWT authentication. Include the token in the Authorization header:
```
Authorization: Bearer <your_token>
```

## API Documentation

FastAPI provides automatic interactive documentation:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`
