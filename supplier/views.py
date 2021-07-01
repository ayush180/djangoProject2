from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from .models import *
class NewSupplier(CreateView):
    model = suppliers
    fields = '__all__'

class ViewSupplier(ListView):
    model = suppliers
    context_object_name = 'supply'

class UpdateSupplier(UpdateView):
    model = suppliers
    fields = '__all__'

class DeleteSupplier(DeleteView):
    model = suppliers
    success_url = '/supplier/view'