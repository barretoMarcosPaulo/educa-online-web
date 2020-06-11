from django.db import models
from apps.core.models import TimeStamp
from apps.accounts.models import User


class SchoolInstitution(User, TimeStamp):
    slogan = models.CharField('Slogan da escola', max_length=255, blank=True, null=True)
    address = models.CharField('Endereço', max_length=255, blank=False, null=False)

    class Meta:
        verbose_name = "Escola"
        verbose_name_plural = "Escolas"
    
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
    school = models.ForeignKey(SchoolInstitution,on_delete=models.PROTECT)
    subjects = models.ManyToManyField(SchoolSubjects)
    classroom = models.ManyToManyField(ClassRoomm)

    class Meta:
        verbose_name = "Professor(a)"
        verbose_name_plural = "Professores(as)"

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
