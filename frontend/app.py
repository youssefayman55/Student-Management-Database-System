# -----------------------------------
# import libraries
# -----------------------------------
import streamlit as st 
import pandas as pd 
import requests



# -----------------------------------
# PAGE CONFIG
# -----------------------------------
st.set_page_config(
    page_title="Student Management System",
    page_icon='🎓',
    layout="wide",
    initial_sidebar_state="expanded"
)


# -----------------------------------
# Slidebar Image
# -----------------------------------
st.sidebar.image("D:/Projects/SQL DB Projects/Project 4 = Student Management Database/GettyImages-1072191138.webp", width='stretch')
st.sidebar.write("Welcome to the Student Management System! Use the sidebar to navigate through different sections and manage student data effectively. ")



# -----------------------------------
# SIDEBAR
# -----------------------------------
menu = st.sidebar.selectbox(
    "Select a page",
    [
        "Home", 
        "Students", 
        "Teachers", 
        "Departments", 
        "Courses",
        "Enrollments", 
        "Exams" ,
        "Grades", 
        "Attendance", 
        "Schedule", 
        "Payments"        
])



# -----------------------------------
# API URL
# -----------------------------------
BASE_URL = "http://127.0.0.1:8000"



# -----------------------------------
# Home 
# -----------------------------------
if menu =="Home" :
    st.title("🎓 Student Management System")
    st.image("D:/Projects/SQL DB Projects/Project 4 = Student Management Database/uni-connect-evaluation-reports.jpg", width='stretch')
    st.write("A Student Management System (SMS) is a comprehensive database-driven application designed to efficiently manage and organize all academic and administrative activities within an educational institution. It provides a centralized platform for storing, updating, and retrieving student-related information such as personal details, enrollment records, courses, grades, attendance, and academic performance.")
    st.write("The system ensures smooth management of student data by enabling structured operations like student registration, course enrollment, grade assignment, and academic tracking. It also supports automated business logic through stored procedures and triggers, ensuring data consistency, integrity, and real-time validation of operations such as preventing duplicate enrollments and generating academic alerts.")
    st.write("Additionally, the system includes analytical views that provide meaningful insights such as student performance (GPA), course statistics, and departmental reports, helping administrators and instructors make informed decisions.")



# -----------------------------------
# Students
# -----------------------------------
if menu == "Students" :

    st.header("🎓 Students")
    
    # Show the history of students
    st.subheader("Students Data")

    if st.button("Refresh"):
        response = requests.get(f"{BASE_URL}/students")

        if response.status_code == 200 :
            data = response.json()

        df = pd.DataFrame(data["students"] , columns= [
            "student_id", 
            "full_name", 
            "email", 
            "phone", 
            "date_of_birth" , 
            "gender",
            "address",
            "enrollment_date",
            "department_id" , 
            "created_at"
        ])

        st.dataframe(df , width="stretch")
    else:
         st.error("Refresh to show data")


    # add new student
    st.subheader("Add New Student")

    with st.form("add_student_form"):
        full_name = st.text_input("Full Name")
        email = st.text_input("Email")
        phone = st.text_input("Phone")
        date_of_birth = st.date_input("Date of birth")
        gender = st.selectbox("Select Gender", ["Male", "Female"])
        address = st.text_input("Address")
        enrollment_date = st.date_input("Enrollment Date")
        department_id = st.number_input("Department ID" ,step = 1)

        submitted = st.form_submit_button("Add Student")
            
        if submitted:
                student_data = {
                    "full_name":full_name ,
                    "email": email,
                    "phone": phone,
                    "date_of_birth": str(date_of_birth),
                    "gender": gender,
                    "address": address,
                    "enrollment_date": str(enrollment_date),
                    "department_id": department_id,
                }
                response = requests.post(f"{BASE_URL}/students", json=student_data)

                if response.status_code ==  200:
                    st.success("Student added successfully!")
                else:
                    st.error("Faild to add new student")
    


    # Delete Students
    st.subheader("Delete Student")

    with st.form("Delete Student"):
        student_name = st.text_input("Student Name")

        submitted = st.form_submit_button("Delete")

        if submitted : 
            response = requests.delete(f"{BASE_URL}/students/{student_name}")
            
            if response.status_code == 200 :
                 st.success("Student deleted successfully!")
            else:
                 st.error("Faild to delete student")
  


