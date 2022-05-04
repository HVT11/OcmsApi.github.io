
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from OcmsApp.models import Accounts, Classes, Teachers, Students
from OcmsApp.serializers import AccountSerializer, TeacherSerializer, ClassSerializer, StudentSerializer

# Create your views here.
@csrf_exempt
def AccountApi(request, id=0):
    if request.method == 'GET':
        account = Accounts.objects.all()
        account_serializer = AccountSerializer(account, many = True)
        return JsonResponse(account_serializer.data, safe = False)
    elif request.method == 'POST':
        account_data = JSONParser().parse(request)
        account_serializer = AccountSerializer(data=account_data)
        if account_serializer.is_valid():
            account_serializer.save()
            return JsonResponse('Added to successfully', safe = False)
        return JsonResponse('Failed to add', safe=False)
    elif request.method == 'PUT':
        account_data = JSONParser().parse(request)
        account = Accounts.objects.get(Username = account_data['Username'])
        account_serializer = AccountSerializer(account, data=account_data)
        if account_serializer.is_valid():
            account_serializer.save()
            return JsonResponse('Updated to successfully', safe=False)
        return JsonResponse('Failed to update', safe=False)
    elif request.method == 'DELETE':
        account = Accounts.objects.get(AccountID = id)
        account.delete()
        return JsonResponse('Delete successfully',safe= False)


@csrf_exempt
def TeacherApi(request, id=0):
    if request.method == 'GET':
        teacher = Teachers.objects.all()
        teacher_serializer = TeacherSerializer(teacher, many = True)
        return JsonResponse(teacher_serializer.data, safe = False)
    elif request.method == 'POST':
        teacher_data = JSONParser().parse(request)
        teacher_serializer = TeacherSerializer(data=teacher_data)
        if teacher_serializer.is_valid():
            teacher_serializer.save()
            return JsonResponse('Added to successfully', safe = False)
        return JsonResponse('Failed to add', safe=False)
    elif request.method == 'PUT':
        teacher_data = JSONParser().parse(request)
        teacher = Teachers.objects.get(Username = teacher_data['Username'])
        teacher_serializer = TeacherSerializer(teacher, data=teacher_data)
        if teacher_serializer.is_valid():
            teacher_serializer.save()
            return JsonResponse('Updated to successfully', safe=False)
        return JsonResponse('Failed to update', safe=False)
    elif request.method == 'DELETE':
        teacher = Teachers.objects.get(TeacherID = id)
        teacher.delete()
        return JsonResponse('Delete successfully',safe= False)


@csrf_exempt
def ClassApi(request, id=0):
    if request.method == 'GET':
        classes = Classes.objects.all()
        class_serializer = ClassSerializer(classes, many = True)
        return JsonResponse(class_serializer.data, safe = False)
    elif request.method == 'POST':
        class_data = JSONParser().parse(request)
        class_serializer = ClassSerializer(data=class_data)
        if class_serializer.is_valid():
            class_serializer.save()
            return JsonResponse('Added to successfully', safe = False)
        return JsonResponse('Failed to add', safe=False)
    elif request.method == 'PUT':
        class_data = JSONParser().parse(request)
        classes = Classes.objects.get(ClassCode = class_data['ClassCode'])
        class_serializer = ClassSerializer(classes, data=class_data)
        if class_serializer.is_valid():
            class_serializer.save()
            return JsonResponse('Updated to successfully', safe=False)
        return JsonResponse('Failed to update', safe=False)
    elif request.method == 'DELETE':
        classes = Classes.objects.get(ClassID = id)
        classes.delete()
        return JsonResponse('Delete successfully',safe= False)

@csrf_exempt
def StudentApi(request, id=0):
    if request.method == 'GET':
        students = Students.objects.all()
        student_serializer = StudentSerializer(students, many = True)
        return JsonResponse(student_serializer.data, safe = False)
    elif request.method == 'POST':
        student_data = JSONParser().parse(request)
        student_serializer = StudentSerializer(data=student_data)
        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse('Added to successfully', safe = False)
        return JsonResponse('Failed to add', safe=False)
    elif request.method == 'PUT':
        student_data = JSONParser().parse(request)
        students = Students.objects.get(Username = student_data['Username'])
        student_serializer = StudentSerializer(students, data=student_data)
        if student_serializer.is_valid():
            student_serializer.save()
            return JsonResponse('Updated to successfully', safe=False)
        return JsonResponse('Failed to update', safe=False)
    elif request.method == 'DELETE':
        students = Students.objects.get(StudentID = id)
        students.delete()
        return JsonResponse('Delete successfully',safe= False)