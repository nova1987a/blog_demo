from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse #used to generate URLs by reverting the URL pattern

# Create your models here.

STATUS = (
	(0, "Draft"),
	(1, "Publish")
)
class Tag(models.Model):
	"""Model representing a blog tags."""
	name = models.CharField(max_length=200, help_text='Enter a blog tag (e.g. science)')

	def __str__(self):
	        """String for representing the Model object."""
        	return self.name

class Blog(models.Model):
	title = models.CharField(max_length=200, unique=True)
	author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
	updated_on = models.DateTimeField(auto_now= True)
	content = models.TextField()
	created_on = models.DateTimeField(auto_now_add=True)
	status = models.IntegerField(choices=STATUS, default=0)
	tag = models.ManyToManyField(Tag, help_text='Select a tag for this book')
	class Meta:
        	ordering = ['-created_on']

	def __str__(self):
        	return self.title

# ----------- Add below for modification ------------------------------------    
	def get_absolute_url(self):
        	"""Returns the url to access a detail record for this blog"""
        	return reverse('blog_detail', kwargs={'pk': self.pk})

	def display_tag(self):
	        """ Create a string for the Tag. This is required to display tag in Admin."""
        	return ', '.join(tag.name for tag in self.tag.all()[:3])
	display_tag.short_description = 'Tag'


#class Blogger(models.Model):
#	name = models.CharField(max_length=250)

#class Article(models.Model):
#	title = models.CharField(max_length=250)
#	content = models.TextField(blank=True)
#	created_on = models.DateTimeField(auto_now_add=True)
#	updated_on = models.DateTimeField(auto_now_add=True)
#	blogger = models.ForeignKey(Blogger, on_delete=models.CASCADE)

