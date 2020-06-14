from django.urls import path
from .views import RegisterSchool, RegisterTeacher, check_user_type
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [

    path('cadastro-escola/', RegisterSchool.as_view(), name='school_register'),
    path('cadastro-professor/', RegisterTeacher.as_view(), name='teacher_register'),

    path('entrar/', auth_views.LoginView.as_view(template_name='login.html',redirect_authenticated_user=True), name='login'),
    path('sair/', auth_views.LogoutView.as_view(), name='logout'),

    path('tipo-de-usuario/', check_user_type, name='check_user_type'),

]
