from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Student, StudentCard
from .forms import StudentForm, StudentCardForm

class StudentListView(ListView):
    model = Student
    template_name = 'students/student_list.html'
    context_object_name = 'students'
    paginate_by = 10

class StudentDetailView(DetailView):
    model = Student
    template_name = 'students/student_detail.html'
    context_object_name = 'student'

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/student_form.html'
    success_url = reverse_lazy('students:list')

    def form_valid(self, form):
        messages.success(self.request, 'تم إضافة الطالب بنجاح')
        return super().form_valid(form)

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'students/student_form.html'
    success_url = reverse_lazy('students:list')

    def form_valid(self, form):
        messages.success(self.request, 'تم تحديث بيانات الطالب بنجاح')
        return super().form_valid(form)

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'students/student_confirm_delete.html'
    success_url = reverse_lazy('students:list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, 'تم حذف الطالب بنجاح')
        return super().delete(request, *args, **kwargs)

def generate_student_card(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        form = StudentCardForm(request.POST)
        if form.is_valid():
            card = form.save(commit=False)
            card.student = student
            card.save()
            messages.success(request, 'تم إصدار البطاقة المدرسية بنجاح')
            return redirect('students:detail', pk=student_id)
    else:
        form = StudentCardForm()
    
    return render(request, 'students/generate_card.html', {
        'form': form,
        'student': student
    })
