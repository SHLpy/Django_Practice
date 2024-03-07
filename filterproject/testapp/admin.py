from django.contrib import admin

# Register your models here.

from testapp.models import FilterModel

class FilterModelAdmin(admin.ModelAdmin):
    list_display = ['name','subject','dept','date']
admin.site.register(FilterModel,FilterModelAdmin)

