import os
from pathlib import Path
from django.contrib import messages

from dotenv import load_dotenv
load_dotenv('all_passwords.env')
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = True
ALLOWED_HOSTS = ['swdc.pythonanywhere.com', '127.0.0.1']
CSRF_TRUSTED_ORIGINS = ['https://swdc.pythonanywhere.com', 'http://127.0.0.1']
CSRF_FAILURE_VIEW  = 'SWDCWebsite.views.csrf_error_handler'
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'authentication',
    'Volunteer',
    'Coordinator',
    'Secretary',
    'action',
    'django_recaptcha',
    'django_user_agents',
]
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django_user_agents.middleware.UserAgentMiddleware',
]

ROOT_URLCONF = 'SWDCWebsite.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'SWDCWebsite/templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
WSGI_APPLICATION = 'SWDCWebsite.wsgi.application'
DATABASES = {
    'default': {
        'ENGINE': os.getenv('DATABASE_ENGINE'),
        'NAME': BASE_DIR /os.getenv('DATABASE_NAME'),
    }
}
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


#Activity Divisions
DIVISIONS = {
    "Utkarsh": ["CS-J", "CS-K"],
    "Matadhikar": ["CS-A", "CS-B", "CS-C", "CS-D"],
    "Muskaan": ["CSSE-C"],
    "Udaan": ["CSDS-A"],
    "Saksham": ["CSDS-B"],
    "Aashakiran": ["CS-L", "IT-F"],
    "Aavishkar": ["CSDS-C", "CS-I"],
    "Vatsalya": ["IT-E"],
    "Aadhar": ["CSSE-A", "CSSE-B"],
    "Swaccha Pune": ["CS-E", "CS-F", "CS-G", "CS-H", "IC-A", "IC-B", "IC-C"],
    "Go Green": ["IT-A", "IT-B", "IT-C", "IT-D", "CSCBI-A", "CSCBI-B", "CSCBI-C"],
    "Night Patrolling": ["CSDS-A"]
}

GROUPS = {
    "Utkarsh": ["1-15", "16-30", "31-45", "46-60", "61-78"],
    "Matadhikar": ["1-15", "16-30", "31-45", "46-60"],
    "Muskaan": [],
    "Udaan": ["1-23", "24-34", "35-46", "47-69"],
    "Saksham": [],
    "Aashakiran": [],
    "Aavishkar": ["1-26", "27-54", "55-78"],
    "Vatsalya": ["1-11", "12-22", "23-33", "34-44", "45-55", "56-66", "67-77"],
}



MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
MESSAGE_TAGS = {messages.ERROR: 'danger'}
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = os.getenv('EMAIL_HOST_USER')
EMAIL_PORT = os.getenv('EMAIL_PORT')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')
SESSION_COOKIE_AGE = 17000
CSRF_COOKIE_AGE = 17000
RECAPTCHA_PUBLIC_KEY = os.getenv('RECAPTCHA_PUBLIC_KEY')
RECAPTCHA_PRIVATE_KEY = os.getenv('RECAPTCHA_PRIVATE_KEY')