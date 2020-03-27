from django.shortcuts import render
from .models import Certificates

def certificates(request):
    certificates = Certificates.objects
    return render(request,'certificates/certificates.html',{'certificates':certificates})

def addcerti(request):
    return render(request,'certificates/addcerti.html')

def certiadded(request):
    if request.method == 'POST':
        name_c = request.POST.get('name')
        org_c = request.POST.get('org')
        date_c = request.POST.get('date')
        link_c = request.POST.get('link')
        c = Certificates(name=name_c,org=org_c,date=date_c,link=link_c)
        c.save()
        return render(request,'certificates/certiadded.html',{'name':name_c})
    else:
        return render(request,'certificates/addcerti.html')

# Create your views here.
