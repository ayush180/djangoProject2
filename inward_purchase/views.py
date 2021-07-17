from django.http import HttpResponseRedirect
from django.shortcuts import render
from prodinward.models import prodinward
from .models import inward_purchase
from django.views.generic import CreateView,ListView,DetailView,DeleteView, UpdateView
# Create your views here.

class NewInwardBill(CreateView):
    model = inward_purchase
    fields = ['date','sup','total','net_amount','gst','discount','due_amount']
    success_url = '/inward_purchase/view'

    def get_context_data(self, **kwargs):
        from django.db.models import Sum
        from django.db.models import aggregates
        context = super().get_context_data(**kwargs)
        context["products"] = prodinward.objects.filter(is_billed=False).all()
        result=prodinward.objects.filter(is_billed=False).aggregate(Sum('price'));
        context["total"]=result['price__sum'];
        return context

    def form_valid(self, form):
        print("inside  form valid before save")
        self.object = form.save()
        print("inside  form valid")
        for product in prodinward.objects.filter(is_billed=False).all():
            self.object.products.add(product)
            product.prod.quantity = int(product.prod.quantity) + int(product.quantity)
            product.prod.save()
            product.is_billed=True
            product.save()


        self.object.save()
        print("object is saved")
        return HttpResponseRedirect(self.get_success_url())


class ViewPurchaseBill(ListView):
    model = inward_purchase
    context_object_name = "bills"

class UpdatePurchaseBill(UpdateView):
    model = inward_purchase
    fields = ['date', 'sup', 'total', 'net_amount', 'gst', 'discount', 'due_amount']
    success_url = '/inward_purchase/view'

    def get_context_data(self, **kwargs):
        from django.db.models import Sum
        from django.db.models import aggregates
        context = super().get_context_data(**kwargs)
        context["products"] = self.object.products.all()
        result=prodinward.objects.filter(is_billed=False).aggregate(Sum('price'));
        context["total"]=result['price__sum'];
        return context



class DeletePurchaseBill(DeleteView):
    model = inward_purchase
    success_url = '/inward_purchase/view'

    # def delete(self, request, *args, **kwargs):
    #     print("inside  form valid before save")
    #     print("inside  form valid")
    #     for product in prodinward.objects.filter(is_billed=False).all():
    #         self.object=self.get_object()
    #         product.prod.quantity = int(product.prod.quantity) - int(product.quantity)
    #         product.prod.save()
    #         product.is_billed = True
    #         product.save()
    #         return super(DeletePurchaseBill, self).delete(request, *args, **kwargs)


class DetailPurchaseBill(DetailView):
    model = inward_purchase

def closewindow(request):
    return render(request,"inward_purchase/close_window.html")