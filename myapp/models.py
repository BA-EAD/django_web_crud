from django.db import models

# Create your models here.
class Registr(models.Model):
	"""docstring for Registrations"""
	first_name = models.TextField(max_length=20)
	last_name = models.TextField(max_length=20)
	email = models.EmailField(max_length=254)
	mobile = models.TextField(max_length=15)
	image = models.ImageField(upload_to = 'pic_folder/', default="")
