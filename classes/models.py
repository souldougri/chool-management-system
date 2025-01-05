from django.db import models
from students.models import Student

class ClassRoom(models.Model):
    name = models.CharField(max_length=50, verbose_name="اسم الفصل")
    capacity = models.IntegerField(verbose_name="السعة")
    grade_level = models.CharField(max_length=20, verbose_name="المستوى الدراسي")
    academic_year = models.CharField(max_length=9, verbose_name="السنة الدراسية")
    students = models.ManyToManyField(Student, related_name='classes', verbose_name="الطلاب")
    
    class Meta:
        verbose_name = "فصل دراسي"
        verbose_name_plural = "الفصول الدراسية"
    
    def __str__(self):
        return f"{self.name} - {self.grade_level}"

class Subject(models.Model):
    name = models.CharField(max_length=100, verbose_name="اسم المادة")
    code = models.CharField(max_length=10, unique=True, verbose_name="رمز المادة")
    description = models.TextField(verbose_name="وصف المادة")
    credit_hours = models.IntegerField(verbose_name="الساعات المعتمدة")
    
    class Meta:
        verbose_name = "مادة دراسية"
        verbose_name_plural = "المواد الدراسية"
    
    def __str__(self):
        return self.name

class TeacherProfile(models.Model):
    first_name = models.CharField(max_length=50, verbose_name="الاسم الأول")
    last_name = models.CharField(max_length=50, verbose_name="اسم العائلة")
    email = models.EmailField(unique=True, verbose_name="البريد الإلكتروني")
    phone_number = models.CharField(max_length=17, verbose_name="رقم الهاتف")
    subjects = models.ManyToManyField(Subject, related_name='teachers', verbose_name="المواد التي يدرسها")
    classes = models.ManyToManyField(ClassRoom, related_name='teachers', verbose_name="الفصول التي يدرسها")
    
    class Meta:
        verbose_name = "معلم"
        verbose_name_plural = "المعلمون"
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
