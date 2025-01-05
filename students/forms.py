from django import forms
from .models import Student, StudentCard
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'date_of_birth', 'gender', 
                 'address', 'phone_number', 'student_id', 'photo']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('first_name', css_class='form-group col-md-6'),
                Column('last_name', css_class='form-group col-md-6'),
            ),
            Row(
                Column('date_of_birth', css_class='form-group col-md-6'),
                Column('gender', css_class='form-group col-md-6'),
            ),
            'address',
            Row(
                Column('phone_number', css_class='form-group col-md-6'),
                Column('student_id', css_class='form-group col-md-6'),
            ),
            'photo',
            Submit('submit', 'حفظ', css_class='btn btn-primary')
        )

class StudentCardForm(forms.ModelForm):
    class Meta:
        model = StudentCard
        fields = ['card_number', 'expiry_date']
        widgets = {
            'expiry_date': forms.DateInput(attrs={'type': 'date'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'card_number',
            'expiry_date',
            Submit('submit', 'إصدار البطاقة', css_class='btn btn-primary')
        )
