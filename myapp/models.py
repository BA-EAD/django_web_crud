from django.db import models
from . compress import *

# Create your models here.
class Registr(models.Model):
	"""docstring for Registrations"""
	first_name = models.TextField(max_length=20)
	last_name = models.TextField(max_length=20)
	email = models.EmailField(max_length=254)
	mobile = models.TextField(max_length=15)
	image = models.ImageField(upload_to = 'pic_folder/', default="", blank=True, null=True)
	image1 = models.ImageField(upload_to='thumbnails/image/', default="", blank=True, null=True)
	browser = models.CharField(max_length=100)
	def save(self, *args, **kwargs):
		# call the compress function
		new_image = compress(self.image, self.first_name)
		# set self.image to new_image
		self.image1 = new_image 
		# save
		super().save(*args, **kwargs)
