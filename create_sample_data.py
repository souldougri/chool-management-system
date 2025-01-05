from django.core.management import execute_from_command_line
import os
import django
from datetime import date, timedelta
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'school_system.settings')
django.setup()

from students.models import Student, StudentCard
from classes.models import ClassRoom, Subject, TeacherProfile
from certificates.models import Grade, Certificate

# Create subjects
subjects = [
    {'name': 'Mathematics', 'code': 'MATH101', 'credit_hours': 4},
    {'name': 'Arabic', 'code': 'ARAB101', 'credit_hours': 4},
    {'name': 'English', 'code': 'ENGL101', 'credit_hours': 4},
    {'name': 'Science', 'code': 'SCIE101', 'credit_hours': 3},
    {'name': 'History', 'code': 'HIST101', 'credit_hours': 2},
    {'name': 'Geography', 'code': 'GEOG101', 'credit_hours': 2}
]

print("Creating subjects...")
for subject in subjects:
    Subject.objects.get_or_create(
        name=subject['name'],
        code=subject['code'],
        credit_hours=subject['credit_hours']
    )

# Create teachers
teachers_data = [
    {'first_name': 'Ahmed', 'last_name': 'Mohamed', 'email': 'ahmed@school.com', 'phone': '0501234567'},
    {'first_name': 'Fatima', 'last_name': 'Ali', 'email': 'fatima@school.com', 'phone': '0501234568'},
    {'first_name': 'Mohamed', 'last_name': 'Khaled', 'email': 'mohamed@school.com', 'phone': '0501234569'},
    {'first_name': 'Sara', 'last_name': 'Ahmed', 'email': 'sara@school.com', 'phone': '0501234570'}
]

print("Creating teachers...")
for teacher in teachers_data:
    teacher_profile = TeacherProfile.objects.get_or_create(
        first_name=teacher['first_name'],
        last_name=teacher['last_name'],
        email=teacher['email'],
        phone_number=teacher['phone']
    )[0]
    # Add subjects to teachers
    subject = Subject.objects.all()[random.randint(0, len(subjects)-1)]
    teacher_profile.subjects.add(subject)

# Create classrooms
classes_data = [
    {'name': 'Class 1A', 'grade_level': '1', 'capacity': 30},
    {'name': 'Class 1B', 'grade_level': '1', 'capacity': 30},
    {'name': 'Class 2A', 'grade_level': '2', 'capacity': 25},
    {'name': 'Class 2B', 'grade_level': '2', 'capacity': 25}
]

print("Creating classrooms...")
for class_info in classes_data:
    classroom, created = ClassRoom.objects.get_or_create(
        name=class_info['name'],
        grade_level=class_info['grade_level'],
        capacity=class_info['capacity']
    )
    teachers = TeacherProfile.objects.all()
    for teacher in teachers[:2]:
        classroom.teachers.add(teacher)

# Create students
student_names = [
    ('Youssef', 'Ahmed'),
    ('Mariam', 'Mohamed'),
    ('Omar', 'Khaled'),
    ('Fatima', 'Ali'),
    ('Zainab', 'Hassan'),
    ('Khaled', 'Mahmoud'),
    ('Nour', 'Abdullah'),
    ('Abdulrahman', 'Mohamed')
]

print("Creating students...")
for first_name, last_name in student_names:
    student = Student.objects.get_or_create(
        first_name=first_name,
        last_name=last_name,
        date_of_birth=date(2010, random.randint(1, 12), random.randint(1, 28)),
        gender='M' if random.random() > 0.5 else 'F',
        address='Sample Address',
        phone_number=f'0{random.randint(100000000, 999999999)}',
        student_id=f'STD{random.randint(1000, 9999)}'
    )[0]
    
    StudentCard.objects.get_or_create(
        student=student,
        card_number=f'CARD{random.randint(1000, 9999)}',
        issue_date=date.today(),
        expiry_date=date.today() + timedelta(days=365)
    )
    
    classroom = ClassRoom.objects.all()[random.randint(0, len(classes_data)-1)]
    student.classroom = classroom
    student.save()

print("Sample data created successfully!")
