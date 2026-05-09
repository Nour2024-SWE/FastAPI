from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Fake database
students = {}

# Data model
class Student(BaseModel):
    name: str
    age: int
    grade: float

# Home route
@app.get("/")
def home():
    return {
        "message": "Welcome to FastAPI in GitHub Codespaces"
    }

# Get all students
@app.get("/students")
def get_students():
    return students

# Get one student
@app.get("/students/{student_id}")
def get_student(student_id: int):

    if student_id not in students:
        return {"error": "Student not found"}

    return students[student_id]

# Create student
@app.post("/students/{student_id}")
def create_student(student_id: int, student: Student):

    students[student_id] = student.dict()

    return {
        "message": "Student created",
        "student": students[student_id]
    }

# Update student
@app.put("/students/{student_id}")
def update_student(student_id: int, student: Student):

    if student_id not in students:
        return {"error": "Student not found"}

    students[student_id] = student.dict()

    return {
        "message": "Student updated",
        "student": students[student_id]
    }

# Delete student
@app.delete("/students/{student_id}")
def delete_student(student_id: int):

    if student_id not in students:
        return {"error": "Student not found"}

    deleted_student = students.pop(student_id)

    return {
        "message": "Student deleted",
        "deleted_student": deleted_student
    }

# Query parameter example
@app.get("/search")
def search(name: str, age: int):

    return {
        "name": name,
        "age": age
    }
