from django.contrib import admin

# Register your models here.

from testapp.models import Movie

class MovieAdmin(admin.ModelAdmin):
    list_display = ['rdate','Moviename','hero','heroine','rating']
admin.site.register(Movie,MovieAdmin)


