from django.shortcuts import render
from django.views.generic import TemplateView

class Index(TemplateView):
    template_name = "index.html"

class Dashboard(TemplateView):
    template_name = "school_dashboard.html"
