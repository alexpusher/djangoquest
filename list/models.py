from django.db import models
from django.core.urlresolvers import reverse
# Create your models here.
class mosttop( models.Model ):
	name = models.CharField( max_length=255 )
	def get_absolute_url(self):
		return reverse('list')
	def __str__(self):
		return self.name

class top( models.Model ):
	parent = models.ForeignKey( 'mosttop', null=True, blank=True )
	name = models.CharField( max_length=255 )
	def get_absolute_url(self):
		return reverse('list')
	def __str__(self):
		return self.name
		
class Category( models.Model ):
	parent = models.ForeignKey( 'top', null=True, blank=True )
	name = models.CharField( max_length=255 )
	href = models.CharField( max_length=255 )
	def __str__(self):
		return self.name