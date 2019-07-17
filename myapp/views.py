from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import *
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def index(request):
	return render(request, 'myapp/login.html')


def register_success(request):
	if request.method == "POST":
		try:
			first_name = request.POST.get("exampleFirstName")
			last_name = request.POST.get("exampleLastName")
			password = request.POST.get("password")
			mob = request.POST.get("examplemobile")
			email = request.POST.get("exampleInputEmail")
			image_file = request.FILES['image_file']
			error = ""
			aviavale_mob = Registr.objects.filter(mobile=mob).exists()
			aviavale_email = User.objects.filter(email=email).exists()
			if aviavale_mob:
				error = "Moile Number is exits"
				if aviavale_email:
					error = "Mobile and Email is allready exits."		
			elif aviavale_email:
				error = "Email id allready exits Please Enter another Email"
			elif  User.objects.filter(username=first_name).exists():
				error = "User Name allready exists Enter another Username."
			else:
				user = User.objects.create_user(first_name, email, password)
				user.first_name = first_name
				user.last_name = last_name
				user.save()
				obj = Registr(first_name=first_name, last_name=last_name, email=email, 
				mobile=mob, image=image_file)
				obj.save()
				request.session['id'] = user.id
				return redirect(log_in)
			return HttpResponse(error)
		except Exception as e:
			print(">>>>>>>>>>>", e)
			return HttpResponse("Something Wrong", e)	
	else:
		return render(request, 'myapp/register.html')


def log_in(request):
	if request.method == "POST":
		try:
			username = request.POST["username"]
			password = request.POST["password"]
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				request.session['id'] = user.id
				return redirect(success)
			else:
				msg = "User name or Passowrd is Wrong."
				return render(request, 'myapp/login.html', {"msg" : msg})
		except Exception as e:
			return HttpResponse("Your username and password didn't match.", e)
	else:
		return redirect(index)


def success(request):
	if not request.user.is_authenticated:
		return redirect(index)
	else:
		user = User.objects.get(id=request.session['id'])
		image = Registr.objects.filter(email=user.email)
		print("image>>>>>>>", image)
		contex = {
		"user" : user,
		"image" : image
		}
		return render(request, 'myapp/index.html', contex )


def forgot_password(request):
	if request.user.is_authenticated:
		return render(request, 'myapp/forgot-password.html')
	else:
		return redirect(index)

def tables(request):
	if request.user.is_authenticated:
		if request.method == "GET":	
			obj = Registr.objects.all()
			return render(request, 'myapp/tables.html', {"data" : obj})
	else:
		return redirect(log_in)


def edit(request, id):
	if request.user.is_authenticated:
		obj = Registr.objects.get(id=id)
		return render(request, 'myapp/update.html', {"data" : obj })
	else:
		return redirect(log_in)

def update(request, id):
	if not request.user.is_authenticated:
		return redirect(log_in)

	elif request.method == "POST":
		try:
			first_name = request.POST.get("exampleFirstName")
			last_name = request.POST.get("exampleLastName")
			password = request.POST.get("password")
			email = request.POST.get("exampleInputEmail")
			mob = request.POST.get("examplemobile")
			obj = Registr(id=id, first_name=first_name, last_name=last_name, email=email, 
				mobile=mob, password=password)
			obj.save()
			return redirect(tables)
		except Exception as e:
			return HttpResponse("Something Wrong", e)
		
	else:
		return redirect(log_in)


def delete(request, id):
	if not request.user.is_authenticated:
		return redirect(log_in)
	elif request.method == "GET":
		obj = Registr.objects.get(id=id)
		obj.delete()
		return redirect(tables)
	else:
		return redirect(log_in)


def log_out(request):
	if logout(request):
		try:
			return redirect(index)
		except Exception as e:
			return HttpResponse("Something Wrong", e)
	else:
		return redirect(index)

def error(request):
	return render(request, 'myapp/error.html', {"error": request})
