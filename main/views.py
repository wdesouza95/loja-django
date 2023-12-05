from django.shortcuts import render
from .models import Category, Marca, Product, ProductAttribute, Banner

def home(request):
    banners = Banner.objects.all().order_by('-id')
    data = Product.objects.filter(destaque=True).order_by('-id')
    return render(request, 'index.html', {'data':data, 'banners':banners})


def category_list(request):
    data = Category.objects.all().order_by('-id')
    return render(request, 'category_list.html', {'data':data})


def filters(request):
    return render(request, 'filters.html')


def marca_list(request):
    data = Marca.objects.all().order_by('-id')
    return render(request, 'marca_list.html', {'data':data})


def product_list(request):
    data = Product.objects.all().order_by('-id')

    cats = Product.objects.distinct().values('category__title', 'category__id')
    marcas = Product.objects.distinct().values('marca__title', 'marca__id')
    colors = Product.objects.distinct().values('color__title', 'color__id', 'color__color_codigo')
    sizes = ProductAttribute.objects.distinct().values('size__title', 'size__id')
    prices = ProductAttribute.objects.distinct().values('price')

    return render(request, 'product_list.html', 
                  {
                      'data':data,
                      'cats':cats,
                      'marcas':marcas,
                      'colors':colors,
                      'sizes':sizes,
                      'prices':prices

                   }
                   )

def category_product_list(request, cat_id):
    category = Category.objects.get(id=cat_id)
    data = Product.objects.all().filter(category=category).order_by('-id')
    cats = Product.objects.distinct().values('category__title', 'category__id')
    marcas = Product.objects.distinct().values('marca__title', 'marca__id')
    colors = Product.objects.distinct().values('color__title', 'color__id', 'color__color_codigo')
    sizes = ProductAttribute.objects.distinct().values('size__title', 'size__id')
    prices = ProductAttribute.objects.distinct().values('price')

    return render(request, 'category_product_list.html', 
                  {
                      'data':data,
                      'cats':cats,
                      'marcas':marcas,
                      'colors':colors,
                      'sizes':sizes,
                      'prices':prices

                   }
                   )

def marca_product_list(request, marca_id):
    marca = Marca.objects.get(id=marca_id)
    data = Product.objects.all().filter(marca=marca).order_by('-id')
    cats = Product.objects.distinct().values('category__title', 'category__id')
    marcas = Product.objects.distinct().values('marca__title', 'marca__id')
    colors = Product.objects.distinct().values('color__title', 'color__id', 'color__color_codigo')
    sizes = ProductAttribute.objects.distinct().values('size__title', 'size__id')
    prices = ProductAttribute.objects.distinct().values('price')

    return render(request, 'marca_product_list.html', 
                  {
                      'data':data,
                      'cats':cats,
                      'marcas':marcas,
                      'colors':colors,
                      'sizes':sizes,
                      'prices':prices

                   }
                   )

def product_detail(request, slug, id):
    product = Product.objects.get(id=id)
    cats = Product.objects.distinct().values('category__title', 'category__id')
    marcas = Product.objects.distinct().values('marca__title', 'marca__id')
    colors = Product.objects.distinct().values('color__title', 'color__id', 'color__color_codigo')
    sizes = ProductAttribute.objects.distinct().values('size__title', 'size__id')
    prices = ProductAttribute.objects.distinct().values('price')

    return render(request, 'product_detail.html', 
                  {
                      'data':product,
                      'cats':cats,
                      'marcas':marcas,
                      'colors':colors,
                      'sizes':sizes,
                      'prices':prices

                   }
                   )