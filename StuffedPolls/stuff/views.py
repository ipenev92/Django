from django.views.generic import ListView, DetailView

from .models import Page


class IndexView(ListView):
    template_name = 'stuff/pages_list.html'
    model = Page



class AnyPageView(DetailView):
    template_name = 'stuff/page.html'
    model = Page
