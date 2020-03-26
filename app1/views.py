from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact

def home(request):
    return render(request,'app1/home.html')

def portfolio(request):
    return render(request,'app1/portfolio.html')

def contact(request):
    return render(request,'app1/contact.html')



def success(request):
    if request.method == 'POST':
        name_f = request.POST.get('name')
        email_f = request.POST.get('email')
        message_f = request.POST.get('message')
        c = Contact(name=name_f, email=email_f, message=message_f)
        c.save()
        return render(request,'app1/success.html',{'name':name_f})
    else:
        return render(request,'app1/contact.html')


# Create your views here.
