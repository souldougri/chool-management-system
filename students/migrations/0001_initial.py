# Generated by Django 5.1.4 on 2025-01-04 22:45

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50, verbose_name='الاسم الأول')),
                ('last_name', models.CharField(max_length=50, verbose_name='اسم العائلة')),
                ('date_of_birth', models.DateField(verbose_name='تاريخ الميلاد')),
                ('gender', models.CharField(choices=[('M', 'ذكر'), ('F', 'أنثى')], max_length=1, verbose_name='الجنس')),
                ('address', models.TextField(verbose_name='العنوان')),
                ('phone_number', models.CharField(max_length=17, validators=[django.core.validators.RegexValidator(message='رقم الهاتف يجب أن يكون بالصيغة الصحيحة', regex='^\\+?1?\\d{9,15}$')], verbose_name='رقم الهاتف')),
                ('enrollment_date', models.DateField(auto_now_add=True, verbose_name='تاريخ التسجيل')),
                ('student_id', models.CharField(max_length=10, unique=True, verbose_name='رقم الطالب')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='student_photos/', verbose_name='الصورة الشخصية')),
            ],
            options={
                'verbose_name': 'طالب',
                'verbose_name_plural': 'الطلاب',
            },
        ),
        migrations.CreateModel(
            name='StudentCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_number', models.CharField(max_length=20, unique=True, verbose_name='رقم البطاقة')),
                ('issue_date', models.DateField(auto_now_add=True, verbose_name='تاريخ الإصدار')),
                ('expiry_date', models.DateField(verbose_name='تاريخ الانتهاء')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعالة')),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='students.student', verbose_name='الطالب')),
            ],
            options={
                'verbose_name': 'بطاقة طالب',
                'verbose_name_plural': 'بطاقات الطلاب',
            },
        ),
    ]
