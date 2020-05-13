from django.contrib import admin
from .models import StudentInfo
from import_export.admin import ImportExportModelAdmin



class  StudentInfoAdmin(ImportExportModelAdmin):
    list_display = ['name','student_id','gender','phone','year_joined']
    list_editable = ['phone','year_joined']
    list_per_page = 10
    list_filter = ['gender']
    search_fields = ['phone','name','student_id']
    


admin.site.register(StudentInfo,StudentInfoAdmin)

