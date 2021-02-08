from django.db import models

# Create your models here.
class Parameters(models.Model):
    emp_name=models.CharField(max_length=100)
    body_temp=models.IntegerField()
    blood_pres=models.IntegerField()
    glucose=models.IntegerField()
    heart_rate=models.IntegerField()
    oxygen_satu=models.IntegerField()

    def __str__(self):
        return self.emp_name
