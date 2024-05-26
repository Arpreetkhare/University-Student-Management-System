from .models import *
from faker import Faker
fake=Faker()
import random
from django.db.models import Sum



def subject_mark(n):
    try:
        student_obj=student.objects.all()
        for students in student_obj:
            subjects=Subject.objects.all()
            for subject in subjects:
                SubjectMarks.objects.create(
                    student =students,
                    subject=subject,
                    marks=random.randint(0,100),

                )

    except Exception as e:
        print(e)        

def seed_db(n=20):
    try:
        for _ in range(0,n):
            department_obj=Department.objects.all()

            email=fake.email()
            address=fake.address()
            name=fake.name()
            password=fake.password()
           
            department= department_obj[random.randint(0,len(department_obj)-1)]
            age= random.randint(20,25)
            student_id= f"STU-0 {random.randint(100,999)}"

            student_id_obj=studentId.objects.create(student_id=student_id)

            student_obj= student.objects.create(name=name ,
                email=email ,
                age=age ,
                password=password,
                
                department=department,
                student_id=student_id_obj,
                address=address)
             

    except Exception as e:
        print(e)


def generate_report_card():
    try:
       
        report_cards_queryset = ReportCard.objects.all()
        return report_cards_queryset
        
    except Exception as e:
        print(e)
