from django.shortcuts import render
from django.views.generic import TemplateView

class SchoolDashboard(TemplateView):
    template_name = "school_dashboard.html"
