from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from .models import *
from django.http import HttpResponseRedirect
# Create your views here.
class NewPayment(CreateView):
    model = suppayment
    fields = '__all__'

    def form_valid(self, form):
        self.object=form.save()
        self.object.bills.due_amount=self.object.bills.net_amount-self.object.cash
        if self.object.bills.due_amount <0 :
            self.object.bills.due_amount=self.object.bills.net_amount
            self.object.delete()
            return HttpResponseRedirect('/supplierpay/new/')
        else :
            self.object.bills.save()
            return HttpResponseRedirect(self.get_success_url())

class ViewPayment(ListView):
    model = suppayment
    context_object_name = 'supps'

class UpdatePayment(UpdateView):
    model = suppayment
    fields = '__all__'

class DeletePayment(DeleteView):
    model = suppayment
    success_url = '/supplierpay/view'

    def delete(self, request, *args, **kwargs):
        self.object=self.get_object()
        self.object.bills.due_amount=self.object.bills.due_amount+self.object.cash
        self.object.bills.save()
        return super(DeletePayment,self).delete(request,*args,**kwargs)
