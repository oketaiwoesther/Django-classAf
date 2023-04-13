from django.shortcuts import render
from django.views.generic import TemplateView 
from .models import Post
# from .forms import PostForm
# Create your views here.

class HomePageView(TemplateView):

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context

   
class ContactPageView(TemplateView):

    template_name = "contact.html"
    
    