from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html
from .models import Student, StudentCard

# Register your models here.

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'first_name', 'last_name', 'gender', 'print_actions')
    list_filter = ('gender',)
    search_fields = ('student_id', 'first_name', 'last_name')
    change_list_template = 'admin/students/student/change_list.html'
    
    def print_actions(self, obj):
        card_url = reverse('print_student_card', args=[obj.id])
        cert_url = reverse('print_certificate', args=[obj.id])
        return format_html(
            '<a class="button" href="{}" target="_blank">طباعة البطاقة</a>&nbsp;'
            '<a class="button" href="{}" target="_blank">طباعة الشهادة</a>',
            card_url, cert_url
        )
    print_actions.short_description = 'طباعة'

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['print_list_url'] = reverse('print_student_list')
        return super().changelist_view(request, extra_context=extra_context)
    
    class Media:
        css = {
            'all': ('admin/css/print_buttons.css',)
        }

@admin.register(StudentCard)
class StudentCardAdmin(admin.ModelAdmin):
    list_display = ('student', 'issue_date', 'expiry_date')
    list_filter = ('issue_date', 'expiry_date')
    search_fields = ('student__first_name', 'student__last_name')
