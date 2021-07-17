from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from .models import *
from django.http import HttpResponseRedirect
# Create your views here.
class NewPayment(CreateView):
    model = cuspayment
    fields = '__all__'

    def form_valid(self, form):
        self.object = form.save()
        self.object.bills.due_amount = self.object.bills.net_amount - self.object.cash
        if self.object.bills.due_amount < 0:
            self.object.bills.due_amount = self.object.bills.net_amount
            self.object.delete()
            return HttpResponseRedirect('/customerpay/new/')
        else:
            self.object.bills.save()
            return HttpResponseRedirect(self.get_success_url())

class ViewPayment(ListView):
    model = cuspayment
    context_object_name = 'cust'

class UpdatePayment(UpdateView):
    model = cuspayment
    fields = '__all__'

class DeletePayment(DeleteView):
    model = cuspayment
    success_url = '/customerpay/view'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.bills.due_amount = self.object.bills.due_amount + self.object.cash
        self.object.bills.save()
        return super(DeletePayment, self).delete(request, *args, **kwargs)