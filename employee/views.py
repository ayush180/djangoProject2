from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DeleteView,DetailView
from .models import *
class NewEmployee(CreateView):
    model = employee
    fields = '__all__'

class ViewEmployee(ListView):
    model = employee
    context_object_name = 'employees'

class UpdateEmployee(UpdateView):
    model = employee
    fields = '__all__'

class DeleteEmployee(DeleteView):
    model = employee
    success_url = '/employee/view'

class Detail(DetailView):
    model = employee
    success_url = '/employee/view'