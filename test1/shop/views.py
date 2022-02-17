from django.shortcuts import render

# Create your views here.
from Orders.models import Order
from shop.models import Product, Category
from shop.forms import TestForm, MainForm


def mainPage(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    content = {
        "products" : products,
        "categories": categories,
               }
    return render(request, 'index.html', content)


def formsPage(request):
    form = TestForm()

    content = {
        "form": form,
    }
    return render(request, 'forms.html', content)




def formCompleted(request):
    name = request.POST['name']
    phone = request.POST['phone']
    content = {
        'name' : name,
        'phone' : phone,
    }
    return render(request, 'completed.html', content)

def showProduct(request, category_id, id):

    product = Product.objects.get(id=id)
    form = MainForm()
    username = request.POST.get('username')
    phone = request.POST.get('phone')
    comment = request.POST.get('comment')
    if username and phone and comment:
        el = Order(name = username, phone = phone, comment = comment, product = product)
        el.save()
    content = {
        'username' : username,
        'product' : product,
        'form' : form,
    }
    return render(request, 'product.html', content)

def categoryView(request, category_id):
    categories = Category.objects.all()
    products = Product.objects.filter(category_id=category_id)
    content = {
        "categories" : categories,
        "products" : products,
               }
    return render(request, 'index.html', content)