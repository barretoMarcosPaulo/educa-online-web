from django.urls import path
from .views import Dashboard, Index

app_name = 'core'

urlpatterns = [

    path('painel/', Dashboard.as_view(), name='dashboard'),
    path('', Index.as_view(), name='home'),

]
