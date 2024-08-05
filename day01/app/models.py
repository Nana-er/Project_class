from django.db import models

# Create your models here.
class category (models.Model):
    name = models.CharField(max_length = 20)
     
def __str__(self):
    return self.name

class unit (models.Model):
    name = models.CharField(max_length = 20)
     
def __str__(self):
    return self.name
        
class item (models.Model):
    name = models.CharField(max_length = 20)
    price = models.DecimalField(max_digits= 8, decimal_places = 2)
    image = models.ImageField(upload_to='item')
    category = models.ForeignKey (category, on_delete= models.CASCADE)
    unit = models.ForeignKey(unit, on_delete= models.CASCADE)

def __str__(self):
    return self.name
        
class supplier (models.Model):
    name = models.CharField(max_length= 20)
    mobileno = models.CharField(max_length= 10)
    item = models.ManyToManyField(item)

def __str__(self):
    return self.name

class Order (models.Model):
    customer = models.CharField(max_length= 20)
    date = models.DateField()
    item = models.ManyToManyField(item)

def __str__(self):
    return self.customer          

class Employee (models.Model):
    name = models.CharField(max_length = 20)
     
def __str__(self):
    return self.name

class Book (models.Model):
    name = models.CharField(max_length = 20)
     
def __str__(self):
    return self.name