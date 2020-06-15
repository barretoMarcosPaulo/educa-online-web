from django.urls import path
from .views import ListTeachersSchool

app_name = 'school'

urlpatterns = [

    path('meus-professores/', ListTeachersSchool.as_view(), name='list_teachers'),

]
