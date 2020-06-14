from django.shortcuts import render
from django.views.generic import TemplateView

class Index(TemplateView):
    template_name = "index.html"


class DashboardSchool(TemplateView):
    template_name = "school_dashboard.html"


class DashboardTeacher(TemplateView):
    template_name = "teacher_dashboard.html"
