from django.contrib import admin
from testapp.models import Student

# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['rollno', 'name', 'dob', 'marks', 'email', 'phonenumber', 'address']
admin.site.register(Student,StudentAdmin)

