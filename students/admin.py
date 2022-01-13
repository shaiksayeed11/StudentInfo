from django.contrib import admin
from students.models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display=["studentrollno","studentname","studentclass","school","mobile","address"]
admin.site.register(Student,StudentAdmin)   
