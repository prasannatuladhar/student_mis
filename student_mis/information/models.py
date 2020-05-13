from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


class StudentInfo(models.Model):
    manager = models.ForeignKey(User,on_delete=models.CASCADE,default=None)
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


