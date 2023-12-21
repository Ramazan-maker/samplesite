from django.db import models
from django.contrib.auth.models import User



class AdvUser(models.Model):
    is_activated = models.BooleanField(default=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

class Spare(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name}"

class Machine(models.Model):
    name = models.CharField(max_length=30)
    spares = models.ManyToManyField(Spare)

    def __str__(self):
        return f"{self.name}"



class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    occupation = models.CharField(max_length=100)

class Child(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE, primary_key=True)
    toys = models.ManyToManyField('Toy')

class Parent(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    occupation = models.CharField(max_length=100)

class IceCream(models.Model):
    flavor = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    kiosk = models.ForeignKey('IceCreamKiosk', on_delete=models.CASCADE)

class IceCreamKiosk(models.Model):
    location = models.CharField(max_length=100)
    owner = models.ForeignKey(Person, on_delete=models.CASCADE)
    ice_creams = models.ManyToManyField(IceCream)

class Toy(models.Model):
    name = models.CharField(max_length=50)
    suitable_age = models.IntegerField()
    owner = models.ForeignKey(Child, on_delete=models.CASCADE)
