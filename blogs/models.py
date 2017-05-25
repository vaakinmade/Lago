from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User


class Post(models.Model):
	created_at = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=225)
	author = models.ForeignKey(User)
	content = models.TextField()
	hits = models.IntegerField(default=0)
	featured = models.BooleanField(default=False)
	visibility = models.BooleanField(default=True)
	image = models.ImageField(upload_to='images/lagopoly', default='pic_folder/None/no-img.jpg')

	def __str__(self):
		return "Post by " + self.author.username

	def get_absolute_url(self):
   	    return reverse('blogs:create')
