from django.urls import path
from .views import RegisterSchool

app_name = 'core'

urlpatterns = [

    path('cadastro-escola/', RegisterSchool.as_view(), name='school_register'),

]
