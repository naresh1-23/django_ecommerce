from django.shortcuts import render, redirect
from .models import Category, Cart, Product, Order
from django.contrib import messages


# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

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

def cart(request):
    datas = Cart.objects.filter(user_id = request.user)
    
    return render(request, "cart.html", {'datas': datas})

def SingleProduct(request, pk):
    data = Product.objects.filter(id = pk).first()
    description_new = data.product_description.split(".")
    if request.method == "POST":
        quantity = request.POST['quantity']
        user = request.user
        new_quantity =data.quantity -  int(quantity)
        new_cart = Cart.objects.filter(user_id = user , product = data).first()
        if new_cart is None:
            cart = Cart.objects.create(quantity=quantity, user_id = user, product = data )
            cart.save()
        else:
            old_quantity = new_cart.quantity
            new_cart.quantity = old_quantity+int(quantity)
            new_cart.save()
        data.quantity = new_quantity
        data.save()
        messages.success(request, "Successfully added to cart")
        return redirect("cart")
    return render(request, "singlepage.html", {'data': data, "description_new": description_new})


def delete_cart(request, pk):
    data = Cart.objects.filter(id = pk).first()
    product = Product.objects.filter(id = data.product.id).first()
    new_quantity = data.quantity+product.quantity
    product.quantity = new_quantity
    data.delete()
    product.save()
    messages.success(request, "Item successfully deleted from the cart")
    return redirect("cart")

def order_cart(request, pk):
    user = request.user
    cart = Cart.objects.filter(id = pk).first()
    product = Product.objects.filter(id = cart.product.id).first()
    order = Order.objects.create(user_id = user, product_id = product, quantity = cart.quantity)
    order.save()
    cart.delete()
    messages.success(request, "Order placed successfully")
    return redirect("order")

def ordersUser(request):
    datas = Order.objects.filter(user_id = request.user)
    return render(request, "usersorder.html", {'datas': datas})

def admin_order(request):
    if request.user.is_superuser:
        datas = Order.objects.all()
        return render(request, 'adminorder.html', {'datas': datas})
    return redirect('home')