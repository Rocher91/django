from django.db import models

# Create your models here.
class Clients( models.Model ):
    name    = models.CharField( max_length = 30 )
    address = models.CharField( max_length = 50, verbose_name="The address" )
    email   = models.EmailField(blank=True,null=True)
    phone   = models.CharField( max_length = 7 )

    def __str__(self):
        return f'{ self.name }'


class Items( models.Model ):
    name    = models.CharField( max_length = 30 )
    section = models.CharField( max_length = 20 )
    price   = models.IntegerField()

    def __str__(self):
        return f'Name : { self.name } Section: { self.section } Price: { self.price }'


class Orders( models.Model ):
    num         = models.IntegerField()
    date        = models.DateField()
    email       = models.EmailField()
    delivered   = models.BooleanField()

