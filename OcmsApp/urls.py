from django.urls import path
from OcmsApp import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('account', views.AccountApi),
    path('account/<int:id>', views.AccountApi),

    path('teacher', views.TeacherApi),
    path('teacher/<int:id>', views.TeacherApi),
    
    path('class', views.ClassApi),
    path('class/<int:id>', views.ClassApi),

    path('student', views.StudentApi),
    path('student/<int:id>', views.StudentApi),

    path('listattendance', views.ListAttendanceApi),
    path('listattendance/<int:id>', views.ListAttendanceApi),

    path('attendance', views.AttendanceApi),
    path('attendance/<int:id>', views.AttendanceApi),

    path('student/savefile', views.SaveFile)
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)