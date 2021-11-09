from django.shortcuts import render
from django.views.generic import ListView,DetailView
# Create your views here.
from .models import Post,Shop


class HomeView(ListView):
	model=Shop
	template_name='index.html'


class AboutView(ListView):
	model=Shop
	template_name='about.html'

class ContactView(ListView):
	model=Shop
	template_name='contact.html'
	
class ShopView(ListView):
	model=Post
	template_name='shop.html'


class SingleProductView(DetailView):
	model=Post
	template_name='singleProduct.html'