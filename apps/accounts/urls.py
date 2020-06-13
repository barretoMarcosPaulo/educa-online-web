from django.urls import path
from .views import RegisterSchool
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [

    path('cadastro-escola/', RegisterSchool.as_view(), name='school_register'),
    path('entrar/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('sair/', auth_views.LogoutView.as_view(), name='logout'),
]
