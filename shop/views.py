from django.shortcuts import render, get_object_or_404
from .models import Category, Product, Brand
from cart.form import AddProductToCartForm

def home(request):
    _all = Product.objects.all()
    new = _all[:6]
    featured = _all[15:20] 
    context = {
        'new' : new,
        'featured':featured,
        'section':'home'
    }
    return render(request, 'shop/index.html', context=context)

def product_list(request, category_slug = None, brand_slug = None):
    category   = None
    brand      = None
    brands     = Brand.objects.all()
    categories = Category.objects.all()
    products   = Product.objects.filter(available =True)
    
    if category_slug:
        category = get_object_or_404(Category, slug = category_slug)
        products = Product.objects.filter(category = category, available = True)

    if brand_slug:
        brand = get_object_or_404(Brand, slug = brand_slug)
        products= Product.objects.filter(brand=brand, available=True)


    context = {
        'category'   : category,
        'categories' : categories,
        'products'   : products,
        'brands'     : brands,
        'brand'      : brand,
        'section'    : 'shop'
    }

    return render(request, 'shop/product/category.html', context)


def product_detail(request, id, slug):
    product = get_object_or_404(Product,id=id,slug=slug,available=True)
    
    cart_product_form = AddProductToCartForm()

    context = {    
        'product': product,
        'cart_product_form' : cart_product_form,
        'section'     : 'shop'

    }
    
    return render(request, 'shop/product/single-product.html', context)