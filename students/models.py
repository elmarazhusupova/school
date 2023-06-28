from django.db import models
from user.models import Teacher


class Student(models.Model):
    GENDER_CHOICES = (
        ('M', 'Мужской'),
        ('F', 'Женский'),
        ('O', 'Другой'),
    )
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    birth_date = models.DateField()
    grade = models.ForeignKey('Grade', related_name='student_grade', on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    gender = models.CharField(max_length=200, choices=GENDER_CHOICES)
    image = models.ImageField(upload_to='student/image/', blank=True, null=True)

    def __str__(self):
        return self.full_name


class School(models.Model):
    name = models.CharField(max_length=150)
    grade = models.ForeignKey('Grade', related_name='school', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Grade(models.Model):
    name = models.CharField(max_length=10)
    teacher = models.OneToOneField('user.Teacher', related_name='teacher', on_delete=models.CASCADE, blank=True, null=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='student', blank=True, null=True)

    def __str__(self):
        return self.name
