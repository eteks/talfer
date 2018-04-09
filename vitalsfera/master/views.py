from django.shortcuts import render
from django.views.generic import TemplateView # Import TemplateView
# Create your views here.
# Create your views here.
# Add the two views we have been talking about  all this time :)
class Index_pageview(TemplateView):
    template_name = "index.html"
class Home_pageview(TemplateView):
    template_name = "home.html"