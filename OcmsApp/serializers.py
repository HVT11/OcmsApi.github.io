from pyexpat import model
from rest_framework import serializers
from OcmsApp.models import Accounts, Teachers, Classes, Students, ListAttendance, Attendance

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        fields = ('AccountID', 'Username', 'Password', 'Type', 'DateCreate')

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teachers
        fields = ('TeacherID', 'Name', 'Email', 'Phone', 'Avatar', 'Username')

class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Classes
        fields = ('ClassID', 'ClassCode', 'ClassName', 'Schedule', 'TotalStu', 'DateCreate', 'TeacherID')

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = ('StudentID', 'Name', 'Gentle', 'StudentCode', 'DateOfBirth', 'Email', 'Avatar', 'Username', 'ClassID')

class ListAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ListAttendance
        fields = ('ListAttendanceID', 'Date', 'Time', 'Total', 'ClassID')

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ('AttendanceID', 'Username', 'Status', 'Note', 'ListAttendanceID')