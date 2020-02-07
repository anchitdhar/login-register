from django.db import models

# Create your models here.
class student(models.Model):
    fname = models.CharField(max_length=20)
    femail = models.EmailField(null=False)
    phoneno = models.CharField(max_length=20)
    class Meta:
        db_table = "student"