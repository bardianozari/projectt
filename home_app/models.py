from django.db import models

# Create your models here.
class Info(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    job = models.CharField(max_length=100)
    telegram = models.URLField(max_length=100)
    instagram = models.URLField(max_length=100)
    facebook = models.URLField(max_length=100)
    twitter = models.URLField(max_length=100)
    age = models.IntegerField(null=True)
    img = models.ImageField(null=True,upload_to='img')
    def __str__(self):
        return self.name
class Education(models.Model):
    education1 = models.CharField(max_length=100)
    education1year = models.CharField(max_length=100,null=True)
    education1company = models.CharField(max_length=100,null=True)
    education1detail = models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.education1
class Career(models.Model):
    career1 = models.CharField(max_length=100)
    within = models.CharField(max_length=100,null=True)
    company =models.CharField(max_length=100,null=True)
    deatil = models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.career1
class Services(models.Model):
    service1 = models.CharField(max_length=100)
    img = models.ImageField(upload_to='services/img')
    detail = models.CharField(max_length=100,null=True)

    def __str__(self):
        return self.service1
class Customer(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='customer/img')
    def __str__(self):
        return self.name
class Opinion(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='opinion/img')
    job = models.CharField(max_length=100)
    detail = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Plan(models.Model):
    price = models.CharField(max_length=100)
    one = models.CharField(max_length=100)
    two = models.CharField(max_length=100)
    three = models.CharField(max_length=100)
    def __str__(self):
        return self.one
class Form(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Portfolio(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='portfolio/img')
    type = models.CharField(max_length=100)
    date = models.DateField(null=True)
    detail = models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.name
