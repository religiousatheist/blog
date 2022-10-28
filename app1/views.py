from multiprocessing import context
from django.shortcuts import render,HttpResponse
from datetime import datetime
from app1.models import Contact
def home(request):
    context={'variable1':'1233dsdfnlnbvoirjfd',
             'variable2':'!@#$%^&&&&*()_}'}
    return render(request,'index.html')
    #return HttpResponse('THIS IS HOME')

def about(request):
    #return HttpResponse('THIS IS ABOUT SECTION !@#$$%^%&%$%$!')
    return render(request,'about.html')
def products(request):
    #return HttpResponse('THE PRODUCT SECTION')
    return render(request,'products.html')
def contact(request):
    #return HttpResponse('CONTACT AT-9599637513')
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        question=request.POST.get('question')
        contact=Contact(name=name,email=email,question=question,date=datetime.today())
        contact.save()

    return render(request,'contact.html')
def part1(request):
    return render(request,'part1.html')
def god(request):
    return render(request,'god.html')
def science(request):
    return render(request,'science.html')
# Create your views here.
