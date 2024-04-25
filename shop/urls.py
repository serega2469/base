from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name='index'),
    path('<int:course_id>', single_course, name='single_course')
]