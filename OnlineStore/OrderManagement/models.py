from django.db import models

# Create your models here.
class Clients( models.Model ):
    name    = models.CharField( max_length = 30 )
    address = models.CharField( max_length = 30 )
    email   = models.EmailField()
    phone   = models.CharField( max_length = 7 )

    def __str__(self):
        return f'Name : { self.name } address: { self.section } email: { self.price } phone: { self.phone }'


class Items( models.Model ):
    name    = models.CharField( max_length = 30 )
    section = models.CharField( max_length = 20 )
    price   = models.IntegerField()

    def __str__(self):
        return f'Name : { self.name } Section: { self.section } Price: { self.price }'


class Orders( models.Model ):
    number      = models.IntegerField()
    date        = models.DateField()
    email       = models.EmailField()
    delivered   = models.BooleanField()

    def __str__(self):
        return f'number : { self.number } date: { self.date } email: { self.email } delivered: {self.delivered}'