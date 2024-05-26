from django.shortcuts import render,HttpResponse,redirect,get_object_or_404

from myA.models import *
from django.core.paginator import Paginator
from django.db.models import Q,Sum
from .seed import*
from  django.conf import settings
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages


# Create your views here.

def get_student(request):
   
    queryset=student.objects.all()

    if 'home' in  request.GET:
        return redirect('home')
    

    
    
    if request.GET.get('search'):
        search=request.GET.get('search')
        queryset=queryset.filter(Q(name__icontains=search,name__startswith=search)| Q(department__department__icontains=search)| Q (student_id__student_id__icontains=search))
    
    paginator = Paginator(queryset, 25)  # Show 25 contacts per page.

    page_number = request.GET.get("page",1)
    page_obj = paginator.get_page(page_number)
    return render(request,'get_student.html',{'queryset':page_obj})


def see_marks(request,student_id):# based on student id vo uske marks ko dikhayaga
    generate_report_card()
    queryset=SubjectMarks.objects.filter(student__student_id__student_id=student_id)
    
    total_marks=queryset.aggregate(total_marks=Sum('marks'))
    
    return render(request, 'see_marks.html', {'queryset':queryset ,'total_marks':total_marks})






def students_in_department(request, department_id):
    if request.method == 'GET':
        department = get_object_or_404(Department, pk=department_id)
        students = student.objects.filter(department=department)
        return render(request, 'student.html', {'department': department, 'students': students})
    return redirect("department")


# def students_in_each_deparment(request):
#     departments = Department.objects.all()
#     students_in_departments = {}
#     for department in departments:

#         if request.departments.departmnet:
#             stu=student.objects.filter(department=department)
    # return render(request,'studnt.html',{"stu":stu})


#     # Iterate over each department and filter students for that department
#     # for department in departments:
#     #     students_in_departments[department] = student.objects.filter(department=department)

#     return render(request, 'student.html', {"students_in_departments": students_in_departments})
#          
@csrf_exempt
def send_email_to_client(request):
    subject='iam testing it'
    message='hello is this working , my messege is visiable to you??'
    email = settings.EMAIL_HOST_USER
    recipient_list=['yuty54112@gmail.com']
    file_path= f'{settings.BASE_DIR}/email_template.html'
    

    send_mail(subject,message,email,recipient_list,file_path)
    return redirect('/')


