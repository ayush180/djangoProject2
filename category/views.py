from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from .models import category
# Create your views here.
class NewCategory(CreateView):
    model = category
    fields = '__all__'

class ViewCategory(ListView):
    model = category
    context_object_name = 'categories'

class UpdateCategory(UpdateView):
    model = category
    fields = '__all__'

class DeleteCategory(DeleteView):
    model = category
    success_url = '/category/view'



