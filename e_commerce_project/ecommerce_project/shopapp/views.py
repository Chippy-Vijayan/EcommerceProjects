from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template.defaultfilters import slugify

from .models import Category,Product
from django.core.paginator import Paginator,EmptyPage,InvalidPage
from . models import Category,Product
# Create your views here.
def add_category(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        def string_to_slug(text):
            # Convert to lowercase
            text = text.lower()

            # Replace non-alphanumeric characters with spaces
            text = ''.join(char if char.isalnum() else ' ' for char in text)

            # Replace consecutive spaces with a single hyphen
            text = '-'.join(text.split())
            return text
        slug = string_to_slug(name)
        description = request.POST.get('description')
        image = request.FILES['image']
        category = Category(name=name, slug=slug, description=description, image=image)
        category.save()
        return redirect('/')
    return render(request,'add_cat.html')

def add_product(request):
    cat = Category.objects.all()
    context = {
        'cat_list': cat
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        def string_to_slug(text):
            # Convert to lowercase
            text = text.lower()

            # Replace non-alphanumeric characters with spaces
            text = ''.join(char if char.isalnum() else ' ' for char in text)

            # Replace consecutive spaces with a single hyphen
            text = '-'.join(text.split())
            return text
        slug = string_to_slug(name)
        description = request.POST.get('description')
        price = request.POST.get('price')
        category_id = request.POST.get('category')
        category = Category.objects.get(name=category_id)
        image = request.FILES['image']
        stock = request.POST.get('stock')
        available = bool(request.POST.get('available'))
        created = request.POST.get('created')
        updated = request.POST.get('updated')
        product = Product(name=name,slug=slug,description=description,price=price,category=category,image=image,stock=stock,available=available,created=created,updated=updated)
        product.save()
        return redirect('/')
    return render(request,'add_prod.html',context)


def allProductCat(request,c_slug=None):
    c_page=None
    products_list=None
    if c_slug != None :
        c_page = get_object_or_404(Category,slug=c_slug)
        products_list = Product.objects.all().filter(category=c_page,available=True)
    else :
        products_list = Product.objects.all().filter(available=True)
    paginator = Paginator(products_list,6)
    try:
        page=int(request.GET.get('page','1'))
    except :
        page = 1
    try:
        products = paginator.page(page)
    except (EmptyPage,InvalidPage) :
        products = paginator.page(paginator.num_pages)

    return render(request,'category.html',{'category':c_page,'products':products})
def productDetail(request,c_slug,product_slug):
    try :
        product = Product.objects.get(category__slug = c_slug,slug=product_slug)
    except Exception as e:
        raise e
    return render(request,'product.html',{'product':product})