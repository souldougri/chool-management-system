from django.db import models
from students.models import Student
from classes.models import Subject, ClassRoom

# Create your models here.

class Grade(models.Model):
    GRADE_CHOICES = [
        ('A', 'ممتاز'),
        ('B', 'جيد جداً'),
        ('C', 'جيد'),
        ('D', 'مقبول'),
        ('F', 'راسب'),
    ]
    
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="الطالب")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name="المادة")
    class_room = models.ForeignKey(ClassRoom, on_delete=models.CASCADE, verbose_name="الفصل")
    grade = models.CharField(max_length=1, choices=GRADE_CHOICES, verbose_name="الدرجة")
    score = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="النتيجة")
    semester = models.CharField(max_length=20, verbose_name="الفصل الدراسي")
    academic_year = models.CharField(max_length=9, verbose_name="السنة الدراسية")
    
    class Meta:
        verbose_name = "درجة"
        verbose_name_plural = "الدرجات"
        unique_together = ['student', 'subject', 'semester', 'academic_year']
    
    def __str__(self):
        return f"{self.student} - {self.subject} - {self.grade}"

class Certificate(models.Model):
    CERTIFICATE_TYPES = [
        ('semester', 'شهادة فصلية'),
        ('yearly', 'شهادة سنوية'),
        ('graduation', 'شهادة تخرج'),
    ]
    
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="الطالب")
    certificate_type = models.CharField(max_length=20, choices=CERTIFICATE_TYPES, verbose_name="نوع الشهادة")
    issue_date = models.DateField(auto_now_add=True, verbose_name="تاريخ الإصدار")
    academic_year = models.CharField(max_length=9, verbose_name="السنة الدراسية")
    grade_level = models.CharField(max_length=20, verbose_name="المستوى الدراسي")
    gpa = models.DecimalField(max_digits=3, decimal_places=2, verbose_name="المعدل التراكمي")
    certificate_number = models.CharField(max_length=20, unique=True, verbose_name="رقم الشهادة")
    
    class Meta:
        verbose_name = "شهادة"
        verbose_name_plural = "الشهادات"
    
    def __str__(self):
        return f"شهادة {self.get_certificate_type_display()} - {self.student}"
