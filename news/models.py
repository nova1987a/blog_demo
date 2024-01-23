from django.db import models

# Create your models here.
class Author(models.Model):
	name = models.CharField(max_length=100)

class Report(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField(blank=True)
	created_on = models.DateTimeField(auto_now= True)
	author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)

	def __str__(self):
		return self.title


