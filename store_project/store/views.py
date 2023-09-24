from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Product, Category , Order
from django.views.generic import ListView , DetailView
from .utils import CategoryMixin


class ProductListView(ListView, CategoryMixin):
    model = Product

    def get_queryset(self):
        search_query = self.request.GET.get('search', None)
        if search_query:
            return self.model.objects.filter(title__icontains=search_query)
        return self.model.objects.all()


        
class ProductDetailView(DetailView, CategoryMixin):
    model = Product

class CategoryDetailView(DetailView, CategoryMixin):
    model = Category

# def product_list(request):
#     category_list = Category.objects.all()
#     search_query = request.GET.get('search', None)
#     if search_query:
#         product_list = Product.objects.filter(title__icontains=search_query)
#     else:
#         product_list = Product.objects.all()

#     return render(request, 'store/product_list.html', context={
#         'product_list': product_list,
#         'category_list': category_list
#     })


# def product_detail(request, pk):
#     category_list = Category.objects.all()
#     product = Product.objects.get(pk=pk)
#     return render(request, 'store/product_detail.html', context={
#         'product': product,
#         'category_list': category_list
#     })


# def category_detail(request, pk):
#     category_list = Category.objects.all()
#     category = Category.objects.get(pk=pk)
#     return render(request, 'store/category_detail.html', context={
#         'category': category,
#         'category_list': category_list
#     })


def save_order(request):
    product = Product.objects.get(pk = request.POST['product_id'])
    order = Order()
    category_list = Category.objects.all()
    order.name = request.POST['user_name']
    order.email = request.POST['user_email']
    order.product = product
    order.save()
    return render(request, 'store/save_order.html', context={
        'order':order,
        'category_list': category_list
    })
