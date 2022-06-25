from django.shortcuts import render, redirect
from main.models import Category2, Product, Order, OrderData, Contact, Contact2
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect
# Create your views here.

def shop(request):
    return render(request, 'shop-details.html')

def index(request):
    categories = Category2.objects.all()
    foodCard = Product.objects.all()       
    # products_cat = Product.objects.filter(category=pk)
    context= {'foodCard':foodCard, 'categories':categories}
    return render(request, 'index.html' , context=context)

def addToCart(request, id):
    cart_session = request.session.get('cart_session', [])
    cart_session.append(id)
    request.session['cart_session'] = cart_session
    return render(request, 'index.html')


def shopingcart(request):
    cart_session = request.session.get('cart_session', [])
    all_product_count = len(cart_session)
    products_inCart = Product.objects.filter(id__in=cart_session)
    print(products_inCart)    
    all_product_total_sum = 0
    for product_cart in products_inCart:
        product_cart.count = cart_session.count(product_cart.id)
        product_cart.sum = product_cart.count * product_cart.price
        all_product_total_sum += product_cart.sum

    return render(request, 'shoping-cart.html', {'products_inCart':products_inCart, 'all_product_count':all_product_count, 'all_product_total_sum':all_product_total_sum} )


def remove_from_url(request, pk):
    cart = request.session.get('cart_session', [])
    cart.remove(pk)
    request.session['cart_session'] = cart

    return redirect('shopingcart')

def order(request):
    return render(request, 'order.html')
    
def order_data(request):
    cart_session = request.session.get('cart_session', [])
    products_inCart = Product.objects.filter(id__in=cart_session)
    print(products_inCart)    
    all_product_total_sum = 0
    for product_cart in products_inCart:
        product_cart.count = cart_session.count(product_cart.id)
        product_cart.sum = product_cart.count * product_cart.price
        all_product_total_sum += product_cart.sum


    if request.method == 'POST':
        orderc = OrderData()
        orderc.name = request.POST.get('c_name')
        orderc.number = request.POST.get('c_number')
        orderc.address = request.POST.get('c_address')
        orderc.email = request.POST.get('c_email')
        orderc.message = request.POST.get('c_message')
        orderc.save()
    
        for i in products_inCart:
            order = Order()
            order.product = i.name
            order.price = i.price
            order.count = i.count
            order.total_sum = i.sum
            order.customer = orderc
            order.save()
    
    cart_session = request.session.get('cart_session', [])
    cart_session.clear()
    request.session['cart_session'] = cart_session
    all_product_count = len(cart_session)

    return redirect('thanks')
    

def thanks(request):
    return render(request, 'thanks.html')


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form = UserCreationForm()

    return render(request, 'user.html', {'form':form})    
        


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)


        if user is not None:
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()

    return render(request, 'user.html', {'form':form})



def signout(request):
    logout(request)
    return render(request, 'index.html')

def contact(request):
    return render(request, 'contact.html')


def sendContact(request):
    if request.method == 'POST':
        contact = Contact()
        contact.name = request.POST.get('name')
        contact.email = request.POST.get('email')
        contact.message = request.POST.get('message')
        contact.save()
    return HttpResponseRedirect('/')

def sendContacts(request):
    if request.method == 'POST':
        contacts = Contact2()
        contacts.email = request.POST.get('email')
        contacts.save()
    return HttpResponseRedirect('/')
