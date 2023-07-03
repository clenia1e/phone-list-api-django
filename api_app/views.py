from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserItemSerializer
from .models import UserItem
from django.shortcuts import get_object_or_404

class UserItemsViews(APIView):
    def post(self, request):
        serializer = UserItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAB_REQUEST)

    def get(self, request, id=None):
        if id:
            item = UserItem.objects.get(id=id)
            serializer = UserItemSerializer(item)
            return Response({"status": "sucess", "data": serializer.data}, status=status.HTTP_200_OK)
        items = UserItem.objects.all()
        serializer = UserItemSerializer(items, many=True)
        return Response({"status": "sucess", "data": serializer.data}, status=status.HTTP_200_OK)
    
    def patch(self, request, id=None):
        item = UserItem.objects.get(id=id)
        serializer = UserItemSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})  
        
    def delete(self, request, id=None):
        item = get_object_or_404(UserItem, id=id)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})
