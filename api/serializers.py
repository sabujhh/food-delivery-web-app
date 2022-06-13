from rest_framework import serializers
from customer.models import MenuItem


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem
        fields = (
            'name', 
            'description'
        )