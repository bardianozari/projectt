from django.shortcuts import render
from . import models
# Create your views here.
def home(request):
    Info = models.Info.objects.first()
    Education = models.Education.objects.all()
    Career = models.Career.objects.all()
    Services = models.Services.objects.all()
    Customer = models.Customer.objects.all()
    Opinion = models.Opinion.objects.all()
    Plan = models.Plan.objects.all()
    Portfolio = models.Portfolio.objects.all()
    name = request.POST.get('name')
    email = request.POST.get('email')
    message = request.POST.get('message')
    if request.method == 'POST':
        models.Form.objects.create(name=name,email=email,message=message)
    return render(request,'home_app/index.html',{'Info':Info,
                                                 'Education':Education,
                                                 'Career':Career,
                                                 'Services':Services,
                                                 'Customer':Customer,
                                                 'Opinion':Opinion,
                                                 'Plan':Plan,
                                                 'Portfolio':Portfolio,})
def about(request):
    return render(request,'home_app/blog-post.html')