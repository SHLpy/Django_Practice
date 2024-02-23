from django.urls import path
from . import views
urlpatterns = [
    path('first/', views.first_view),
    path('second/', views.second_view),
    path('third/', views.third_view),
]
