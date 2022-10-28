from django.shortcuts import render
from .models import *
from django.core import serializers
from django.core.exceptions import PermissionDenied
# Create your views here.
def home(request):
    urls=[]
    context=[]
    if request.user.is_authenticated:
        urls= Url.objects.all()
    print(urls)

    return render(request,'home.html',{"urls": serializers.serialize("json", Url.objects.all())})

def forbidden(request):
    raise PermissionDenied()