# -----------------------------------
# Teachers 
# -----------------------------------
if menu == "Teachers":

    st.header("Teachers")

    # show teachers 
    if st.button("Refresh Data"):
        response = requests.get(f"{BASE_URL}/teachers")

        if response.status_code == 200 :
        
            data = response.json()

        df = pd.DataFrame(data = data  , 
                          columns=["teacher_id" , "full_name" , "email" , "phone" , "specialization" ,"hire_date", "salary" ,"department_id", "created_at"])
        
        st.dataframe(df , width="stretch")
    else:
        st.error("Refrech to show teachers data")


    # Add new teacher 
    st.subheader("Add new teacher")
    with st.form("Add new teacher"):
        full_name = st.text_input("Full Name")
        email = st.text_input("Email")
        phone = st.text_input("Phone")
        specialization = st.selectbox("Select" , ["Artificial Intelligence","Marketing","Mechanical Engineering","Cardiology","Statistics","Software Engineering","Finance","Physics","Data Science","Biology"])
        hire_date = st.date_input("Hire Date")
        salary = st.text_input("Salary")
        department_id = st.text_input("Department ID")
        
        submitted = st.form_submit_button("Add Teacher")

        if submitted:
            teacher_data = {
                "full_name" : full_name , 
                "email" : email , 
                "phone" : phone , 
                "specialization" : specialization , 
                "hire_date" : str(hire_date) , 
                "salary" : salary , 
                "department_id" : department_id 
            }

            response = requests.post(f"{BASE_URL}/teachers" , json =teacher_data)

            if response.status_code == 200 :
                st.success("New teacher added successfully!")
            
            else:
                st.error("Failed to add new teacher")

    
    # Delete Teacher Data 
    st.subheader("Delete Teacher Data")

    with st.form("Delete Teacher Data"):
        full_name = st.text_input("Full Name")

        submitted = st.form_submit_button("Delete")

        if submitted:
            response = requests.delete(f"{BASE_URL}/delete/{full_name}")

            if response.status_code == 200 :
                st.success("Teacher data deleted successfully!")
            else :
                st.error("Failed to delete teacher data , Try again!")



# ===================================
# Departments
# ===================================

if menu == "Departments" :

    # 1- Show departments
    st.subheader("Departments Information")

    if st.button("Show Departments"):
        response = requests.get(f"{BASE_URL}/departments")

        if response.status_code == 200 : 
            data = response.json()

            df = pd.DataFrame(
                data["departments"],
                columns=["department_id", "department_name", "office_location" , "created_at"]
        )
    
        st.dataframe(df , width="stretch")

    else: 
        st.error("Refresh!")

    
    # 2- Add new Department 
    st.subheader("Add New Department")

    with st.form("Add new department"):
        department_name = st.text_input("Department Name")
        office_location = st.text_input("Office Location")

        submitted = st.form_submit_button("Add New Department")

        if submitted :
            data= {
                "department_name" : department_name,
                "office_location" : office_location
            }
            response = requests.post(f"{BASE_URL}/departments",json=data)

            if response.status_code == 200 :
                st.success("New department added successfully!")

        else:
            st.error("Failed to add new department")


        # 3- Delete any department 
        st.subheader("Delete department")

    with st.form("Delete Department"):
        department_name = st.text_input("Department Name")

        submitted = st.form_submit_button("Delete")

        if submitted:
            response = requests.delete(f"{BASE_URL}/delete/{department_name}")

            if response.status_code == 200 :
                st.success("Department deleted successfully!")
        else:
            st.error("Failed to delete department!")


# ==============================
# courses
# ==============================

