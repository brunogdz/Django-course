# Django Tutorial

Welcome to Django Tutorial, I'm Bruno, welcome again, I'm glad that you showed up! So, this is just a few steps to have contact with Django Framework!!

I hope that you'd contact with python before, so, there are the steps to run the first Django App!

## Steps

### Step 1

Create on your VS Code a folder

### Step 2

Make sure you have Django installed. If it's not

```
pip3 install django
```

We are now ready to use django and create our first Django project

Check with this command:

```
python3 -m django --version
```

### Step 3

Run to start the project

```
django-admin startproject myproject
```

### Step 4

Go to the project and create the app

```
cd myproject
```

```
python3 manage.py startapp myapp
```

After you create the app you can run the server

```
python3 manage.py runserver
```

### Step 5

Now you will see something like this:

<img width="auto" src="https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/2qf2oWa1SP-7x-uVj3dDLw_a559d35295d84210afe17fc1561916a1_runserver.jpeg?expiry=1708300800000&hmac=LqZF_G8NYDXA4u_kOa5UnAfTafx3WyYFCiTYDTp7Ttw" >

### Step 6

Finally, you can access the page with [http://127.0.0.1:8000/](http://127.0.0.1:8000/) or [http://localhost:8000](http://localhost:8000)

## Models

If you check the folder my app you will see that I have a models.py file, there I created a simple model that contains course, year and name.

After you finish writing the model, you need to go to the settings.py file that is inside the project folder.

### Installing on the project the model that you created

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

you will see on the file this Installed_apps, but you can see that's not showing the myapp there, so to you install there you need to type

```
'myapp.apps.MyappConfig',
```

So will be like:

```
INSTALLED_APPS = [
    'myapp.apps.MyappConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

## Migrations

After you finish to write on installed_apps, you need to do a migration. There are the commands that you will do:

```
python manage.py makemigrations
```

```
python manage.py migrate
```

But imagine that you want to change a field or more fields on your model, what's the proceed? You'll need to run the command to makemigrations, that it will apply the changes that you did on the models.

So, imagine that you want to change on the model on myapp:

```
class Menuitems(models.Model):
    name = models.CharField(max_length = 200)
    course = models.CharField(max_length = 200)
    year = models.IntegerField()
```

to:

```
class Menuitems(models.Model):
    name = models.CharField(max_length = 200)
    category = models.CharField(max_length = 200)
    year = models.IntegerField()
```

you will need to run:

```
python manage.py makemigrations
```

if you want to check the migrations that you did, you can run:

```
python manage.py showmigrations
```

If you want to use the admin.py inside the myapp folder you can use like:

```
from django.contrib import admin
from .models import Drinks

# Register your models here.
admin.site.register(Menuitems)
```

Let's give you another example of a new model and we created a app for a bar. Let's use this example to explain how Foreign Keys works:

the models:

```
from django.db import models

# Create your models here.
class DrinksCategory(models.Model):
    category_name = models.CharField(max_length=200)

class Drinks(models.Model):
    drink = models.CharField(max_length=200)
    price = models.IntegerField()
    category_id = models.ForeignKey(DrinksCategory, on_delete=models.PROTECT, default=None)

```

admin.py:

```
from django.contrib import admin
from .models import Drinks
from .models import DrinksCategory

# Register your models here.
admin.site.register(Drinks)
admin.site.register(DrinksCategory)
```

and then just run the migrations

## Forms

### Using Forms

Inside the app's folder, we have forms.py, this is a way that reduce time and uses the models and way better when render in a view. There are the examples:

forms.py:

```
from django import forms

from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'
```

models.py:

```
from django.db import models

# Create your models here.
class Booking(models.Model):
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    guest_count = models.IntegerField()
    reservation_time = models.DateField(auto_now=True)
    comments = models.CharField(max_length=1000)
```

admin.py:

```
from django.contrib import admin
from .models import Booking

# Register your models here.
admin.site.register(Booking)
```

## Admin

### Managing users

One admin.py we need to setup the user

```
from django.contrib, import admin
# Register your models here.
from django.contrib.auth.models, import User
# Unregister the provided model admin:
admin.site.unregister(User)
```

To register our own admin, use @admin.register() decorator. Give the user a model as the argument. Decorate a sub-class of UserAdmin class.

```
from django.contrib.auth.admin import UserAdmin
@admin.register(User)
class NewAdmin(UserAdmin):
    pass
```

The user model has a field date_joined. Suppose you want that its value given at the time of creating a new user should never be changed. So, keep this field in the readonly_fields list. Include this at the end of admin.py

```
from django.contrib.auth.admin import UserAdmin
@admin.register(User)
class NewAdmin(UserAdmin):
    readonly_fields = [
        'date_joined',
    ]
```

Django Admin’s change form will show date_joined field as disabled, thereby, it will not be editable.

The UserAdmin class (the base class for NewAdmin class that you have registered in the admin site) has a method known as get_form(). You need to override it to disable the username field in it.

```
def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
```

Next, verify if the current user is a super user. If yes, disable the username field in the form.

```
is_superuser = request.user.is_superuser

        if not is_superuser:
            form.base_fields['username'].disabled = True
```

The NewAdmin class that is registered as admin will now look like this:

```
from django.contrib.auth.admin import UserAdmin
@admin.register(User)
class NewAdmin(UserAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser

        if not is_superuser:
            form.base_fields['username'].disabled = True

        return form
```

For using we need to set on installed_apps:

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'myapp.apps.MyappConfig',
]
```

### Permissions

Let’s assume that there is a Product model in a Django app named myapp. Here, a custom permission called change_category has been defined.

```
class Product(models.Model):
    ProductID: models.IntegerField()
    name : models.TextField()
    category : models.TextField
    class Meta:
        permissions = [('can_change_category', 'Can change category')]
```

This name of permission will be visible in the list of available user permissions when a new user is added or an existing group is edited.

### Enforcing permissions at the view level

If a user has logged in and has been authenticated, its details are available to the view function in the form of request.user object. If not, the value of request.user is an instance of AnonymousUser. In that case, the permission to call a view can be denied as follows:

```
from django.core.exceptions import PermissionDenied
def myview(request):
    if request.user.is_anonymous():
        raise PermissionDenied()
```

You can decorate the view with a login_required decorator. It only allows access for logged users.

```
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
 @login_required
def myview(request):
    return HttpResponse("Hi, you're logged!")
```

Another way of restricting access to a view is by using the @user_passes_test()decorator. It takes one mandatory argument, which is a function returning True or False. If True is returned, the decorated view function defined below it is invoked.

Let’s define a function testpermission(). It returns True if the user is authenticated and has a change_category permission.

```
def testpermission(user):
    if user.is_authenticated() and user.has_perm("myapp.change_category"):
        return True
    else:
        return False
```

This function is then used as an argument to the @user_passes_test() decorator. The view function defined below it will be invoked if the testpermission() function returns True.

```
from django.contrib.auth.decorators import user_passes_test

@user_passes_test(testpermission)
def change_ctg(request):
    # Logic for making change to category of product model instance
```

The user_passes_test() can be given an additional argument – login_url. The user will be redirected to this URL if the testpermission() function returns False. Typically, it is mapped to a view that renders a login page.

Another method to enforce permission at the view level is with the @permission_required() decorator. Unless the user possesses the permission mentioned as an argument, the view function won’t be called.

```
from django.contrib.auth.decorators import permission_required

@permission_required("myapp.change_category")
def store_creator(request):
    # Logic for making change to category of product model instance
```

To enforce permissions on a class-based view, you need to use PermissionRequiredMixin and set the permission_required attribute of the view class to the permission you want to enforce.

Here is an example:

Assuming that a product model is present in models.py. The ProductListView class view renders a list of products only if the user has view permission on this model.

```
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic import ListView

from .models import Product

class ProductListView(PermissionRequiredMixin, ListView):
    permission_required = "myapp.view_product"
    template_name = "product.html"
    model = Product
```

### Permissions in Template

You can check various user attributes, such as is_authenticated and render the information on the web page accordingly. A typical template looks like this:

```
<html>
<body>
{% if user.is_authenticated %}
         {#  to be rendeed if the user has been authenticated  #}
    {% endif %}
<body>
</html>
```

### Enfonrcing permissions in URL patterns

To configure the pattern, you use the url() function, in which the permission decorators can be used.

```
from django.conf.urls import url
from django.contrib.auth.decorators import login_required, permission_required

urlpatterns = [
    url(r'^users_only/', login_required(myview)),

    url(r'^category/', permission_required('myapp.change_category', login_url='login')(myview)),
]
```

## Database Config

Let's use MySQL!!

Install the MySQL server, download the installer appropriate for your operating system

```
mysql -u root -p
```

create the database:

```
Create database mydatabase;
```

You will need to install in your project mysql

```
pip3 install mysqlclient
```

On settings.py will need to setup too:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'mydatabase',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
    }
}
```
