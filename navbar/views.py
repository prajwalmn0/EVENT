from http.client import HTTPResponse
from re import X
from django.shortcuts import render,HttpResponse

# Create your views here.
def home(request):
    return render(request,'index.html')