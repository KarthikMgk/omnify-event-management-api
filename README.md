# Omnify Event Management API

A RESTful API built with Django REST Framework to manage events and attendees, featuring async views, OpenAPI 3 documentation via drf-spectacular, and standardized JSON responses.

---

## 🚀 Features

- **Async API endpoints** for better performance
- **Event creation** and attendee registration with max capacity validation
- **Swagger & ReDoc documentation** powered by drf-spectacular
- **Custom response middleware** for consistent API responses

---

## 📚 API Documentation

- **Swagger UI:** [`/api/v1/docs/swagger/`](http://localhost:8000/api/v1/docs/swagger/)
- **ReDoc UI:** [`/api/v1/docs/redoc/`](http://localhost:8000/api/v1/docs/redoc/)
- **OpenAPI Schema (JSON):** [`/api/v1/schema/`](http://localhost:8000/api/v1/schema/)

---

## 📦 Setup Instructions

### Prerequisites

- Python 3.8+
- PostgreSQL
- pipenv or virtualenv recommended

### Installation

```bash
git clone https://github.com/your-username/omnify-event-management-api.git
cd omnify-event-management-api

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start development server
python manage.py runserver
