# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework.views import APIView

from rest_framework.response import Response

from  . import serializers
from rest_framework import status
from rest_framework import viewsets



# Create your views here.

class HelloApiView(APIView):

    """Test API View"""

    serializers_class=serializers.HelloSerializer

    def get(self, request, format=None):
        """Returns a list a APIView features"""

        an_apiview=[
        'Uses HTTP methods as function (get, post, patch, put, delete)',
        'It is similar to a traditional Django view',
        'Its mapped manually to URLs'
        ]

        return Response({'message':"Hello",'an_apiview':an_apiview})


    def post(self,request):
        """Creates a hello message with our name"""
        serializer=serializers.HelloSerializer(data=request.data)
        if serializer.is_valid():
            name=serializer.data.get('name')
            message='Hello {0}'.format(name)
            return Response({"message":message})

        else:

            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk=None):
        """Handles updating an object."""
        return Response({'method':'put'})


    def patch(self,request,pk=None):
        """Patch request, only updates fields provided in the request"""
        return Response({'method':'patch'})


    def delete(self,request,pk=None):
        """Deletes an object."""

        return Response({'method'})


class HelloViewSet(viewsets.ViewSet):
    """Test API ViewSet."""

    serializer_class=serializers.HelloSerializer


    def list(self,request):
        a_viewset=[
        'Uses actions (list, create, retrieve, update, partial_update)',
        'Automatically maps to URLs using Routers',
        'Provides more functionality with less code'
        ]

        return Response({'message':'Hello!','a_viewset':a_viewset})


    def create(self, request):
        """Create a new hello message"""
        serializer=serializers.HelloSerializer(data=request.data)
        if serializer.is_valid():
            name=serializer.data.get('name')
            message='Hello {0}'.format(name)
            return Response({"message":message})
        else:

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self,request,pk=None):
        """Handles getting objects by its id"""

        return Response({'http_method':'GET'})

    def update(self,request,pk=None):#corresponds to the put http function
        '''Handles getting objects by its i'''
        return Response({'http_method':'PUT'})

    def partial_update(self,request,pk=None):
        """Handles updating part an object."""

        return Response({'http_method':'PATCH'})

    def destroy(self,request,pk=None):
        """Handles removing an object."""
        return Response({'http_method':'DELETE'})
