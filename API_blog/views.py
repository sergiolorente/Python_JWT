from django.shortcuts import render
from django.urls import reverse_lazy
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from .models import Ciudad
from .serializer import PostCiudad
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_jwt import authentication
from rest_framework import permissions,viewsets
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework import generics
from django.http import Http404

# Create your views here.


class CiudadesListAPIView(ListAPIView):
    serializer_class = PostCiudad
    permission_classes = [IsAuthenticated]
    #authentication_classes = [JWTAuthentication]
    #authentication_classes = [authentication.JSONWebTokenAuthentication]

    def get_queryset(self):
        query = Ciudad.objects.all()
        return query


class tabla(viewsets.ModelViewSet):
    queryset = Ciudad.objects.all()
    serializer_class = PostCiudad
    #permission_classes = [permissions.IsAuthenticated]
    #authentication_classes = [JSONWebTokenAuthentication]



def table3(request):
    return render(request, 'API_blog/table3.html')

class table2(generics.ListAPIView):
    serializer_class = PostCiudad
    authentication_classes = [authentication.JSONWebTokenAuthentication]
    #permission_classes = [permissions.IsAuthenticated]


    def perform_authentication(self, request):
        print ('HOLA')
        print(request.user)

    def get_queryset(self):
        params = self.request.query_params
        if params:
            print (params)
            try:
                title = params["title"]
                query = Ciudad.objects.filter(title__icontains=title)
                if query:
                    return query
                else:
                    raise Http404("PAS D'ELEMENTS")
            except:
                return Ciudad.objects.all()
        else:
            return Ciudad.objects.all()


