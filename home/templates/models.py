from django.db import models

# Create your models here
class ClassName(object):
	nombre = models.CharField(max_length=50)

	def __str__(self):
		return self.nombre



class Producto(models.Model):
	nombre = models.CharField(max_length=50)
	llaveforanea= models.ForeignKey(Marca, on_delete=models.PROTECT)

	def __str__(self):
		return self.nombre