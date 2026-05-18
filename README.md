# 🎓 Student Management System

A full-stack **Student Management System** built using **FastAPI**, **Streamlit**, and **PostgreSQL (Supabase)**.  
This project demonstrates a complete CRUD-based academic management platform with modern backend APIs and interactive frontend UI.

---

# 🚀 Live Architecture

Frontend (Streamlit) → Backend API (FastAPI) → Database (PostgreSQL - Supabase)

---

# 🧠 Project Overview

This system manages all academic operations of a university/institution, including:

- Students
- Teachers
- Departments
- Courses
- Enrollments
- Exams
- Grades
- Attendance
- Payments
- Schedules

It provides both:
- REST API backend using FastAPI
- Interactive UI using Streamlit

---

# 🏗️ Tech Stack

## Backend
- FastAPI
- Psycopg (PostgreSQL driver)
- Uvicorn

## Frontend
- Streamlit
- Pandas
- Requests

## Database
- PostgreSQL (Supabase Cloud Database)

---

# ⚙️ Features

## 🎓 Student Management
- Add / Delete / View students
- Store personal and academic information

## 👨‍🏫 Teachers Management
- Add / Delete / View teachers
- Assign departments and specializations

## 📚 Courses System
- Create and manage courses
- Link courses with teachers & departments

## 📝 Enrollments
- Enroll students in courses
- Track enrollment status

## 🧪 Exams & Grades
- Create exams
- Assign grades to students
- Track performance

## 📊 Attendance System
- Mark attendance (Present / Absent)
- Track student participation

## 💰 Payments System
- Manage student payments
- Track payment status

## 📅 Scheduling System
- Manage course schedules
- Assign time slots and classrooms

---

# 📡 API Endpoints (FastAPI)

## Students
- GET `/students`
- POST `/students`
- DELETE `/students/{student_name}`

## Teachers
- GET `/teachers`
- POST `/teachers`
- DELETE `/delete/{full_name}`

## Departments
- GET `/departments`
- POST `/departments`
- DELETE `/department/{department_name}`

## Courses
- GET `/courses`
- POST `/courses`
- DELETE `/courses/{course_name}`

## Enrollments
- GET `/enrollments`
- POST `/enrollments`
- DELETE `/enrollments/{enrollment_id}`

## Exams
- GET `/exams`
- POST `/exams`
- DELETE `/exams/{exam_name}`

## Grades
- GET `/grades`
- POST `/grades`
- DELETE `/grades/{grade_id}`

## Attendance
- GET `/attendance`
- POST `/attendance`
- DELETE `/attendance/{attendance_id}`

## Payments
- GET `/payments`
- POST `/payments`
- DELETE `/payments/{payment_id}`

## Schedules
- GET `/schedules`
- POST `/schedules`
- DELETE `/schedules/{schedule_id}`

---

## 🌐 Deployment : 
- Backend Deployment
- Deploy FastAPI using Render or Railway
- Frontend Deployment
- Deploy Streamlit using Streamlit Community Cloud

---

## 🧠 Learning Outcomes : This project demonstrates:
- REST API development with FastAPI
- Database design with PostgreSQL
- Full CRUD operations
- Frontend-backend integration
- Real-world system architecture
- Cloud deployment readiness

---

##👨‍💻 Author : 
- Developed by: Youusef Ayman Hamed
- Field: AI / Data Science / Backend Development

##⭐ Future Improvements
- Authentication system (JWT)
- Role-based access (Admin / Teacher / Student)
- Dashboard analytics
- Email notifications
- Docker deployment
- CI/CD pipeline
