from Project.settings.base_settings import *
import os
from dotenv import load_dotenv
load_dotenv()

SECRET_KEY = str(os.getenv("SECRET_KEY"))
DEBUG = True,
DJANGO_ALLOWED_HOSTS= ['localhost', '127.0.0.1']
DATABASES =  {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'habit_tracker_db',
        'USER': '',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',
    }
 }



