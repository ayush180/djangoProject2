from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from .models import *
# Create your views here.
class Newsubcategory(CreateView):
    model = subcategory
    fields = '__all__'

class Viewsubcategory(ListView):
    model = subcategory
    context_object_name = 'subcategories'

class Updatesubcategory(UpdateView):
    model = subcategory
    fields = '__all__'

class Deletesubcategory(DeleteView):
    model = subcategory
    success_url = '/subcategory/view'