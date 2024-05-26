from django.contrib import admin

# Register your models here.
from .models import*
from myP.util import *


admin.site.register(studentId)
admin.site.register(Department)

class studentAdmin(admin.ModelAdmin):
    list_display=('name','department','student_id', 'address','email')
admin.site.register(student,studentAdmin)
admin.site.register(Subject)

class SubjectmarkAdmin(admin.ModelAdmin):
    list_display=['student','subject','marks']
admin.site.register(SubjectMarks,SubjectmarkAdmin)

class ReportCardAdmin(admin.ModelAdmin):
    list_display=['student','student_rank','date_of_report_card_generation','total_marks']
    def total_marks(self,obj):
        subject_marks=SubjectMarks.objects.filter(student=obj.student)
        return subject_marks.aggregate(marks=sum('marks'))
admin.site.register(ReportCard,ReportCardAdmin)
admin.site.register(create_Reportcard)

admin.site.register(professors)



