from django.shortcuts import render
from .models import Product

# Create your views here.



def home(request):
    return render(request, 'home.html')

def products(request):
    category = request.GET.get("category", None)
    print(category == "")
    if  category != None and category != "":
        products = Product.objects.filter(category = category)
    else:
        products = Product.objects.all()
    print(products)
    categories = []
    for i in Product.objects.all():
        if(i.category in categories):
            pass
        else:
            categories.append(i.category)

    sort_criteria = request.GET.get('sort', 'name')  # Default to sorting by name
    sort_order = request.GET.get('order', 'asc')  # Default to ascending order    
    if sort_criteria == 'name':
        products = products.order_by('name' if sort_order == 'asc' else '-name')
    elif sort_criteria == 'price':
        products = products.order_by('price' if sort_order == 'asc' else '-price')
    elif sort_criteria == "id":
        products = products.order_by("id" if sort_order == "asc" else "-id")

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