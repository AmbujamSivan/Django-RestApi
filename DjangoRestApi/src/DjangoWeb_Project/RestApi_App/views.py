from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializer

# Create your views here.
class HelloApiView(APIView):
    #To Test APIView
    """Tells taht we are going to use this helloserializer for this APIView"""
    serializer_class = serializer.HelloSerializer

    def get(self, request, format=None):
        """Return the list of API features"""
        an_apiview = [
        'Its similar to the traditional Django Views but',
        'Uses Http methods as function (get,post,put,delete,pathch)',
        'It is mapped manually to the urls',
        'Gives you the most control over the logics'
        ]
        #Response Objj should be returned as a Dictionary which is then converted to JSON
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Returns a variable of our name"""

        serialized = serializer.HelloSerializer(data = request.data)

        if serialized.is_valid():
            name = serialized.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message':message})
        else:
            return Response(serialized.errors, status = status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        """ performs Update functionality"""
        return Response({'method':'put'})

    def patch(self, request, pk = None):
        """ partial updation of the object only those provided in the req"""
        return Response({'method':'patch'})

    def delete(self, request, pk = None):
        """Perfors the deletion of object"""
        return Response({'method':'delete'})
