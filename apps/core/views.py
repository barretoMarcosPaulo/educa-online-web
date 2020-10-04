from django.shortcuts import render
from django.views.generic import TemplateView
from apps.school.models import Teacher, SchoolInstitution
from django.http import HttpResponse, JsonResponse


class Index(TemplateView):
    template_name = "index.html"


class DashboardSchool(TemplateView):
    template_name = "school_dashboard.html"

    def get_context_data(self, **kwargs):
        context = super(DashboardSchool, self).get_context_data(**kwargs)
        context['user_scholl'] = SchoolInstitution.objects.get(id=self.request.user.id)
        return context

class DashboardTeacher(TemplateView):
    template_name = "teacher_dashboard.html"

    def get_context_data(self, **kwargs):
        context = super(DashboardTeacher, self).get_context_data(**kwargs)
        context['user_teacher'] = Teacher.objects.get(id=self.request.user.id)
        return context


class SearchTeacherSchool(TemplateView):

    def get(self, request,code,*args, **kwargs):
        
        try:
            school = SchoolInstitution.objects.get(cod_teacher=code)
            teacher = Teacher.objects.filter(id=self.request.user.id)
            teacher.update(school=school)
            
            return JsonResponse({'msg': "Escola encontrada!", 'code': "1", 'name':school.name})
        except:
            return JsonResponse({'msg': "Nenhuma escola encontrada com este código!", 'code': "0"})



