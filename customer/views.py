from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,DetailView
from .models import *
class NewCustomer(CreateView):
    model = customer
    fields = '__all__'

class ViewCustomer(ListView):
    model = customer
    context_object_name = 'customer'

class UpdateCustomer(UpdateView):
    model = customer
    fields = '__all__'

class DeleteCustomer(DeleteView):
    model = customer
    success_url = '/customer/view'

class Detail(DetailView):
    model = customer
    success_url = '/customer/view'