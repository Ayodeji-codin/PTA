from django.contrib import admin
from .models import *
    
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ['id','name','student_class','date_admitted']
    ordering = ['id']

admin.site.register(Student,StudentAdmin)

class EvaluationAdmin(admin.ModelAdmin):
    list_display = ['student','subject','assignments','test1','test2','exam','comment']
    ordering = ['student']

admin.site.register(Evaluation,EvaluationAdmin)
admin.site.register(Classes)
admin.site.register(Subject)
