from django.shortcuts import render, redirect
from shoppingApp.forms import ProductForm
from shoppingApp.forms import CartForm
from shoppingApp.models import Product
from shoppingApp.models import Cart
from . import views
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.db.models import Avg, Count, Min, Sum
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect




def home(request):
	all_items = Product.objects.all
	return render(request,'home.html', {'all_items':all_items})

    # return render(request, 'home.html',{})

def about(request):
    return render(request, 'about.html',{})

@login_required
def product(request):
    return render(request, 'addProduct.html',{})

# @login_required
# def cart(request,id):
# 	all_carts = Cart.objects.get(pk=1)
# 	total = Cart.objects.all().aggregate(Sum('price'))
# 	# avrg = Cart.objects.all().aggregate(Sum('price'))
# 	avrg = 0000
# 	context = {'foo': avrg,}
# 	return render(request, 'cart.html',{'all_carts':all_carts,'priceTotal':total,'avrg':context,'fTotal':total})


@login_required
def cart(request,id):
	all_carts = Cart.objects.filter(created_by=id)
	total = all_carts.aggregate(Sum('price'))
	# avrg = Cart.objects.all().aggregate(Sum('price'))
	avrg = 0000
	context = {'foo': avrg,}
	return render(request, 'cart.html',{'all_carts':all_carts,'priceTotal':total,'avrg':context,'fTotal':total})



@login_required
def addproduct(request):
	if request.method == "POST":
		form = ProductForm(request.POST)
		if form.is_valid():
			try:
				form.save()
				messages.success(request, ('Item added successfully!'))
				return redirect("/")
			except:
				pass
	else:
		form = ProductForm()
	return render(request, "addProduct.html",{'form':form})

@login_required
def addToCart(request, id1, id2):
	if request.method == "POST":
		form = CartForm(request.POST)
		if form.is_valid():
			try:
				form.save()
				messages.success(request, ('Product successfully added to cart!'))
				return redirect("/")
			except:
				pass
	else:
		form = CartForm()
	return redirect("home")

@login_required
def deleteToCart(request,list_id):
	id=request.user.id
	item = Cart.objects.filter(pk=list_id)
	item.delete()
	messages.success(request, ('Item Has Been Deleted!'))
	return redirect("cart",id)

@login_required
def checkout(request):
    return render(request, 'checkout.html',{})


@login_required
def payment(request,id):
	p = Cart.objects.filter(created_by=id)
	p.delete()
	return render(request, 'thankyou.html',{})

@login_required
def thankyou(request):
	return render(request, 'thankyou.html',{})

@login_required
def offerApply(request,id):
	all_carts = Cart.objects.filter(created_by=id)
	total = all_carts.aggregate(Sum('price'))
	avrg = all_carts.aggregate(Sum('price'))
	
	for value in total.values():
		avrg = value
		avrg = avrg/2
		context = {'foo': avrg,}

	return render(request, 'cart.html',{'all_carts':all_carts,'priceTotal':total,'avrg':context,'fTotal':context})
