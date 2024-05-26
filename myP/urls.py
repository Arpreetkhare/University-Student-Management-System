"""
URL configuration for myP project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myA.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/',get_student,name='get_student'),
    #  path('', get_student, name='home'),
     path('see_marks/<student_id>/', see_marks, name="see_marks"),
     path('send_email/',send_email_to_client),
     path('department/',alldepartment,name= 'department'),
        #  path('students_in_department/',students_in_department, name='students_in_department'),

     path('students/department/<int:department_id>/',students_in_department, name='students_in_department'),
     path('Add/',add_students,name= "add_students"),
     path('prof',main_page,name="MainPage"),
    #  path('CR',create_reportcard,name= 'create_reportcard'),
     path('',home,name='home'),
     path('stu',mainpage2,name= 'mainpage2'),
     path('login',student_login,name='login'),
     path('pro',student_profile,name= 'student_profile'),
     path('login2',professor_login,name='login2'),
     path('dept_stu',show_dep_stu,name= 'show_dep_stu'),

]
