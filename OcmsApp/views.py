from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from OcmsApp.models import Accounts
from OcmsApp.serializers import AccountSerializer

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
        account = Accounts.objects.get(DepartmentId = id)
        account.delete()
        return JsonResponse('Delete successfully',safe= False)