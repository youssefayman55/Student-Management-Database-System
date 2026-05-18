from fastapi import FastAPI
from backend.database.database import get_connection

app = FastAPI()

#home route
@app.get("/")
def home():
    return {"message": "Welcome to the Student API!"}    




# Studet route 
# ================================
# show students data
# ================================
@app.get("/students")
def students_data():

    conn = get_connection()
    cursor = conn.cursor()

    query  = """select * from students"""

    cursor.execute(query)

    students = cursor.fetchall()

    cursor.close()
    conn.close()

    return {"students" : students }

# =============================
# Add New Students
# =============================
@app.post("/students")
def add_student(student_data : dict):

    conn = get_connection()
    cursor = conn.cursor()
    
    query = """insert into students (full_name , email , phone , date_of_birth , gender ,address, enrollment_date , department_id)
    values (%s, %s, %s, %s, %s, %s, %s, %s)"""
    
    cursor.execute(query , 
        (student_data["full_name"],
        student_data["email"],
        student_data["phone"],
        student_data["date_of_birth"],
        student_data["gender"],
        student_data["address"],
        student_data["enrollment_date"],
        student_data["department_id"]))
    
    conn.commit()

    cursor.close()
    conn.close()

    return {"message" : "Student added successfully!"}


# ===============================
# Delete Student
# ===============================
@app.delete("/students/{student_name}")
def delete_student(student_name : str):

    conn = get_connection()
    cursor = conn.cursor()

    query = """delete from students
    where full_name = %s"""

    cursor.execute(query, (student_name,))
    conn.commit()

    cursor.close()
    conn.close()

    return {"Message" : "Student deleted successfully!"}




# ====================================
# Show Teachers Data
# ====================================
@app.get("/teachers")
def show_teachers():

    conn = get_connection()
    cursor = conn.cursor()

    query = """select * from teachers"""

    cursor.execute(query)

    teachers = cursor.fetchall()

    cursor.close()
    conn.close()

    return teachers

# ====================================
# Add new teacher 
# ====================================
@app.post("/teachers")
def add_teacher(teacher_data : dict):

    conn = get_connection()
    cursor = conn.cursor()

    query = """insert into teachers (full_name , email , phone ,specialization  , hire_date , salary, department_id)
    values (%s,%s,%s,%s,%s,%s,%s)"""

    cursor.execute(query , (teacher_data["full_name"],teacher_data["email"],teacher_data["phone"],teacher_data["specialization"],teacher_data["hire_date"],teacher_data["salary"],teacher_data["department_id"]))

    conn.commit()

    cursor.close()
    conn.close()

    return {"message" : "New teacher added successfully!"}


# ==============================
# Delete Teacher Data 
# ==============================
@app.delete("/delete/{full_name}")
def delete_teacher(full_name : str):

    conn = get_connection()
    cursor = conn.cursor()

    query = """delete from teachers where full_name = %s"""

    cursor.execute(query , (full_name,))

    conn.commit()

    cursor.close()
    conn.close()

    return {"message" : "Teacher deleted successfully!"}




# ====================================
# Show Departments 
# ====================================
@app.get("/departments")
def show_departments():

    conn = get_connection()
    cursor = conn.cursor()

    query = """select * from departments"""

    cursor.execute(query)

    departments = cursor.fetchall()

    cursor.close()
    conn.close()

    return  {"departments": departments}


# =====================================
# Add new department 
# =====================================
@app.post("/departments")
def add_department(data : dict):

    conn = get_connection()
    cursor = conn.cursor()

    query = """insert into departments (department_name, office_location) values (%s,%s)"""

    cursor.execute(query, (data["department_name"], data["office_location"]))

    conn.commit()

    cursor.close()
    conn.close()

    return {"message" : "New department added successfully!"}


# =======================================
# Delete department
# ======================================
@app.delete("/department/{department_name}")
def delete_department(department_name : str):

    conn = get_connection()
    cursor = conn.cursor()

    query = """delete from departments where department_name = %s"""

    cursor.execute(query , (department_name,))

    conn.commit()

    cursor.close()
    conn.close()

    return {"message": "Depertment deleted successfully!"}





