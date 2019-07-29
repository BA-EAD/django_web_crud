from PIL import Image
from io import BytesIO
from django.core.files import File

size = 128, 128
def compress(image, name):
		im = Image.open(image)
		im.thumbnail(size, Image.ANTIALIAS)
		im_io = BytesIO() 
		im.save(im_io, 'JPEG', quality=70)
		new_image = File(im_io, name=image.name)
		return new_image
