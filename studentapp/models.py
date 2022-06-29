from django.db import models

# Create your models here.

class StudentDetail(models.Model):
    application_no = models.BigAutoField(primary_key=True)
    student_name = models.CharField(max_length=50)
    father_name = models.CharField(max_length=50)
    mother_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=500)

    def __str__(self):
        return str(self.student_name)

class LoginDetail(models.Model):
    email = models.ForeignKey(StudentDetail, to_field='email', on_delete=models.CASCADE)
    password = models.CharField(max_length=10)

class AcademicsDetail(models.Model):
    application_no = models.ForeignKey(StudentDetail, on_delete=models.CASCADE)
    student_id = models.BigAutoField(primary_key=True)
    higher_secondary_school_marks = models.PositiveIntegerField()
    higher_secondary_school_name = models.CharField(max_length=200)
    secondary_school_marks = models.PositiveIntegerField()
    secdondary_school_name = models.CharField(max_length=200)

    def __str__(self):
        return ('Student id '+ str(self.application_no))

class AdmitStudent(models.Model):
    student_id = models.ForeignKey(to=AcademicsDetail, on_delete=models.CASCADE)
    roll_no = models.AutoField(primary_key=True)
    course = models.CharField(max_length=50)
    section = models.CharField(max_length=10)

    def __str__(self):
        return ('Roll no '+ str(self.roll_no))