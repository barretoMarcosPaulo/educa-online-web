from django.urls import path
from .views import ListTeachersSchool, ListAddSubjects, ListAddClassRoomm

app_name = 'school'

urlpatterns = [

    path('meus-professores/', ListTeachersSchool.as_view(), name='list_teachers'),
    path('materias/', ListAddSubjects.as_view(), name='subjects'),
    path('turmas/', ListAddClassRoomm.as_view(), name='class_room'),

]
