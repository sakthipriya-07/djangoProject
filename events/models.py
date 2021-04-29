from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser


class User(AbstractUser):
    is_patient = models.BooleanField(default=False)
    phone = models.CharField(max_length=20, null=False)


GRAD, UNDER_GRAD = range(2)

PROGRAM = ((GRAD, 'GRAD'),(UNDER_GRAD,'UNDER_GRAD')
)



ISQA_3900, ISQA_8040, ISQA_8210, ISQA_8220, ISQA_3900, ISQA_8420, ISQA_8410 = range(7)
COURSES = (
    (ISQA_3900, 'ISQA_8410'),
    (ISQA_8040, 'ISQA_3900'),
    (ISQA_8210, 'ISQA_8210'),
    (ISQA_8220, 'ISQA_8420'),
    (ISQA_3900, 'ISQA_8220'),
    (ISQA_8420, 'ISQA_8040'),
    (ISQA_8420, 'ISQA_8420'),
)


class Student(models.Model):
    full_name = models.CharField('Full Name', max_length=50)
    program = models.PositiveSmallIntegerField('program', choices=PROGRAM, default='')
    courses = models.PositiveSmallIntegerField('courses', choices=COURSES, default='')
    grades = models.CharField('Grades', max_length=2)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = ('Student')