if menu == "Courses":

    # =====================================
    # Show Courses
    # =====================================
    st.subheader("Courses Information")

    if st.button("Show Courses"):

        response = requests.get(f"{BASE_URL}/courses")

        if response.status_code == 200:

            data = response.json()

            df = pd.DataFrame(
                data["courses"],
                columns=[
                    "course_id",
                    "course_name",
                    "course_code",
                    "credits",
                    "department_id",
                    "teacher_id",
                    "classroom_id",
                    "created_at"
                ]
            )

            st.dataframe(df, width="stretch")

        else:
            st.error("Failed to load courses!")



    # =====================================
    # Add New Course
    # =====================================
    st.subheader("Add New Course")

    with st.form("Add new Course"):

        course_name = st.text_input("Course Name")
        course_code = st.text_input("Course Code")

        credits = st.number_input(
            "Credits",
            min_value=1,
            step=1
        )

        department_id = st.number_input(
            "Department ID",
            min_value=1,
            step=1
        )

        teacher_id = st.number_input(
            "Teacher ID",
            min_value=1,
            step=1
        )

        classroom_id = st.number_input(
            "Classroom ID",
            min_value=1,
            step=1
        )

        submitted = st.form_submit_button("Add New Course")

        if submitted:

            data = {
                "course_name": course_name,
                "course_code": course_code,
                "credits": credits,
                "department_id": department_id,
                "teacher_id": teacher_id,
                "classroom_id": classroom_id
            }

            response = requests.post(
                f"{BASE_URL}/courses",
                json=data
            )

            if response.status_code == 200:
                st.success("New course added successfully!")

            else:
                st.error("Failed to add new course!")



    # =====================================
    # Delete Course
    # =====================================
    st.subheader("Delete Course")

    with st.form("Delete Course"):

        course_name = st.text_input("Course Name To Delete")

        submitted = st.form_submit_button("Delete")

        if submitted:

            response = requests.delete(
                f"{BASE_URL}/courses/{course_name}"
            )

            if response.status_code == 200:
                st.success("Course deleted successfully!")

            else:
                st.error("Failed to delete course!")



# ==============================
# Enrollments
# ==============================
if menu == "Enrollments":

    # =====================================
    # Show Enrollments
    # =====================================
    st.subheader("Enrollments Information")

    if st.button("Show Enrollments"):

        response = requests.get(f"{BASE_URL}/enrollments")

        if response.status_code == 200:

            data = response.json()

            df = pd.DataFrame(
                data["enrollments"],
                columns=[
                    "enrollment_id",
                    "student_id",
                    "course_id",
                    "status" ,
                    "enrollment_date"
                ]
            )

            st.dataframe(df, width="stretch")

        else:
            st.error("Failed to load enrollments!")



    # =====================================
    # Add New Enrollment
    # =====================================
    st.subheader("Add New Enrollment")

    with st.form("Add new Enrollment"):

        student_id = st.number_input("Student ID", min_value=1, step=1)
        course_id = st.number_input("Course ID", min_value=1, step=1)
        status = st.text_input("Status")

        submitted = st.form_submit_button("Add New Enrollment")

        if submitted:

            data = {
                "student_id": student_id,
                "course_id": course_id,
                "status": status
            }

            response = requests.post(
                f"{BASE_URL}/enrollments",
                json=data
            )

            if response.status_code == 200:
                st.success("New enrollment added successfully!")

            else:
                st.error("Failed to add new enrollment!")



    # =====================================
    # Delete Enrollment
    # =====================================
    st.subheader("Delete Enrollment")

    with st.form("Delete Enrollment"):

        enrollment_id = st.number_input("Enrollment ID To Delete", min_value=1, step=1)

        submitted = st.form_submit_button("Delete")

        if submitted:

            response = requests.delete(
                f"{BASE_URL}/enrollments/{enrollment_id}"
            )

            if response.status_code == 200:
                st.success("Enrollment deleted successfully!")

            else:
                st.error("Failed to delete enrollment!")


# ==============================
# Exams
# ==============================
if menu == "Exams":

    # =====================================
    # Show Exams
    # =====================================
    st.subheader("Exams Information")

    if st.button("Show Exams"):

        response = requests.get(f"{BASE_URL}/exams")

        if response.status_code == 200:

            data = response.json()

            df = pd.DataFrame(
                data["exams"],
                columns=[
                    "exam_id",
                    "course_id",
                    "exam_name",
                    "exam_date",
                    "total_marks",
                ]
            )

            st.dataframe(df, width="stretch")

        else:
            st.error("Failed to load exams!")


    # =====================================
    # Add New Exam
    # =====================================
    st.subheader("Add New Exam")

    with st.form("Add new Exam"):

        course_id = st.number_input( "Course ID",min_value=1, step=1)
        exam_name = st.text_input("Exam Name")
        exam_date = st.text_input("Exam Date (YYYY-MM-DD)")
        total_marks = st.number_input("Total Marks",min_value=1, step=1 )

        submitted = st.form_submit_button("Add New Exam")

        if submitted:

            data = {
                "course_id": course_id,
                "exam_name": exam_name,
                "exam_date": exam_date,
                "exam_date": exam_date,
                "total_marks": total_marks
            }

            response = requests.post(
                f"{BASE_URL}/exams",
                json=data
            )

            if response.status_code == 200:
                st.success("New exam added successfully!")
            else:
                st.error("Failed to add new exam!")


    # =====================================
    # Delete Exam
    # =====================================
    st.subheader("Delete Exam")

    with st.form("Delete Exam"):

        exam_name = st.text_input("Exam Name To Delete")

        submitted = st.form_submit_button("Delete")

        if submitted:

            response = requests.delete(
                f"{BASE_URL}/exams/{exam_name}"
            )

            if response.status_code == 200:
                st.success("Exam deleted successfully!")
            else:
                st.error("Failed to delete exam!")



