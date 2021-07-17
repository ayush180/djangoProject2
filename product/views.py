from django.views.generic import CreateView,ListView,UpdateView,DeleteView, DetailView
from .models import *
# Create your views here.
class Newproduct(CreateView):
    model = product
    fields = '__all__'

class Viewproduct(ListView):
    model = product
    context_object_name = 'products'

class Updateproduct(UpdateView):
    model = product
    fields = '__all__'

class Deleteproduct(DeleteView):
    model = product
    success_url = '/product/view'

class Detail(DetailView):
    model = product
    success_url = '/product/view'