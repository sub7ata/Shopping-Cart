from django.db import models
from django.utils.timezone import datetime
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=120)
    price = models.IntegerField()

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-id']



class Cart(models.Model):
	name = models.CharField(max_length=120)
	price = models.IntegerField()
	product = models.ForeignKey('Product',on_delete=models.SET_NULL, null=True)
	created_by = models.ForeignKey('auth.User', on_delete=models.SET_NULL, null=True)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['-id']