from Project.settings.base_settings import *
import dj_database_url
import os
from dotenv import load_dotenv
load_dotenv()

SECRET_KEY = str(os.getenv("SECRET_KEY"))
DEBUG = False
ALLOWED_HOSTS = ['host-test-yju8.onrender.com', 'final-api.onrender.com', 'authentication-test-7108.onrender.com' ]
DATABASES = {
    'default': dj_database_url.parse(os.environ.get('DATABASE_URL'), conn_max_age=600)
}

