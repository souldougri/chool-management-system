from django.contrib import admin
from .models import Grade, Certificate

# Register your models here.

@admin.register(Grade)
class GradeAdmin(admin.ModelAdmin):
    list_display = ('student', 'subject', 'grade', 'semester')
    list_filter = ('semester', 'subject')
    search_fields = ('student__first_name', 'student__last_name', 'subject__name')

@admin.register(Certificate)
class CertificateAdmin(admin.ModelAdmin):
    list_display = ('student', 'issue_date', 'grade_level')
    list_filter = ('grade_level', 'issue_date')
    search_fields = ('student__first_name', 'student__last_name')
