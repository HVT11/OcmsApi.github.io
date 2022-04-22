from rest_framework import serializers
from OcmsApp.models import Accounts

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accounts
        fields = ('AccountID', 'Username', 'Password', 'Type')