@csrf_exempt
def add_students(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        email = request.POST.get('email')
        age = request.POST.get('age')
        department_id = int(request.POST.get('department'))

        # Get the age parameter from the POST request
        age_str = request.POST.get('age')

        # Check if age parameter is present and non-empty
        if age_str:
            try:
                age = int(age_str)
            except ValueError:
                # Handle the case where age parameter is not a valid integer
                return render(request, 'add.html', {'error_message': 'Invalid age value'})

        else:
            # Handle the case where age parameter is not present or empty
            return render(request, 'add.html', {'error_message': 'Age is required'})


        # Ensure all required fields are present
        if not all([name, address, email, age, department_id]):
            return render(request, 'add.html', {'error_message': 'Missing required fields'})

        try:
            # Get or create student ID object
            student_id_number = request.POST.get('student_id')
            student_id, created = studentId.objects.get_or_create(student_id=student_id_number)

            # Get department object
            department = Department.objects.get(pk=department_id)

            # Create student object
            student.objects.create(name=name, address=address, email=email,
                                   student_id=student_id, age=age, department=department)
            
            return redirect('get_student')

        except (ValueError, Department.DoesNotExist):
            return render(request, 'add.html', {'error_message': 'Invalid form data'})

        


    else:
        # Fetching departments to display in the form
        departments = Department.objects.all()
        return render(request, 'add.html', {'departments': departments})
    


def home(request):
    if request.method=="GET":
        if 'student' in request.GET:
            return redirect('login')
        
        if  'professor' in request.GET:
            return redirect('login2')
        
    return render(request,'home.html')    



def main_page(request) :
    if request.method == "GET":
        if 'department' in request.GET:
            return redirect('department')
        
        if 'student' in request.GET:
            return redirect('get_student')
        
        if 'add_students' in request.GET:
            return redirect('add_students')
        
        if 'home' in request.GET:
            return redirect('home')
    
    return render(request, "main.html")


def mainpage2(request):
    if request.method=="GET":
        if 'department' in request.GET:
            return redirect('department')
        
        if 'student' in request.GET:
            return redirect('get_student')
        
        if 'student_profile' in request.GET:
            return redirect('student_profile')
        
    return render(request,'mainpage2.html') 







# def student_profile(request)  :
#     name=request.session['name']
#     departmnet=request.session['departmnet']
#     student_id=request.session['student_id']
#     address=request.session['address']  
#     email=request.session['email']
#     age=request.session['age']
    
    

    

#     return render(request,"student_profile.html",{'name':name,'departmnet':departmnet,'address':address,'age':age,'student_id':student_id,'email':email})    

from django.shortcuts import render

def student_profile(request):
   
    name = request.GET.get('name')
    department = request.GET.get('department')
    student_id = request.GET.get('student_id')
    address = request.GET.get('address')
    email = request.GET.get('email')
    age = request.GET.get('age')
    
    return render(request, "student_profile.html", {
        'name': name,
        'department': department,
        'student_id': student_id,
        'address': address,
        'email': email,
        'age': age
    })


def student_login(request):
    if request.method == 'POST':
        student_id = request.POST.get('student_id')
        password = request.POST.get('password')
   
        try:
            student_obj = student.objects.get(student_id__student_id=student_id, password=password)
                
            return redirect('mainpage2')
        except student.DoesNotExist:
            error_message = "Invalid student ID or password."
            students = student.objects.all()
            return render(request, 'login.html', {'error_message': error_message,'students':students})     
       
        
    else:
        students = student.objects.all()
        return render(request, 'login.html', {'students': students})
    


def professor_login(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        department_id = request.POST.get('department')
        subject_id = request.POST.get('subject')
        
        try:
            professor = professors.objects.get(name=name, email=email, department_id=department_id, subject_id=subject_id)
            return redirect('MainPage')
        
        except professors.DoesNotExist:
            
            error="invalid data"
            
            departments=Department.objects.all()
            subjects=Subject.objects.all()
        

            return render(request,'login2.html',{'error':error,'departments':departments,'subjects':subjects})


    else:
        departments=Department.objects.all()
        subjects=Subject.objects.all()
        
        return render(request,"login2.html",{'departments':departments,'subjects':subjects})

print("Rendering professor_login view")








# def create_reportcard(request):
#     if request.method == 'POST':
#         # Extract data from the form submission
#         student_id = request.POST.get('student_id')
#         subject_id = request.POST.get('subject_id')
#         marks = request.POST.get('marks')

#         # Get or create student, subject, and studentId instances
#         student_instance, created_student = student.objects.get_or_create(student_id=student_id)
#         subject_instance, created_subject = Subject.objects.get_or_create(id=subject_id)
#         student_id_instance, created_student_id = studentId.objects.get_or_create(student_id=student_id)

#         # Create ReportCard instance
#         report_card = ReportCard.objects.create(
#             student=student_instance,
#             student_identifier=student_id_instance,
#             subject=subject_instance,
#             marks=marks
#         )

#         # Render the template with the context
#         return render(request, 'create_reportcard.html', {'report_card': report_card})
#     else:
#         # If the request method is GET, render the form
#         students = student.objects.all()
#         subjects = Subject.objects.all()

def show_dep_stu(request):
    if 'department' in request.GET:
        department_name = request.GET['department']  # Get the selected department name from GET parameters
        students = student.objects.filter(department__department=department_name)
       
        return render(request, 'show_dep_stu.html', {'students': students})
    else:
       
        return HttpResponse("Department not selected")

def alldepartment(request):
    departments = Department.objects.all()
    return render(request, "alldepartment.html", {"departments": departments})
    
    
    # # Create an empty dictionary to store students for each department
    # students_in_departments = {}

    # # Iterate over each department and filter students for that department
    # for department in departments:
    #     students_in_departments[department] = student.objects.filter(department=department)

