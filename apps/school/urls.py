from django.urls import path
from .views import ListTeachersSchool, ListAddSubjects

app_name = 'school'

urlpatterns = [

    path('meus-professores/', ListTeachersSchool.as_view(), name='list_teachers'),
    path('materias/', ListAddSubjects.as_view(), name='subjects'),

]
