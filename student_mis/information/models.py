from django.db import models


class StudentInfo(models.Model):
    name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20)
    phone = models.IntegerField()
    gender = models.CharField(max_length=10,choices=(
        ('Male','Male'),
        ('Female','Female')
    ))
    image = models.ImageField(upload_to='',null=True)
    year_joined = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


