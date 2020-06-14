from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, RedirectView

from .forms import UserSchoolForm, UserTeacherlForm


class RegisterSchool(CreateView):
    template_name = "school/register.html"
    form_class = UserSchoolForm
    

class RegisterTeacher(CreateView):
    template_name = "teacher/register.html"
    form_class = UserSchoolForm
