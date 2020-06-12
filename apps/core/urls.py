from django.urls import path
from .views import SchoolDashboard, Index

app_name = 'core'

urlpatterns = [

    path('painel-da-escola/', SchoolDashboard.as_view(), name='school_dashboard'),
    path('', Index.as_view(), name='home'),

]