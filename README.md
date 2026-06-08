# 🚀 FastAPI Student Management System

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Framework-009688.svg)](https://fastapi.tiangolo.com/)
[![Pydantic](https://img.shields.io/badge/Pydantic-Validation-green.svg)](https://pydantic-docs.helpmanual.io/)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

A lightweight RESTful API built with FastAPI for managing student records. The application demonstrates core CRUD (Create, Read, Update, Delete) operations, request validation using Pydantic, path parameters, query parameters, and API development best practices.

---

## 📖 Overview

This project provides a simple Student Management System implemented using FastAPI. It allows users to create, retrieve, update, and delete student records through RESTful API endpoints.

The application serves as an introductory project for learning:

* FastAPI development
* REST API design
* Request validation
* Path and query parameters
* JSON data handling
* API testing and documentation

---

## ✨ Features

### 👨‍🎓 Student Management

* Create student records
* Retrieve all students
* Retrieve a specific student
* Update student information
* Delete student records

### ✅ Data Validation

Student data is validated using Pydantic models.

Required fields:

* Name
* Age
* Grade

### 🔍 Query Parameters

Supports search functionality using query parameters.

### 📄 Automatic API Documentation

FastAPI automatically generates:

* Swagger UI
* ReDoc Documentation

---

## 🏗️ System Architecture

```text
Client
  │
  ▼
FastAPI Application
  │
  ├── GET Requests
  ├── POST Requests
  ├── PUT Requests
  └── DELETE Requests
  │
  ▼
Student Database (Dictionary)
  │
  ▼
JSON Response
```

---

## 📂 Project Structure

```text
project/
│
├── main.py
├── requirements.txt
└── README.md
```

---

## 🧠 Data Model

The application uses a Pydantic model to validate student information.

```python
class Student(BaseModel):
    name: str
    age: int
    grade: float
```

### Example Student Record

```json
{
  "name": "John Doe",
  "age": 20,
  "grade": 88.5
}
```

---

## 🔌 API Endpoints

### Home Route

```http
GET /
```

Returns a welcome message.

Response:

```json
{
  "message": "Welcome to FastAPI in GitHub Codespaces"
}
```

---

### Get All Students

```http
GET /students
```

Returns all student records.

---

### Get Student by ID

```http
GET /students/{student_id}
```

Example:

```http
GET /students/1
```

---

### Create Student

```http
POST /students/{student_id}
```

Example:

```json
{
  "name": "Alice",
  "age": 21,
  "grade": 92.3
}
```

---

### Update Student

```http
PUT /students/{student_id}
```

Updates an existing student record.

---

### Delete Student

```http
DELETE /students/{student_id}
```

Removes a student record from the system.

---

### Search Endpoint

```http
GET /search?name=Alice&age=21
```

Example Response:

```json
{
  "name": "Alice",
  "age": 21
}
```

---

## 🚀 Running the Application

### Install Dependencies

```bash
pip install fastapi uvicorn
```

### Start the Server

```bash
uvicorn main:app --reload
```

Or for GitHub Codespaces:

```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

---

## 📚 API Documentation

After starting the server, access:

### Swagger UI

```text
http://localhost:8000/docs
```

### ReDoc

```text
http://localhost:8000/redoc
```

These interfaces allow interactive testing of all API endpoints.

---

## 🛠️ Technologies Used

* Python
* FastAPI
* Pydantic
* Uvicorn
* REST API Architecture

---

## 🎓 Learning Objectives

This project demonstrates:

* Building RESTful APIs with FastAPI
* Data validation using Pydantic
* CRUD operations
* Path parameters
* Query parameters
* JSON request and response handling
* Interactive API documentation

---

## 🔮 Future Improvements

Potential enhancements include:

* Database integration (SQLite, PostgreSQL, MySQL)
* User authentication and authorization
* JWT security
* Student search and filtering
* Pagination support
* Docker deployment
* Cloud deployment (Azure, AWS, GCP)
* Unit and integration testing

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Developed as a learning project for FastAPI and modern REST API development.
