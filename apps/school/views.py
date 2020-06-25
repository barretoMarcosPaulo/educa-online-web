from django.shortcuts import render
from django.views.generic import TemplateView
from .models import SchoolInstitution,Teacher, SchoolSubjects
from django.urls import reverse
from django.shortcuts import redirect


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


    def get_context_data(self, **kwargs):
        context = super(ListAddSubjects, self).get_context_data(**kwargs)
        user_school = SchoolInstitution.objects.get(pk=self.request.user.pk)
        context['subjects'] = user_school.subjects.all().order_by('-created_at')

        return context

    def post(self, request, *args, **kwargs):

        subjects = request.POST.get('subjects')
        subjects_array = subjects.split(',')
        subjects_created = list()
        
        for subject in subjects_array:
            if subject != ' ':
                try:
                    subject_save = SchoolSubjects.objects.get(name=subject)
                    subjects_created.append(subject_save)
                except:
                    new_subject = SchoolSubjects.objects.create(name=subject)
                    subjects_created.append(new_subject)


        user_school = SchoolInstitution.objects.get(pk=self.request.user.pk)
        user_school.subjects.add(*subjects_created)

        return redirect('school:subjects')
