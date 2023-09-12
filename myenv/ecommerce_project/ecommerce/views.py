from django.shortcuts import render
from .models import Product

# Create your views here.



def home(request):
    return render(request, 'home.html')

def products(request):
    products = Product.objects.all()
    categories = []
    for i in Product.objects.all():
        if(i.category in categories):
            pass
        else:
            categories.append(i.category)

    context = {"categories": categories, "products": products, "pageHeading": "Featured Products"}
    return render(request, 'products.html', context)

def product_detail(request, product_id):
    product = Product.objects.get(id  = product_id)
    categories = []
    for i in Product.objects.all():
        if(i.category in categories):
            pass
        else:
            categories.append(i.category)

    context = {"categories": categories, "product": product}
    return render(request, 'product_detail.html', context)

def cart(request):
    return render(request, 'cart.html')

def productCategory(request, category):
    products = Product.objects.filter(category = category)
    categories = []
    for i in Product.objects.all():
        if(i.category in categories):
            pass
        else:
            categories.append(i.category)

    context = {"categories": categories, "products": products, "pageHeading": category}
    return render(request, "products.html" ,context)