from django.shortcuts import render
from django.views.generic import TemplateView, CreateView

from .forms import UserSchoolForm


class RegisterSchool(CreateView):
    template_name = "school/register.html"
    form_class = UserSchoolForm
    
