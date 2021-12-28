from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms
from django.views import generic


class HomePageView(generic.ListView):
    template_name = 'product_1/home_page.html'
    queryset = models.Product.objects.filter().order_by('-id')
    context_object_name = 'product'

    def get_queryset(self):
        return models.Product.objects.filter()



class HomePageDetailView(generic.DetailView):
    template_name = 'product_1/home_page_detail.html'

    def get_object(self, **kwargs):
        homepage_id = self.kwargs.get('id')
        return get_object_or_404(models.Product, id=homepage_id)



class HomePageCreateView(generic.CreateView):
    template_name = 'product_1/add_home_page.html'
    form_class = forms.OrderForm
    success_url = '/product/'
    queryset = models.Product.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form=form)



class HomePageCreateView2(generic.CreateView):
    template_name = 'product_1/add_customer.html'
    form_class = forms.CustomerForm
    success_url = '/product/'
    queryset = models.Customer.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form=form)