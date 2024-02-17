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
