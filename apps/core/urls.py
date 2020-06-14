from django.urls import path
from .views import DashboardSchool, DashboardTeacher, Index

app_name = 'core'

urlpatterns = [

    path('painel/escola/', DashboardSchool.as_view(), name='dashboard_school'),
    path('painel/professor/', DashboardTeacher.as_view(), name='dashboard_teacher'),
    path('', Index.as_view(), name='home'),

]
