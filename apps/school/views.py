from django.shortcuts import render
from django.views.generic import TemplateView
from .models import SchoolInstitution,Teacher


class ListTeachersSchool(TemplateView):
    template_name = "teachers_list.html"

    def get_context_data(self, **kwargs):
        context = super(ListTeachersSchool, self).get_context_data(**kwargs)
        school_user = SchoolInstitution.objects.get(pk=self.request.user.id)
        all_teachers_school = Teacher.objects.filter(school__id=school_user.id)

        context['teachers'] = all_teachers_school

        return context


class ListAddSubjects(TemplateView):
    template_name = "subjects.html"
