from django.shortcuts import render
from django.views.generic import TemplateView
from .models import SchoolInstitution, Teacher, SchoolSubjects, ClassRoomm
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


class ListAddClassRoomm(TemplateView):
    template_name = "class_room.html"

    def get_context_data(self, **kwargs):
        context = super(ListAddClassRoomm, self).get_context_data(**kwargs)
        user_school = SchoolInstitution.objects.get(pk=self.request.user.pk)
        context['class_rooms'] = user_school.class_rooms.all().order_by('-created_at')

        return context

    def post(self, request, *args, **kwargs):

        class_room = request.POST.get('class_rooms')
        class_room_array = class_room.split(',')
        class_room_created = list()

        for class_room in class_room_array:
            if class_room != ' ':
                new_class_room = ClassRoomm.objects.create(name_year=class_room)
                class_room_created.append(new_class_room)

        print(class_room_created)
        user_school = SchoolInstitution.objects.get(pk=self.request.user.pk)
        user_school.class_rooms.add(*class_room_created)

        return redirect('school:class_room')


class TeacherSubjects(TemplateView):
    template_name = "teacher/subjects.html"

    def get_context_data(self, **kwargs):
        context = super(TeacherSubjects, self).get_context_data(**kwargs)
        
        teacher = Teacher.objects.get(pk=self.request.user.pk)
        have_subjects = True
        subjects_suggestions = list()

        if not teacher.subjects.all():
            have_subjects = False
            subjects_suggestions = teacher.school.subjects.all()
        else:
            teacher_subjects = teacher.subjects.all()
            for subject in teacher.school.subjects.all():
                if subject not in teacher_subjects:
                    subjects_suggestions.append(subject)
        
        context['teacher'] = teacher
        context['have_subjects'] = have_subjects
        context['subjects_suggestions'] = subjects_suggestions
        
        return context
    
    def post(self, request, *args, **kwargs):
        subjects_ids = request.POST.get('subjects', None)
        
        teacher = Teacher.objects.get(pk=self.request.user.pk)
        teacher.subjects.add(*subjects_ids.split(','))

        return redirect('school:subjects_teacher')


class TeacherClassRoom(TemplateView):
    template_name = "teacher/class_rooms.html"

    def get_context_data(self, **kwargs):
        context = super(TeacherClassRoom, self).get_context_data(**kwargs)
        teacher = Teacher.objects.get(pk=self.request.user.pk)
        return context
