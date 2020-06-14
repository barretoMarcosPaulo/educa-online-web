from django.db import models
from apps.core.models import TimeStamp
from apps.accounts.models import User
from django.urls import reverse

class SchoolInstitution(User, TimeStamp):
    address = models.CharField('Endereço', max_length=255, blank=False, null=False)
    cod_student = models.CharField("Código do Aluno", max_length=255, blank=False, null=False)
    cod_teacher = models.CharField("Código do Professor", max_length=255, blank=False, null=False)

    class Meta:
        verbose_name = "Escola"
        verbose_name_plural = "Escolas"

    def get_absolute_url(self):
        return reverse('accounts:login')

    def __str__(self):
        return self.name



class SchoolSubjects(TimeStamp):
    name = models.CharField('Nome da matéria', max_length=100, blank=False, null=False)

    class Meta:
        verbose_name = "Matéria"
        verbose_name_plural="Matérias"
    
    def __str__(self):
        return self.name



class ClassRoomm(TimeStamp):
    name_year = models.CharField("Nome/Ano", max_length=100, blank=False, null=False)
    subjects = models.ManyToManyField(SchoolSubjects)
   
    class Meta:
        verbose_name = "Turma"
        verbose_name_plural = "Turmas"

    def __str__(self):
        return self.name_year



class Teacher(User,TimeStamp):
    school = models.ForeignKey(SchoolInstitution,on_delete=models.PROTECT, null=True, blank=True)
    subjects = models.ManyToManyField(SchoolSubjects)
    classroom = models.ManyToManyField(ClassRoomm)

    class Meta:
        verbose_name = "Professor(a)"
        verbose_name_plural = "Professores(as)"

    def get_absolute_url(self):
        return reverse('accounts:login')

    def not_have_school(self):
        not_have = True
        if(self.school):
            not_have = False
        return not_have

    def __str__(self):
        return self.name




class Student(User, TimeStamp):
    school = models.ForeignKey(SchoolInstitution, on_delete=models.PROTECT)
    classroom = models.ForeignKey(ClassRoomm, on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Estudante"
        verbose_name_plural = "Estudante"

    def __str__(self):
        return self.name
