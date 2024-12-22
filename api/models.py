from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator,MinLengthValidator
from phonenumber_field.modelfields import PhoneNumberField

class Service_Type(models.Model):
    type = models.CharField(max_length=50)


    def __str__(self):
        return self.type

class Field(models.Model):
    First_Name = models.CharField(max_length=20)
    Middle_Name = models.CharField(max_length=20)
    Last_Name = models.CharField(max_length=20)
    Email = models.EmailField()
    Phone_Number = PhoneNumberField(null=False, blank=False)
    Service_Type = models.ForeignKey(Service_Type, on_delete=models.CASCADE)
    Location = models.CharField(max_length=50,validators=[MinLengthValidator(2)])
    details = models.TextField()
    terms1 = models.BooleanField()
    terms2 = models.BooleanField()
    terms3 = models.BooleanField()
    
    
    def __str__(self):
        return self.First_Name