# ==============================
# Grades
# ==============================
if menu == "Grades":

    # =====================================
    # Show Grades
    # =====================================
    st.subheader("Grades Information")

    if st.button("Show Grades"):

        response = requests.get(f"{BASE_URL}/grades")

        if response.status_code == 200:

            data = response.json()

            df = pd.DataFrame(
                data["grades"],
                columns=[
                    "grade_id",
                    "student_id",
                    "exam_id",
                    "marks_obtained",
                    "grade",
                    "status",
])

            st.dataframe(df, width="stretch")

        else:
            st.error("Failed to load grades!")



    # =====================================
    # Add New Grade
    # =====================================
    st.subheader("Add New Grade")

    with st.form("Add new Grade"):

        student_id = st.number_input(
            "Student ID",
            min_value=1,
            step=1
        )

        exam_id = st.number_input(
            "Exam ID",
            min_value=1,
            step=1
        )
        marks_obtained = st.selectbox("Marks Obtained" , ["A", "B", "C" ,"D" ,"F"])

        grade = st.number_input(
            "Grade",
            min_value=0.0,
            max_value=100.0,
            step=0.1
        )
        status = st.text_input("Status")

        submitted = st.form_submit_button("Add New Grade")

        if submitted:

            data = {
                "student_id": student_id,
                "exam_id": exam_id,
                "marks_obtained": marks_obtained,
                "grade": grade ,
                "status": status
            }

            response = requests.post(
                f"{BASE_URL}/grades",
                json=data
            )

            if response.status_code == 200:
                st.success("New grade added successfully!")

            else:
                st.error("Failed to add new grade!")



    # =====================================
    # Delete Grade
    # =====================================
    st.subheader("Delete Grade")

    with st.form("Delete Grade"):

        grade_id = st.number_input(
            "Grade ID To Delete",
            min_value=1,
            step=1
        )

        submitted = st.form_submit_button("Delete")

        if submitted:

            response = requests.delete(
                f"{BASE_URL}/grades/{grade_id}"
            )

            if response.status_code == 200:
                st.success("Grade deleted successfully!")

            else:
                st.error("Failed to delete grade!")




# ==============================
# attendance
# ==============================
if menu == "Attendance":

    # =====================================
    # Show Attendance
    # =====================================
    st.subheader("Attendance Information")

    if st.button("Show Attendance"):

        response = requests.get(f"{BASE_URL}/attendance")

        if response.status_code == 200:

            data = response.json()

            df = pd.DataFrame(
                data["attendance"],
                columns=[
                    "attendance_id",
                    "student_id",
                    "course_id",
                    "status",
                    "attendance_date"
                ]
            )

            st.dataframe(df, width="stretch")

        else:
            st.error("Failed to load attendance!")



    # =====================================
    # Add New Attendance
    # =====================================
    st.subheader("Add New Attendance")

    with st.form("Add new Attendance"):

        student_id = st.number_input( "Student ID", min_value=1, step=1)
        course_id = st.number_input( "Course ID", min_value=1, step=1)
        status = st.selectbox( "Status",["Present", "Absent"])
        attendance_date = st.date_input("Attendance Date")

        submitted = st.form_submit_button("Add New Attendance")

        if submitted:

            data = {
                "student_id": student_id,
                "course_id": course_id,
                "status": status,
                "attendance_date": str(attendance_date)
            }

            response = requests.post(
                f"{BASE_URL}/attendance",
                json=data
            )

            if response.status_code == 200:
                st.success("New attendance added successfully!")

            else:
                st.error("Failed to add new attendance!")



    # =====================================
    # Delete Attendance
    # =====================================
    st.subheader("Delete Attendance")

    with st.form("Delete Attendance"):

        attendance_id = st.number_input(
            "Attendance ID To Delete",
            min_value=1,
            step=1
        )

        submitted = st.form_submit_button("Delete")

        if submitted:

            response = requests.delete(
                f"{BASE_URL}/attendance/{attendance_id}"
            )

            if response.status_code == 200:
                st.success("Attendance deleted successfully!")

            else:
                st.error("Failed to delete attendance!")