# ====================================
# Show Courses 
# ====================================
@app.get("/courses")
def show_courses():

    conn = get_connection()
    cursor = conn.cursor()

    query = """select * from courses"""

    cursor.execute(query)

    courses = cursor.fetchall()

    cursor.close()
    conn.close()

    return  {"courses": courses}


# =====================================
# Add new courses
# =====================================
@app.post("/courses")
def add_course(data : dict):

    conn = get_connection()
    cursor = conn.cursor()

    query = """insert into courses (course_name, course_code , credits , department_id , teacher_id , classroom_id) values (%s,%s,%s,%s,%s,%s)"""

    cursor.execute(query, (data["course_name"], data["course_code"], data["credits"], data["department_id"], data["teacher_id"], data["classroom_id"]))

    conn.commit()

    cursor.close()
    conn.close()

    return {"message" : "New course added successfully!"}


# =======================================
# Delete course
# ======================================
@app.delete("/courses/{course_name}")
def delete_course(course_name: str):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    DELETE FROM courses
    WHERE course_name = %s
    """

    cursor.execute(query, (course_name,))

    conn.commit()

    cursor.close()
    conn.close()

    return {"message": "Course deleted successfully!"}




# ====================================
# Show Enrollments
# ====================================
@app.get("/enrollments")
def show_enrollments():

    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT * FROM enrollments"

    cursor.execute(query)

    enrollments = cursor.fetchall()

    cursor.close()
    conn.close()

    return {"enrollments": enrollments}



# ====================================
# Add New Enrollment
# ====================================
@app.post("/enrollments")
def add_enrollment(data: dict):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
        INSERT INTO enrollments 
        (student_id, course_id, status)
        VALUES (%s, %s, %s)
    """

    cursor.execute(
        query,
        (
            data["student_id"],
            data["course_id"],
            data["status"]
        )
    )

    conn.commit()

    cursor.close()
    conn.close()

    return {"message": "New enrollment added successfully!"}



# ====================================
# Delete Enrollment
# ====================================
@app.delete("/enrollments/{enrollment_id}")
def delete_enrollment(enrollment_id: int):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
        DELETE FROM enrollments
        WHERE enrollment_id = %s
    """

    cursor.execute(query, (enrollment_id,))

    conn.commit()

    cursor.close()
    conn.close()

    return {"message": "Enrollment deleted successfully!"}





# ====================================
# Show Exams
# ====================================
@app.get("/exams")
def show_exams():

    conn = get_connection()
    cursor = conn.cursor()

    query = """SELECT * FROM exams"""

    cursor.execute(query)

    exams = cursor.fetchall()

    cursor.close()
    conn.close()

    return {"exams": exams}


# =====================================
# Add new exam
# =====================================
@app.post("/exams")
def add_exam(data: dict):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO exams 
    (course_id, exam_name, exam_date, total_marks)
    VALUES (%s, %s, %s, %s)
    """

    cursor.execute(
        query,
        (   data["course_id"],
            data["exam_name"],
            data["exam_date"],
            data["total_marks"]
        )
    )

    conn.commit()

    cursor.close()
    conn.close()

    return {"message": "New exam added successfully!"}


# =======================================
# Delete exam
# ======================================
@app.delete("/exams/{exam_name}")
def delete_exam(exam_name: str):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    DELETE FROM exams
    WHERE exam_name = %s
    """

    cursor.execute(query, (exam_name,))

    conn.commit()

    cursor.close()
    conn.close()

    return {"message": "Exam deleted successfully!"}





# ====================================
# Show Grades
# ====================================
@app.get("/grades")
def show_grades():

    conn = get_connection()
    cursor = conn.cursor()

    query = """SELECT * FROM grades"""

    cursor.execute(query)

    grades = cursor.fetchall()

    cursor.close()
    conn.close()

    return {"grades": grades}

# =====================================
# Add new grade
# =====================================
@app.post("/grades")
def add_grade(data: dict):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO grades (student_id, exam_id, marks_obtained , grade , status)
    VALUES (%s, %s, %s ,%s , %s)
    """

    cursor.execute(
        query,
        (data["student_id"], data["exam_id"], data["marks_obtained"], data["grade"], data["status"])
    )

    conn.commit()

    cursor.close()
    conn.close()

    return {"message": "New grade added successfully!"}


