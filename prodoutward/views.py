from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from .models import *
# Create your views here.
class Newproduct(CreateView):
    model = prodoutward
    fields = ['prod', 'quantity', 'rate', 'price', 'discount', 'gst']
    context_object_name = 'product'

class Viewproduct(ListView):
    model = prodoutward
    context_object_name = 'prod'

class Updateproduct(UpdateView):
    model = prodoutward
    fields = ['prod', 'quantity', 'rate', 'price', 'discount', 'gst']

class Deleteproduct(DeleteView):
    model = prodoutward
    success_url = '/outward_purchase/closed'