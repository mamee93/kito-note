
import os
import dj_database_url
from .settings import *
SECRET_KEY = os.environ.get('SECRET_KEY')
# DEBUG = FalseT
ALLOWED_HOSTS = ['kito-note.herokuapp.com']


DATABASES = {
    'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))

    

}