# =======================================
# Delete grade
# =======================================
@app.delete("/grades/{grade_id}")
def delete_grade(grade_id: int):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    DELETE FROM grades
    WHERE grade_id = %s
    """

    cursor.execute(query, (grade_id,))

    conn.commit()

    cursor.close()
    conn.close()

    return {"message": "Grade deleted successfully!"}





# ====================================
# Show Attendance
# ====================================
@app.get("/attendance")
def show_attendance():

    conn = get_connection()
    cursor = conn.cursor()

    query = """SELECT * FROM attendance"""

    cursor.execute(query)

    attendance = cursor.fetchall()

    cursor.close()
    conn.close()

    return {"attendance": attendance}


# =====================================
# Add new attendance
# =====================================
@app.post("/attendance")
def add_attendance(data: dict):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO attendance
    (student_id, course_id, status, attendance_date)
    VALUES (%s, %s, %s, %s)
    """

    cursor.execute(
        query,
        (
            data["student_id"],
            data["course_id"],
            data["status"],
            data["attendance_date"]
        )
    )

    conn.commit()

    cursor.close()
    conn.close()

    return {"message": "New attendance added successfully!"}


# =======================================
# Delete attendance
# =======================================
@app.delete("/attendance/{attendance_id}")
def delete_attendance(attendance_id: int):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    DELETE FROM attendance
    WHERE attendance_id = %s
    """

    cursor.execute(query, (attendance_id,))

    conn.commit()

    cursor.close()
    conn.close()

    return {"message": "Attendance deleted successfully!"}





# ====================================
# Show Payments
# ====================================
@app.get("/payments")
def show_payments():

    conn = get_connection()
    cursor = conn.cursor()

    query = """SELECT * FROM payments"""

    cursor.execute(query)

    payments = cursor.fetchall()

    cursor.close()
    conn.close()

    return {"payments": payments}


# =====================================
# Add new payment
# =====================================
@app.post("/payments")
def add_payment(data: dict):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO payments
    (student_id, amount, payment_method, payment_status, payment_date)
    VALUES (%s, %s, %s, %s, %s)
    """

    cursor.execute(
        query,
        (
            data["student_id"],
            data["amount"],
            data["payment_method"],
            data["payment_status"],
            data["payment_date"]
        )
    )

    conn.commit()

    cursor.close()
    conn.close()

    return {"message": "New payment added successfully!"}


# =======================================
# Delete payment
# =======================================
@app.delete("/payments/{payment_id}")
def delete_payment(payment_id: int):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    DELETE FROM payments
    WHERE payment_id = %s
    """

    cursor.execute(query, (payment_id,))

    conn.commit()

    cursor.close()
    conn.close()

    return {"message": "Payment deleted successfully!"}





# ====================================
# Show Schedules
# ====================================
@app.get("/schedules")
def show_schedules():

    conn = get_connection()
    cursor = conn.cursor()

    query = """SELECT * FROM schedules"""

    cursor.execute(query)

    schedules = cursor.fetchall()

    cursor.close()
    conn.close()

    return {"schedules": schedules}


# =====================================
# Add new schedule
# =====================================
@app.post("/schedules")
def add_schedule(data: dict):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO schedules
    (course_id, classroom_id, day_of_week, start_time, end_time)
    VALUES (%s, %s, %s, %s, %s)
    """

    cursor.execute(
        query,
        (
            data["course_id"],
            data["classroom_id"],
            data["day_of_week"],
            data["start_time"],
            data["end_time"]
        )
    )

    conn.commit()

    cursor.close()
    conn.close()

    return {"message": "New schedule added successfully!"}


# =======================================
# Delete schedule
# =======================================
@app.delete("/schedules/{schedule_id}")
def delete_schedule(schedule_id: int):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    DELETE FROM schedules
    WHERE schedule_id = %s
    """

    cursor.execute(query, (schedule_id,))

    conn.commit()

    cursor.close()
    conn.close()

    return {"message": "Schedule deleted successfully!"}