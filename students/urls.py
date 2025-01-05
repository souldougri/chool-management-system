from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('', views.StudentListView.as_view(), name='list'),
    path('<int:pk>/', views.StudentDetailView.as_view(), name='detail'),
    path('add/', views.StudentCreateView.as_view(), name='create'),
    path('<int:pk>/edit/', views.StudentUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.StudentDeleteView.as_view(), name='delete'),
    path('<int:student_id>/generate-card/', views.generate_student_card, name='generate_card'),
]
