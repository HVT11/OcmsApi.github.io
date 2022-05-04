from django.urls import path
from OcmsApp import views

urlpatterns = [
    path('account', views.AccountApi),
    path('account/<int:id>', views.AccountApi),

    path('teacher', views.TeacherApi),
    path('teacher/<int:id>', views.TeacherApi),
    
    path('class', views.ClassApi),
    path('class/<int:id>', views.ClassApi),

    path('student', views.StudentApi),
    path('student/<int:id>', views.StudentApi)
]