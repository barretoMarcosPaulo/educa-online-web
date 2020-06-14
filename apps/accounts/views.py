from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, RedirectView
from .forms import UserSchoolForm, UserTeacherForm


def check_user_type(request):
    user = request.user
    if(user.get_type_user() == 'school'):
        return redirect('core:dashboard_school')
    else:
        return redirect('core:dashboard_teacher')


class RegisterSchool(CreateView):
    template_name = "school/register.html"
    form_class = UserSchoolForm
    

class RegisterTeacher(CreateView):
    template_name = "teacher/register.html"
    form_class = UserTeacherForm
