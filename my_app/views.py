from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Helloworld")

def about(request):
    return HttpResponse("about me")
def hello(request, first_name):
    return HttpResponse(f"hello {first_name}")

def add(request, num1,num2):
    return HttpResponse(f"the total is{num1+num2}")

