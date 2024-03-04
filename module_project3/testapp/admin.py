from django.contrib import admin

# Register your models here.

from testapp.models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = ['rollno', 'name', 'dob', 'marks', 'email', 'phonenumber', 'address']
    
admin.site.register(Student,StudentAdmin)

