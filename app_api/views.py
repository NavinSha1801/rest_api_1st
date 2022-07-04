from django.shortcuts import render

#added manually on 04-07-2022 00:33
from django.http import JsonResponse
from .serializers import myserializer
from .models import Post

#third parties input
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
def json_response_view(request):
    data = {
        'status':200,
        'description':'OK'
    }
    return JsonResponse(data)

class TestView(APIView):
    def get(self,request,*args, **kwargs):
        data = Post.objects.all()
        serializer = myserializer(data,many = True)
        return JsonResponse(serializer.data )

    # def post(self,request,*args, **kwargs):
    #     data0 = {
    #         'status':500,
    #         'description':'Internal server error',
    #         'Test View': ' checking'
    #     }

    def post(self,request,*args, **kwargs):
        serializer = myserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
