from django.db import models

# Create your models here.from django.db import models







# Create your models here.


class studentmanager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=False)


class studentId(models.Model):
    id = models.AutoField(primary_key=True)
    student_id= models.CharField(max_length = 100)


    def __str__(self) -> str:
        return str(self.student_id)
    

class Department(models.Model):
    department=models.CharField(max_length=500) 
    #foreign key to Department model


    def __str__(self) -> str:
        return self.department  

    class meta :
        ordering=['department'] 


class student(models.Model):
    name=models.CharField(max_length=50)   
    address=models.TextField()
    # image=models.ImageField(upload_to='images/',blank=True)
    
    student_id=models.OneToOneField(studentId,  on_delete=models.CASCADE,max_length=50)
    age=models.IntegerField(default=0)
    department=models.ForeignKey(Department,on_delete=models.CASCADE,default=None) #foreign key to Department model
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=20,default=False)
    is_deleted=models.BooleanField(default=False)

    objects=studentmanager()
    admin_objects=models.Manager()

    def __str__(self) -> str:
        return self.name  
    
    class meta:
        ordering=['name']
        verbose_name='student'

class Subject(models.Model):
    subject_name=models.CharField(max_length=100)
    def  __str__(self) -> str:
        return self.subject_name
    
class SubjectMarks(models.Model):
    student=models.ForeignKey(student,related_name='studentmarks',on_delete=models.SET_NULL,null=True,blank=True)
    subject=models.ForeignKey(Subject,on_delete=models.SET_NULL, null=True)
    marks=models.IntegerField()

    class Meta:
        unique_together=['student','subject']
    
    def __str__(self) -> str:
        return f"{self.student.name}-{self.subject.subject_name}"

class ReportCard(models.Model):
    student=models.ForeignKey(student,related_name='studentreportcard',on_delete=models.CASCADE)
    student_rank=models.IntegerField()
    date_of_report_card_generation=models.DateField(auto_now_add=True)

    class Meta:
        unique_together=['student_rank']


class create_Reportcard(models.Model):
    student=models.ForeignKey(student,on_delete=models.SET('Not Found'),null=True, blank=True)
    student_identifier=models.ForeignKey(studentId,  on_delete=models.CASCADE,max_length=50)

    
    subject=models.ForeignKey(Subject,on_delete=models.SET_NULL,null=True, blank=True)
    marks=models.IntegerField(blank=False)


    def __str__(self) -> str:
        return self.student.name
    


class professors(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(unique=True)
    department=models.ForeignKey(Department, on_delete=models.CASCADE)
    subject=models.ForeignKey(Subject, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return f'{self.name} from- {self.department} department- teaching- {self.subject}'

    

# class login_Student(models.Model) :
#     student_id=models.ForeignKey(studentId, on_delete=models.CASCADE)   
    
#     def check_password(self,password):
#         if self.password==password: 
#             return True
#         else:
#             return False




# class email(models.Model):
    
#     Email=models.EmailField(unique=True, max_length=254)  
#     Subject=models.TextField()
#     messegs=models.TextField()
    
    
    

 
