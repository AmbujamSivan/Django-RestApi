from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class HelloApiView(APIView):
    #To Test APIView

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
