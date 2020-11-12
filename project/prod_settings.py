
import os
import dj_databas_url
from .settings import *
SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = False
ALLOWED_HOSTS = ['kito-note.herokuapp.com']


DATABASES = {
    'default': dj_databas_url.config(default=os.environ.get('DATABASE_URL'))

    

}
