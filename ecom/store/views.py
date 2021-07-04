from django.shortcuts import render, get_object_or_404
from .models import Category, Product  


# Create your views here.
def categories(request):
    return{
        'categories':Category.objects.all()
    }



def product_all(request):
    products=Product.objects.all()
    context= {
     'products':products
    }
    return render (request, 'store/home.html',context)


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/products/detail.html', {'product':product})


def category_list(request, category_slug):
    #select one iteam from the database where slug is the giver slug
    category = get_object_or_404(Category, slug=category_slug ) 
    products = Product.objects.filter(category=category)
    data={
        'category':category,
        'products':products
     }
    return render(request, 'store/products/category.html', data)