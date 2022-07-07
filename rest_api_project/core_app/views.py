from django.shortcuts import render
# Create your views here.

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins

from rest_framework import generics

from .serializers import Form
from .models import post_model

class secondview(mixins.ListModelMixin, 
                mixins.CreateModelMixin,
                 generics.GenericAPIView):
    serializer_class = Form
    queryset = post_model.objects.all()

    def get(self,request,*args, **kwargs):
        return self.list(self,request,*args, **kwargs)
    
    def post(self,request,*args, **kwargs):
        return self.create(request,*args, **kwargs)

class PostCreateView(mixins.ListModelMixin,generics.GenericAPIView):
    serializer_class = Form
    queryset = post_model.objects.all()

    def get(self,request,*args, **kwargs):
        return self.list(self,request,*args, **kwargs)

# class first_view(APIView):

#     permission_classes = (IsAuthenticated,)

#     def get(self,request,*args, **kwargs):
#         # data = {
#         #     'status': 200,
#         #     'desctiption':'This is an test view and it is running sucessfully',
#         # }
#         # return Response(data)
#         qs = post_model.objects.all()
#         post = qs.first()
#         serializers = Form(post)
#         # serializers = Form(qs,many = True)
#         return Response(serializers.data)    
    
#     def post(self,request,*args, **kwargs):
#         serializers = Form(data = request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data)
#         return Response(serializers.errors)