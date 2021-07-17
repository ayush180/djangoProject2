from django.http import HttpResponseRedirect
from django.shortcuts import render
from prodinward.models import prodinward
from .models import loss
from django.views.generic import CreateView,ListView,DetailView,DeleteView, UpdateView
# Create your views here.
class NewLoss(CreateView):
    model = loss
    fields = '__all__'

class ViewLoss(ListView):
    model = loss
    context_object_name = 'losses'
    
class UpdateLoss(UpdateView):
    model = loss
    fields = '__all__'
  
class DeleteLoss(DeleteView):
    model = loss
    success_url = '/loss/view'