from django.db import models
from django.core.validators import RegexValidator

class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'ذكر'),
        ('F', 'أنثى'),
    ]
    
    first_name = models.CharField(max_length=50, verbose_name="الاسم الأول")
    last_name = models.CharField(max_length=50, verbose_name="اسم العائلة")
    date_of_birth = models.DateField(verbose_name="تاريخ الميلاد")
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="الجنس")
    address = models.TextField(verbose_name="العنوان")
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="رقم الهاتف يجب أن يكون بالصيغة الصحيحة"
    )
    phone_number = models.CharField(
        validators=[phone_regex],
        max_length=17,
        verbose_name="رقم الهاتف"
    )
    enrollment_date = models.DateField(auto_now_add=True, verbose_name="تاريخ التسجيل")
    student_id = models.CharField(max_length=10, unique=True, verbose_name="رقم الطالب")
    photo = models.ImageField(upload_to='student_photos/', null=True, blank=True, verbose_name="الصورة الشخصية")
    
    class Meta:
        verbose_name = "طالب"
        verbose_name_plural = "الطلاب"
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class StudentCard(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, verbose_name="الطالب")
    card_number = models.CharField(max_length=20, unique=True, verbose_name="رقم البطاقة")
    issue_date = models.DateField(auto_now_add=True, verbose_name="تاريخ الإصدار")
    expiry_date = models.DateField(verbose_name="تاريخ الانتهاء")
    is_active = models.BooleanField(default=True, verbose_name="فعالة")
    
    class Meta:
        verbose_name = "بطاقة طالب"
        verbose_name_plural = "بطاقات الطلاب"
    
    def __str__(self):
        return f"بطاقة {self.student.first_name} {self.student.last_name}"
