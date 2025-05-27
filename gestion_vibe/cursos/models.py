from django.db import models

class IntensivePrepCourse(models.Model):  # CPI
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2) #monto
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name