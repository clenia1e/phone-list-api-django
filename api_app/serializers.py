from rest_framework import serializers
from phone_field import PhoneField
from .models import UserItem


class UserItemSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(max_length=10)
    user_last_name = serializers.CharField(max_length=10)
    user_number = PhoneField(blank=True, help_text='Contact phone number')

    class Meta:
        model = UserItem
        fields = ('__all__')