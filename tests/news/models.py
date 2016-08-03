from __future__ import unicode_literals
from django.contrib.syndication.views import Feed

from django.db import models

# Create your models here.
class News(models.Model):
	tittle = models.CharField(max_length=50)
	
	fullDef = models.TextField()
	image = models.ImageField(upload_to='news')
	habr = "habrahabr.ru"
	maduza = "maduza.io"
	lenta = "lenta.ru"
	SOURCE_CHOICES = (
        (habr, 'habrahabr.ru'),
        (maduza, 'maduza.io'),
        (lenta, 'lenta.ru'),
    )
	source = models.CharField(max_length=50,choices=SOURCE_CHOICES, default=habr) 
	dateAdd =models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.tittle

