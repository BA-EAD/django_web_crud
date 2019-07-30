#					Django-bootstrap-sb2

#					Install the Python, Virtual Envirment and 	   									Django
step:1	sudo apt update<br>
step:2	python3 -V

#	Next, let's install pip from the  repositories:
step:3	sudo apt install python3-pip

#	Once pip is installed, you can use it to install the venv package:
step:4	sudo apt install python3-venv
		mkdir ~/newproject
		cd ~/newproject

#	Next, create a virtual environment
step:5	python3.6 -m venv my_env

#	To install packages into the isolated environment, you must activate it by typing:
step:6	source my_env/bin/activate

#	Install django
step:7	pip install django

#	You can verify the installation by typing:
setp:8 	django-admin --version


#				Project Configurations


#	Create a Django Project
django-admin startproject <name_of_project>

#	Create a Django App in Project

cd <name_of_project>
	python3 manage.py startapp <name_of_app>
find the settings.py file that is in the root project folder
and add the app name

#add this
INSTALLED_APPS = [
    #....
    '<name_of_app>',
    #...
]

Create a urls.py file  in the <name_of_app> app.
After that go into the root project and find the urls.py file

#add this

from django.urls import path, include

urlpatterns = [
    #...
    path('', include("<name_of_app>.urls")),
    #...
]

#				Mysql Database Configuratios

#	Install mysqlclient
pip install mysqlclient

Goto the settings.py file and 
#add this

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'database name',                      			
        'USER': 'username',                      
        'PASSWORD': 'password',                  
        'HOST': 'host name',                 
        'PORT': 'port number', 
    }
}

# Migrate the project
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver