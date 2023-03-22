
# A-bit API

## Project Overview

This repository is a the backend of our team project at Northcoders. It's a RESTful API written in Python and using the Django framework alongside PostgreSQL as a database management system and hosted on Render.

A user is able to interact with the databse with the following methods:

* GET a list of all of the users

* GET a list of all the rewards 
* GET a list of all the habits
* GET a list of all the achievements
* GET/PATCH/POST/DELETE a list of all the rewards of a specific user
* GET/PATCH/POST/DELETE a specific reward of an user
* GET/PATCH/POST/DELETE a specific habit of an user
* GET a specific user's achievement
* GET the currency of a specific user

## Hosted Version

You can see a live version of this API, hosted with [Render](https://final-api.onrender.com/)

[Link](https://www.youtube.com/watch?v=iUrSxLPm9Zo&feature=youtu.be) to our presentation (includes a video of the app in action, the tech we used, and challenges we overcame)

The frontend repository for our project can be found [here](https://github.com/crypticalfish86/fe-Habit-Tracker)

## Further Resources
<details>

<summary>Back-end Instructions!</summary>
  

**Disclaimer**: These commands work on **WSL Ubuntu**
   
## Summary
1. Setup
2. Create model in the database
3. Setup Django REST framework
4. Model serialisation
5. Visualisation

# Python Setup
1. Install the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python) in VS code.

2. Install Python by running in Terminal:
```
sudo apt update
sudo apt install python3 python3-pip ipython3
```

Note: you can check your python version by running:
```
python3 --version
```

## Virtual Environment Setup
A virtual environment avoids installing Django into a global Python environment, giving the user exact control over the libraries used in the application.
* Run these commands in the Terminal:
```
sudo apt-get install python3-venv
python3 -m venv .venv
source .venv/bin/activate
```
* Open the Command Palette (View > Command Palette or `Ctrl-⇧-P`) and select
```diff
+ Python: Select Interpreter
```
and choose the virtual environment from the project folder. Example:
```diff
+ Python 3.8.10 ('.venv':venv)
```
## Database Setup
Run the command: 
```
pip install psycopg2-binary
```
Then, create a file called `sql.py`.
```
import psycopg2

conn = psycopg2.connect(
   database="postgres", user='', password='', host='127.0.0.1', port= '5432')
conn.autocommit = True

cursor = conn.cursor()
cursor.execute("DROP DATABASE IF EXISTS database_name")
cursor.execute("CREATE DATABASE database_name")

print("Database created successfully........")

conn.close()
```
# Django Setup
Run the command: 
```
python -m pip install django
```
### **PostgreSQL notes**
PostgreSQL should be already setup with custom user and password.

## Django Project
To open a Python terminal, you can create a `hello.py` file and write
```
print("Hello World")
```
and run the file (clicking the **play** button in the upper-right corner).

In the virtual environment, run the command:
```
django-admin startproject project_name
```
## Django App
Inside the project folder, run the command:
```
python manage.py startapp app_name
```
To check that everything is okay, and to run the server in the future, run the command:
```
python manage.py runserver
```

## PSQL configuration
In the settings.py file of your Project folder, go near line 76 and change the `DATABASES` voice to:
```
DATABASES = {
    'default' : {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'database_name',
        'USER': 'user',
        'PASSWORD': 'pa$$word',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```

# Create a table and import .json data
**DISCLAIMER**: the .json file needs to be in the right format:
```
[
    {
        "model": "app_name.model_name",
        "key": num,
        "fields": {
            "field1": "value1",
            "field2": "value2",
            ...
        }
    }
]
```

1. In the `models.py` file of your App folder, create a new model (PSQL table):
```
class ModelName(models.Model):
    column1 = models.CharField(max_length=50)
    column2 = models.CharField(max_length=50)
    ... (continue with how many you need)
```
2. In the App folder, create a new `load_json.py` file.
```
import json
from django.core.management.base import BaseCommand
from app_folder.models import ModelName

class Command(BaseCommand):
    help = "Load data from a JSON file"

    def add_arguments(self, parser):
        parser.add_argument('json_path', type=str)

    def handle(self, *args, **options):
        with open(options['json_path'], 'r') as f:
            data = json.load(f)

            for obj in data:
                field1 = obj.get('key1')
                ...

                if field 1 and ... :
                my_model = ModelName(**obj)
                my_model.save()
```
3. Back into the settings.py file, edit the `INSTALLED_APPS` voice to register your app, so that it can be included when tools are run (e.g. adding models to the database).

Note: to get the app name, checkout the `apps.py` file!
```
INSTALLED_APPS = [
    ...,
    # Add application
    app_folder_name.apps.app_nameConfig,
]
```
4. Run these commands in the terminal to update the changes in `models.py` (e.g. adding a new table, changing a field name):
```
python manage.py makemigrations
python manage.py migrate
```

5. To load data from `.json`, run the command:
```
python manage.py loaddata path_file.json
```
6. Repeat step 4 whenever needed

**Conclusion**: If you check `psql` in your terminal, you should be able to see your database and your populated table ✅

# API setup
1. Run the command:
```
python manage.py createsuperuser

Username (leave blank to use default):
Email address:
Password:
Password (again):
```
You should get a message `Superuser created successfully`.

2. Register the model in the `admin.py` (App folder):
```
from django.contrib import admin
from .models import ModelName

admin.site.register(ModelName)
```

3. Setup REST framework:
```
pip install djangorestframework
```
and register it in the `INSTALLED_APPS` voice in the settings.py folder (Project folder):
```
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```

4. Serialise the model:
    
    * create a new file `serializers.py` in App folder

```
from rest_framework import serializers
from .models import ModelName

class NameSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
    model = ModelName
    fields = ('column1', ...)
```

5. Render by editing the `views.py` in App folder:
```
from rest_framework import viewsets
from .serializers import NameSerializer
from .models import ModelName

class NameViewSet(viewsets.ModelViewSet):
    queryset = ModelName.objects.all().order_by('whatever')
    serializer_class = NameSerializer
```

6. Setup some URLs:

go to the `urls.py` file (Project folder) and edit it:
```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_folder.urls')),
]
```

create a new `urls.py` file in the App folder and edit it:

```
from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'name', views.NameViewSet)
    
urlpatterns = [
   path('', include(router.urls)),
   path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
```

# Testing
Run the Django server. You'll be able to:
- visit the endpoint via GET
- send a POST request
- checkout the single objects by adding an ID (parametric endpoint)
- DELETE or PATCH that object

</details>
