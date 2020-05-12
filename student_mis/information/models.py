from django.db import models
from django.utils import timezone


class StudentInfo(models.Model):
    name = models.CharField(max_length=100)
    student_id = models.CharField(max_length=20)
    phone = models.IntegerField()
    gender = models.CharField(max_length=10,choices=(
        ('Male','Male'),
        ('Female','Female')
    ))
    image = models.ImageField(upload_to='images/',null=True)
    year_joined = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']    


