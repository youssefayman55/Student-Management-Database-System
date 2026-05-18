CREATE TABLE "departments" (
  "department_id" serial PRIMARY KEY,
  "department_name" varchar,
  "office_location" varchar,
  "created_at" timestamp
);

CREATE TABLE "students" (
  "student_id" serial PRIMARY KEY,
  "full_name" varchar,
  "email" varchar UNIQUE,
  "phone" varchar,
  "gender" varchar,
  "date_of_birth" date,
  "address" text,
  "enrollment_date" date,
  "department_id" int,
  "created_at" timestamp
);

CREATE TABLE "teachers" (
  "teacher_id" serial PRIMARY KEY,
  "full_name" varchar,
  "email" varchar UNIQUE,
  "phone" varchar,
  "specialization" varchar,
  "hire_date" date,
  "salary" numeric,
  "department_id" int,
  "created_at" timestamp
);

CREATE TABLE "classrooms" (
  "classroom_id" serial PRIMARY KEY,
  "room_number" varchar,
  "building" varchar,
  "capacity" int,
  "created_at" timestamp
);

CREATE TABLE "courses" (
  "course_id" serial PRIMARY KEY,
  "course_name" varchar,
  "course_code" varchar UNIQUE,
  "credits" int,
  "department_id" int,
  "teacher_id" int,
  "classroom_id" int,
  "created_at" timestamp
);

CREATE TABLE "enrollments" (
  "enrollment_id" serial PRIMARY KEY,
  "student_id" int,
  "course_id" int,
  "enrollment_date" date,
  "status" varchar
);

CREATE TABLE "attendance" (
  "attendance_id" serial PRIMARY KEY,
  "student_id" int,
  "course_id" int,
  "attendance_date" date,
  "status" varchar
);

CREATE TABLE "exams" (
  "exam_id" serial PRIMARY KEY,
  "course_id" int,
  "exam_name" varchar,
  "exam_date" date,
  "total_marks" numeric
);

CREATE TABLE "grades" (
  "grade_id" serial PRIMARY KEY,
  "student_id" int,
  "exam_id" int,
  "marks_obtained" numeric,
  "grade" varchar,
  "status" varchar
);

CREATE TABLE "payments" (
  "payment_id" serial PRIMARY KEY,
  "student_id" int,
  "amount" numeric,
  "payment_date" date,
  "payment_method" varchar,
  "payment_status" varchar
);

CREATE TABLE "schedules" (
  "schedule_id" serial PRIMARY KEY,
  "course_id" int,
  "classroom_id" int,
  "day_of_week" varchar,
  "start_time" time,
  "end_time" time
);

ALTER TABLE "students" ADD FOREIGN KEY ("department_id") REFERENCES "departments" ("department_id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "teachers" ADD FOREIGN KEY ("department_id") REFERENCES "departments" ("department_id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "courses" ADD FOREIGN KEY ("department_id") REFERENCES "departments" ("department_id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "courses" ADD FOREIGN KEY ("teacher_id") REFERENCES "teachers" ("teacher_id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "courses" ADD FOREIGN KEY ("classroom_id") REFERENCES "classrooms" ("classroom_id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "enrollments" ADD FOREIGN KEY ("student_id") REFERENCES "students" ("student_id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "enrollments" ADD FOREIGN KEY ("course_id") REFERENCES "courses" ("course_id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "attendance" ADD FOREIGN KEY ("student_id") REFERENCES "students" ("student_id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "attendance" ADD FOREIGN KEY ("course_id") REFERENCES "courses" ("course_id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "exams" ADD FOREIGN KEY ("course_id") REFERENCES "courses" ("course_id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "grades" ADD FOREIGN KEY ("student_id") REFERENCES "students" ("student_id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "grades" ADD FOREIGN KEY ("exam_id") REFERENCES "exams" ("exam_id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "payments" ADD FOREIGN KEY ("student_id") REFERENCES "students" ("student_id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "schedules" ADD FOREIGN KEY ("course_id") REFERENCES "courses" ("course_id") DEFERRABLE INITIALLY IMMEDIATE;

ALTER TABLE "schedules" ADD FOREIGN KEY ("classroom_id") REFERENCES "classrooms" ("classroom_id") DEFERRABLE INITIALLY IMMEDIATE;
