from django.shortcuts import render
from . models import Products
# Create your views here.

# from django.http import HttpResponse
# from django.template import loader

# from .models import Products

def index(request):
    products = Products.objects.all()
    print(products)
    params = {'product': products}
    return render(request, 'index.html', params)


def products(request):
    products = Products.objects.all()
    return render(request,"index.html", products)

def ContactUs(request):
    return render(request, 'ContactUs.html')


def Product(request):
    return render(request, 'Products.html')

def Post(request, id):
    product=Products.objects.get(id=id)
    context={'product':product}

    return render(request, 'Post.html',context)


def addproducts(request):
    return render(request, 'addproducts.html')




