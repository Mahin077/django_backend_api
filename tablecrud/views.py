from django.shortcuts import render,HttpResponse
from tablecrud.models import Person
import json
from rest_framework import serializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from tablecrud.serializer import PersonSerializer
from django.db import connection


class PersonDetails(APIView):
    def get(self,request):
        obj = Person.objects.all()
        serializer = PersonSerializer(obj,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    

    # def post(self,request):
    #     serializer = PersonSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data,status=status.HTTP_201_CREATED)
    #     return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
    def post(self, request):
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            name = data['name']
            age = data['age']
        
            # Call the custom insert_person method to insert the data
            Person.insert_person(name, age)
        
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class PersonInfo(APIView):
    def get(self,request,id):
        try:
            obj = Person.objects.get(id=id)
        except Person.DoesNotExist:
            msg = {"msg":"not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        
        serializer = PersonSerializer(obj)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    def put(self,request,id):
        try:
            obj = Person.objects.get(id=id)
        except Person.DoesNotExist:
            msg={"msg":"not found"}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        
        serializer = PersonSerializer(obj,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,id):
        try:
            obj = Person.objects.get(id=id)
        except Person.DoesNotExist:
            msg={"msg":"not found"}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        
        serializer = PersonSerializer(obj,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id):
        try:
            obj = Person.objects.get(id=id)

        except Person.DoesNotExist:
            msg={"msg":"not found"}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        
        obj.delete()
        return Response({"msg":"deleted"},status=status.HTTP_204_NO_CONTENT)


