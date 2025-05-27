from django.db import models
from usuarios.models import User
from cursos.models import IntensivePrepCourse

class Attendance(models.Model):
    SHIFT_CHOICES = [
        ('morning', 'Morning'),
        ('afternoon', 'Afternoon'),
        ('evening', 'Evening'),
    ]

    teacher = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'teacher'})
    course = models.ForeignKey(IntensivePrepCourse, on_delete=models.CASCADE)
    shift = models.CharField(max_length=10, choices=SHIFT_CHOICES) #turno
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.teacher} - {self.date} - {self.shift}'
