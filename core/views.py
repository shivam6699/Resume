from django.shortcuts import render

# Create your views here.
from .models import * 

def index(request):
    about = About.objects.first()
    skills = Skills.objects.all()
    education = Education.objects.all()
    exp = Experience.objects.all()
    port = portfolio.objects.all()
    service = Service.objects.all()
    return render(request,'index.html',{'about':about,'skill':skills,'ed':education,'ex':Experience,'port':portfolio,'ser':service})

    
