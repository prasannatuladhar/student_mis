from django.contrib import admin
from .models import StudentInfo



class  StudentInfoAdmin(admin.ModelAdmin):
    list_display = ['name','student_id','gender','phone','year_joined']
    list_editable = ['phone']
    list_per_page = 10
    list_filter = ['gender']
    search_fields = ['phone','name','student_id']
    


admin.site.register(StudentInfo,StudentInfoAdmin)

