from django.contrib import admin

# Register your models here.
from academics.models import Studentacademics
class StudentacademicsAdmin(admin.ModelAdmin):
    
    list_display=["studentrollno","maths","physics","chemistry","biology","english"]
admin.site.register(Studentacademics,StudentacademicsAdmin)
