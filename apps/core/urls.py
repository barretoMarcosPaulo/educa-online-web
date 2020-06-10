from django.urls import path
from .views import SchoolDashboard

app_name = 'core'

urlpatterns = [

    path('painel-da-escola/', SchoolDashboard.as_view(), name='school_dashboard')

]