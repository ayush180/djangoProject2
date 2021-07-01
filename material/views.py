from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from .models import *
# Create your views here.
class NewMaterial(CreateView):
    model = material
    fields = '__all__'

class ViewMaterial(ListView):
    model = material
    context_object_name = 'materials'

class UpdateMaterial(UpdateView):
    model = material
    fields = '__all__'

class DeleteMaterial(DeleteView):
    model = material
    success_url = '/material/view'