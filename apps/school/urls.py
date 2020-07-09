from django.urls import path
from .views import ListTeachersSchool, ListAddSubjects, ListAddClassRoomm, TeacherClassRoom
from .views import TeacherSubjects

app_name = 'school'

urlpatterns = [

    path('meus-professores/', ListTeachersSchool.as_view(), name='list_teachers'),
    path('materias/', ListAddSubjects.as_view(), name='subjects'),
    path('turmas/', ListAddClassRoomm.as_view(), name='class_room'),

    path('professor/materias/', TeacherSubjects.as_view(), name='subjects_teacher'),
    path('professor/turmas/', TeacherClassRoom.as_view(), name='class_room_teacher'),

]
