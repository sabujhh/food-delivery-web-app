from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView


from .serializers import MenuItemSerializer
from customer.models import MenuItem

# Create your views here.
class TestView(APIView):
    def get(self, request, *args, **kwargs):
        qs = MenuItem.objects.all()
        #post = qs.first()
        serializer = MenuItemSerializer(qs, many=True)
        #serializer = PostSerializer(post)
        return Response(serializer.data)

