from django.shortcuts import render
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from .models import *
# Create your views here.
class NewPayment(CreateView):
    model = OwnerPayment
    fields = '__all__'

class ViewPayment(ListView):
    model = OwnerPayment
    context_object_name = 'OwnerPayments'

class UpdatePayment(UpdateView):
    model = OwnerPayment
    fields = '__all__'

class DeletePayment(DeleteView):
    model = OwnerPayment
    success_url = '/ownerpayment/view'