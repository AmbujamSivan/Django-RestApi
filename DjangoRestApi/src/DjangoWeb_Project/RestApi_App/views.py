from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from . import serializer
from . import models

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

class HelloViewSets(viewsets.ViewSet):
    """To Explain viewsets"""
    # def __init__(self, arg):
    #     super(, self).__init__()
    #     self.arg = arg
    serializer_class = serializer.HelloSerializer

    def list(self, request):
        """Returns a Hello message"""

        aViewset=[
            'Uses the Actions: List, Create, Retrive, Update, Partial_Update',
            'Automatic mapping of urls by the Router',
            'Provides more functionality with less code'
        ]
        return Response({'message':'Hello', 'aViewset':aViewset})

    def create(self, request):
        """create a new hello message"""
        serialized = serializer.HelloSerializer(data = request.data)

        if serialized.is_valid():
            name = serialized.data.get('name')
            message = 'Hello {0}, from ViewSet'.format(name)
            return Response({'message':message})
        else:
            return Response(serialized.errors, status = status.HTTP_400_BAD_REQUEST)


    def retrieve(self, request, pk = None):
        """gets the object by its id from DB"""
        return Response({'http_method':'GET'})

    def update(self, request, pk = None):
        """updates the object by its id in DB"""
        return Response({'http_method':'PUT'})

    def partial_update(self, request, pk = None):
        """partial updation of object by its ID in DB"""
        return Response({'http_method':'PATCH'})

    def destroy(self, request, pk = None):
        """deletes the object by its ID in DB"""
        return Response({'http_method':'DELETE'})

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating and updating a user UserProfile"""
    serializer_class = serializer.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
