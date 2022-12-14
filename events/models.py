from datetime import datetime
from time import timezone
from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

# Create your models here.

class MyClubUser(models.Model):
    first_name = models.CharField('User First Name', max_length=64, null=False)
    last_name = models.CharField('User Last Name', max_length=64, null= False)
    email =models.EmailField('User Email', max_length=64)

    def __str__(self):
        return self.first_name + ' ' + self.last_name



class Venue(models.Model):
    name = models.CharField('Venue Name', max_length=64)
    address = models.CharField('Venue Address', max_length=128)
    zip_code =models.CharField('Venue Zip Code', max_length=5)
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    phoneNumber = models.CharField(validators = [phoneNumberRegex], max_length = 16, unique = True, null=True)
    web = models.URLField('Website Address')
    email =models.EmailField('Email Address', max_length=64)
    
   
    def __str__(self):
        return self.name




class Event(models.Model):
    name = models.CharField('Event Name', max_length=64, blank= False, null= False)
    date = models.DateTimeField('Event Date', blank=False, null= False)
    manager = models.ForeignKey(User,blank = False, on_delete=models.PROTECT,related_name="user_creator")
    description =models.TextField(blank=True)
    attendees = models.ManyToManyField(MyClubUser, blank = True,related_name="attendees")
    venue = models.ForeignKey(Venue, blank= False, null=False, on_delete=models.PROTECT,related_name="event_place")

    def __str__(self):
        return self.name