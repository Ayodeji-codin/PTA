from django.db import models

# Create your models here.

class Classes(models.Model):
    school_class = models.CharField(max_length=200)

    def __str__(self):
        return self.school_class
    
class Subject(models.Model):
    subject = models.CharField(max_length=50,unique=True)

    def __str__(self):
        return self.subject

class Student(models.Model):
    name = models.CharField(max_length=90,unique=True)
    id_num = models.IntegerField(default=1,null=False,blank=False)
    date_admitted = models.DateField(auto_now_add=True)
    student_class = models.ForeignKey(Classes, on_delete=models.SET_NULL,blank=True,null=True)
    subjects = models.ManyToManyField(Subject)

    def __str__(self):
        return f'{self.name}'
    

class Evaluation(models.Model):
    id_num = models.IntegerField(default=1,null=False,blank=False)
    student = models.ForeignKey(Student, on_delete=models.CASCADE,related_name='student')
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    assignments = models.IntegerField()
    test1 = models.IntegerField()
    test2 = models.IntegerField()
    exam = models.IntegerField()
    comment = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.student} {self.subject} evaluation'

    def get_subject_total_score(self):
        total_score = self.test1 + self.test2 + self.exam
        return total_score

    def grading(self):
        total_score = self.test1 + self.test2 + self.exam
        if total_score > 69:
            return 'A'
        elif total_score > 59:
            return 'B'
        elif total_score > 49:
            return 'B2'
        elif total_score > 39:
            return 'C4'
        else:
            return 'F9'