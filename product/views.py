from django.shortcuts import render, redirect
from .models import Category, Cart, Product
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request, 'home.html')

def add_product(request):
    if request.user.is_superuser:
        category = Category.objects.all()
        if request.method == 'POST':
            name = request.POST['name']
            description = request.POST['description']
            price = request.POST['price']
            quantity  = request.POST['quantity']
            category  = request.POST['category']
            product_image = request.FILES['product_image']
            if name == '' or description == '' or price == '' or quantity == '' or category == '' or product_image == '':
                messages.warning(request, "Fields cannot be empty")
                return redirect('add-product')
            elif not price.isdigit() or not quantity.isdigit():
                messages.warning(request, "price and quantity should be in number")
                return redirect('add-product')
            else:
                category_obj = Category.objects.filter(name = category).first()
                if category_obj is None:
                    messages.warning(request,"category doesn't exist")
                    return redirect('add-product')
                else:
                    data = Product.objects.create(product_name = name , product_description = description, product_img = product_image, price = price, quantity = quantity, category = category_obj)
                    data.save()
                    messages.success(request, "Product successfully added")
                    return redirect('home')                 
        return render(request, "addproduct.html", {'category': category})
    return redirect('home')