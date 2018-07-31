from django.db import models
from django.contrib.auth.models import User

class SubsciptionTable(models.Model):
    email=models.CharField(max_length=300)
    def __str__(self):
        return self.email

class Store(models.Model):
    product_logo=models.CharField(max_length=500)
    product_name=models.CharField(max_length=300)
    product_price=models.FloatField()

    def __str__(self):
        return self.product_name

class Diet(models.Model):
    breakfast_logo=models.CharField(max_length=500)
    breakfast=models.CharField(max_length=2200)
    lunch_logo=models.CharField(max_length=500)
    lunch=models.CharField(max_length=2200)
    dinner_logo=models.CharField(max_length=500)
    dinner=models.CharField(max_length=2200)

class UserProfileInfo(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    portfolio_site=models.URLField(blank=True)
    profile_pic=models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username