# ==============================
# schedules
# ==============================
if menu == "Schedule":

    # =====================================
    # Show Schedules
    # =====================================
    st.subheader("Schedules Information")

    if st.button("Show Schedules"):

        response = requests.get(f"{BASE_URL}/schedules")

        if response.status_code == 200:

            data = response.json()

            df = pd.DataFrame(
                data["schedules"],
                columns=[
                    "schedule_id",
                    "course_id",
                    "classroom_id",
                    "day_of_week",
                    "start_time",
                    "end_time",
                ]
            )

            st.dataframe(df, width="stretch")

        else:
            st.error("Failed to load schedules!")



    # =====================================
    # Add New Schedule
    # =====================================
    st.subheader("Add New Schedule")

    with st.form("Add new Schedule"):

        course_id = st.number_input(
            "Course ID",
            min_value=1,
            step=1
        )

        classroom_id = st.number_input(
            "Classroom ID",
            min_value=1,
            step=1
        )

        day_of_week = st.selectbox(
            "Day Of Week",
            [
                "Sunday",
                "Monday",
                "Tuesday",
                "Wednesday",
                "Thursday",
                "Friday",
                "Saturday"
            ]
        )

        start_time = st.text_input(
            "Start Time (HH:MM)"
        )

        end_time = st.text_input(
            "End Time (HH:MM)"
        )

        submitted = st.form_submit_button("Add New Schedule")

        if submitted:

            data = {
                "course_id": course_id,
                "classroom_id": classroom_id,
                "day_of_week": day_of_week,
                "start_time": start_time,
                "end_time": end_time
            }

            response = requests.post(
                f"{BASE_URL}/schedules",
                json=data
            )

            if response.status_code == 200:
                st.success("New schedule added successfully!")

            else:
                st.error("Failed to add new schedule!")



    # =====================================
    # Delete Schedule
    # =====================================
    st.subheader("Delete Schedule")

    with st.form("Delete Schedule"):

        schedule_id = st.number_input(
            "Schedule ID To Delete",
            min_value=1,
            step=1
        )

        submitted = st.form_submit_button("Delete")

        if submitted:

            response = requests.delete(
                f"{BASE_URL}/schedules/{schedule_id}"
            )

            if response.status_code == 200:
                st.success("Schedule deleted successfully!")

            else:
                st.error("Failed to delete schedule!")




# ==============================
# payments
# ==============================
if menu == "Payments":

    # =====================================
    # Show Payments
    # =====================================
    st.subheader("Payments Information")

    if st.button("Show Payments"):

        response = requests.get(f"{BASE_URL}/payments")

        if response.status_code == 200:

            data = response.json()

            df = pd.DataFrame(
                data["payments"],
                columns=[
                    "payment_id",
                    "student_id",
                    "amount",
                    "payment_method",
                    "status",
                    "payment_date",
                ]
            )

            st.dataframe(df, width="stretch")

        else:
            st.error("Failed to load payments!")



    # =====================================
    # Add New Payment
    # =====================================
    st.subheader("Add New Payment")

    with st.form("Add new Payment"):

        student_id = st.number_input("Student ID",min_value=1,step=1)

        amount = st.number_input(  "Amount", min_value=0.0, step=1.0)

        payment_method = st.selectbox( "Payment Method", ["Cash", "Credit Card", "Visa", "Bank Transfer"])

        payment_status = st.selectbox( "Payment Status", ["Paid", "Pending", "Failed"])

        payment_date = st.date_input( "Payment Date")

        submitted = st.form_submit_button("Add New Payment")

        if submitted:

            data = {
                "student_id": student_id,
                "amount": amount,
                "payment_method": payment_method,
                "payment_status": payment_status,
                "payment_date": str(payment_date)
            }

            response = requests.post(
                f"{BASE_URL}/payments",
                json=data
            )

            if response.status_code == 200:
                st.success("New payment added successfully!")

            else:
                st.error("Failed to add new payment!")



    # =====================================
    # Delete Payment
    # =====================================
    st.subheader("Delete Payment")

    with st.form("Delete Payment"):

        payment_id = st.number_input(
            "Payment ID To Delete",
            min_value=1,
            step=1
        )

        submitted = st.form_submit_button("Delete")

        if submitted:

            response = requests.delete(
                f"{BASE_URL}/payments/{payment_id}"
            )

            if response.status_code == 200:
                st.success("Payment deleted successfully!")

            else:
                st.error("Failed to delete payment!")
