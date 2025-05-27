from django.db import models
from cursos.models import IntensivePrepCourse

class Student(models.Model):
    full_name = models.CharField(max_length=100)
    dni = models.CharField(max_length=20, unique=True)
    course = models.ForeignKey(IntensivePrepCourse, on_delete=models.CASCADE)

    def __str__(self):
        return self.full_name

class MonthlyFee(models.Model): #cuota
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    month = models.IntegerField()  # 1 = Jan, ..., 12 = Dec
    year = models.IntegerField()
    is_paid = models.BooleanField(default=False)
    payment_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return f'{self.student} - {self.month}/{self.year}'
