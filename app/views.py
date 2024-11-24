from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'app/index.html')
def logout_view(request):
    return render(request,'/')