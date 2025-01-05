from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
from students.models import Student
from classes.models import ClassRoom, TeacherProfile
from certificates.models import Certificate
from datetime import date

def home(request):
    context = {
        'total_students': Student.objects.count(),
        'total_classes': ClassRoom.objects.count(),
        'total_teachers': TeacherProfile.objects.count(),
    }
    return render(request, 'home.html', context)

def print_student_card(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    context = {
        'student': student,
        'print_date': date.today(),
    }
    html_string = render_to_string('print/student_card.html', context)
    html = HTML(string=html_string, base_url=request.build_absolute_uri('/'))
    pdf = html.write_pdf()
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'filename=student_card_{student.student_id}.pdf'
    return response

def print_certificate(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    context = {
        'student': student,
        'print_date': date.today(),
    }
    html_string = render_to_string('print/certificate.html', context)
    html = HTML(string=html_string, base_url=request.build_absolute_uri('/'))
    pdf = html.write_pdf()
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = f'filename=certificate_{student.student_id}.pdf'
    return response

def print_student_list(request):
    students = Student.objects.all().order_by('classes', 'first_name')
    context = {
        'students': students,
        'print_date': date.today(),
    }
    html_string = render_to_string('print/student_list.html', context)
    html = HTML(string=html_string, base_url=request.build_absolute_uri('/'))
    pdf = html.write_pdf()
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'filename=student_list.pdf'
    return response
