from django.shortcuts import render, redirect
from django.http import HttpResponse
from . models import *
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.template.loader import render_to_string
from django.core.mail import send_mail, EmailMultiAlternatives

# Create your views here.

def index(request):
	if request.user.is_authenticated:
		return redirect(success)
	else:
		return render(request, 'myapp/login.html')


def register_success(request):
	if request.user.is_authenticated:
		return redirect(success)
	elif request.method == "POST":
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
			var = request.headers['User-Agent']
			var1 = var.split()
			if "Chrome" in var:
				var1 = var1[-2]
			else:
				var1 = var1[-1]
			
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
				obj.browser = var1
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
	if request.user.is_authenticated:
		return redirect(success)
	elif request.method == "POST":
		print(request.user.is_superuser)
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
		device_name = request.environ['GNOME_SHELL_SESSION_MODE']
		language = request.environ['LANGUAGE']
		server_name = request.environ['SERVER_NAME']
		Port = request.environ['SERVER_PORT']
		user = User.objects.get(id=request.session['id'])
		image = Registr.objects.filter(email=user.email)
		contex = {
		"user" : user,
		"image" : image,
		"device_name" : device_name,
		"language" : language,
		"server_name" : server_name,
		"Port" : Port,
		}
		return render(request, 'myapp/index.html', contex )


def forgot_password(request):
	if request.user.is_authenticated:
		return redirect(success)
	else:
		return render(request, 'myapp/forgot-password.html')


def tables(request):
	if request.user.is_authenticated:
		if request.method == "GET":
			obj = Registr.objects.all()
			user = User.objects.get(id=request.session['id'])
			image = Registr.objects.filter(email=user.email)
			contex = {
			"user" : user,
			"image" : image,
			"data" : obj
			}	
			
			return render(request, 'myapp/tables.html', contex)
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

	elif request.method == "PUT":
		try:
			first_name = request.POST.get("exampleFirstName")
			last_name = request.POST.get("exampleLastName")
			password = request.POST.get("password")
			email = request.POST.get("exampleInputEmail")
			mob = request.POST.get("examplemobile")
			obj = Registr(id=id, first_name=first_name, last_name=last_name, email=email, 
				mobile=mob, image=image_file)
			obj.save()
			return redirect(tables)
		except Exception as e:
			return HttpResponse("Something Wrong", e)
		
	else:
		return redirect(log_in)


def edit_profile(request, id):
	if request.user.is_authenticated:
		user = User.objects.get(id=id)
		obj = Registr.objects.get(email=user.email)
		contex = {
		"data" : obj,
		"user" : user
		}
		return render(request, 'myapp/profile_update.html', contex)
	else:
		return redirect(log_in)


def update_profile(request, id):
	if request.user.is_authenticated:
		if request.method == "POST":
			try:
				user = User.objects.get(id=id)
				obj = Registr.objects.get(email=user.email)
				first_name = request.POST.get("exampleFirstName")
				last_name = request.POST.get("exampleLastName")
				email = request.POST.get("exampleInputEmail")
				mob = request.POST.get("examplemobile")
				image_file = request.FILES.get('image_file')
				error = ""
				# aviavale_mob = Registr.objects.filter(mobile=mob).exists()
				# aviavale_email = User.objects.filter(email=email).exists()
				# if aviavale_mob == True and Registr.objects.filter(mobile=obj.mobile).exists() == False:
				# 	error = "Moile Number is exits"
				# 	if aviavale_email and Registr.objects.filter(email=obj.email).exists() == False:
				# 		error = "Mobile and Email is allready exits."		
				# elif aviavale_email and Registr.objects.filter(email=obj.email).exists() == False:
				# 	error = "Email id allready exits Please Enter another Email"
				if image_file == None:
					obj.first_name = first_name
					obj.last_name = last_name
					obj.email = email
					obj.mobile = mob
					user.username = first_name
					user.email = email
					user.last_name = last_name
					user.save() 
					obj.save()
					return success(request)
				else:
					obj = Registr(id=obj.id, first_name=first_name, last_name=last_name, email=email, 
						mobile=mob, image=image_file)
					user.username = first_name
					user.email = email
					user.last_name = last_name
					user.save() 
					obj.save()
					return success(request)
				return HttpResponse(error)
			except Exception as e:
				print("Exception", e)
				return HttpResponse("Something Wrong", e)
	else:
		return redirect(log_in)


def show_profile(request, id):
	if request.user.is_authenticated:
		if request.method == "GET":
			user = User.objects.get(id=id)
			obj = Registr.objects.get(email=user.email)
			contex = {
			"user" : user,
			"data" : obj
			}
			return render(request, 'myapp/show_profile.html', contex)
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


def email(request):
	if request.method == "POST":
		recipient_list = [request.POST.get("forgetemail")]
		subject = 'Chang the paassword!!!'
		text_content = 'This is an important message.'
		html_content = render_to_string("myapp/emailtemplate.html", {"recipient_list" :
			request.POST.get("forgetemail")})
		email_from = settings.EMAIL_HOST_USER
		msg = EmailMultiAlternatives(subject, text_content, email_from, recipient_list)
		msg.attach_alternative(html_content, "text/html")
		msg.send()
		return redirect(log_in)
	else:
		return redirect(log_in)


def confirm_password(request):
	confirm_password = request.GET["confirm_password"]
	email = request.GET["email"]
	print(email)
	obj = User.objects.filter(email = email)
	if not obj.exists():
		return HttpResponse("Email does not exists.")
	for i in obj:
		i.set_password(confirm_password)
		i.save()
	return redirect(log_in)	
