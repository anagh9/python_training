from django.shortcuts import render
from .models import Restaurant,Review
# Create your views here.

def home(request):
    return render(request,'home.html',{'title':"Home"})