from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from . import models
from .mixins import PageTitleMixin, ImageOperations


class PostCreateView(PageTitleMixin, CreateView):
	fields = ['title', 'content', 'image']
	model = models.Post
	page_title = "Add New Blog Post"

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super(PostCreateView, self).form_valid(form)


class PostListView(PageTitleMixin, ListView):
	context_object_name = "posts"
	model = models.Post
	page_title = "Keep up to date with the latest in buy-to-let properties"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		post_images = models.Post.objects.all()
		obj = ImageOperations()

		for post in post_images:
			obj.process_ratio(post.image)
		
		return context

	def get_queryset(self):
		return models.Post.objects.filter(visibility=True).order_by('-created_at')


class PostDetailView(PageTitleMixin, DetailView):
	model = models.Post

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		try:
			context['post_next'] = models.Post.objects.filter(id__gt=self.kwargs['pk']).order_by('created_at')[0:1].get()
			
		except models.Post.DoesNotExist:
			context['post_next'] = None

		try:
			context['post_prev'] = models.Post.objects.filter(id__lt=self.kwargs['pk']).order_by('-created_at')[0:1].get()
		except models.Post.DoesNotExist:
			context['post_prev'] = None

		return context