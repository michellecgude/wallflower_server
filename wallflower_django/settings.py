from pathlib import Path
import os
import dotenv
import django_heroku
import dj_database_url
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
exit()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Add .env variables anywhere before SECRET_KEY
dotenv_file = os.path.join(BASE_DIR, ".env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True if os.environ['MODE'] == 'dev' else False
DEBUG = False

# ALLOWED_HOSTS = ['*']

# Specifies localhost port 3000 where the React
# server will be running is safe to receive requests
# from.
# DONT FORGET TO CHANGE THIS/ADD THE HEROKU DEPLOYED FRONTEND LINK!

# CORS_ALLOWED_ORIGINS = [    
# 'http://localhost:3000'
# ]

# the following is temporary until you showcase your frontend 
CORS_ALLOW_ALL_ORIGINS = True

# Application definition
INSTALLED_APPS = [
    # INSTALLED APPS
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # THIRD PARTY APPS
    'rest_framework', 
    'rest_framework.authtoken', 
    'rest_auth', 
    'django.contrib.sites', 
    'django_extensions',
    'djoser',
    'allauth', 
    'allauth.account', 
    'allauth.socialaccount', 
    'rest_auth.registration', 
    'corsheaders', 
    # LOCAL APPS
    'wallflower',
]

# Configure Django App for Heroku.
django_heroku.settings(locals())

# Django All Auth config. Add all of this.
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

SITE_ID = 1 
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_SESSION_REMEMBER = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_UNIQUE_EMAIL = True

# Rest Framework config.
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
   	# or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': ['rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'],
    'DATETIME_FORMAT': "%m/%d/%Y %I:%M%P",
    'DEFAULT_AUTHENTICATION_CLASSES': ['rest_framework.authentication.TokenAuthentication',],
}


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # 'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'wallflower_django.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'wallflower_django.wsgi.application'



# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'wallflower',
        'USER': 'wallfloweruser',
        'PASSWORD': 'wallflower',
        'HOST': 'localhost'
    }
}

# DATABASES = {
#     'default': dj_database_url.config(conn_max_age=600)
# }

# DATABASE_URL=postgres://wallfloweruser:wallflower@localhost:8000/wallflower


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

# Whitenoise pckg to help serving static files
# The URL to use when referring to static files (where they will be served from)
# STATIC_URL = 'static/css/style.css/'

# # The absolute path to the directory where collectstatic will collect static files for deployment.
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# # Extra places for collectstatic to find static files.
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static'),
# )

# # Simplified static file serving.
# # https://warehouse.python.org/project/whitenoise/
# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Profile via Abstract User Auth
# https://docs.djangoproject.com/en/3.1/topics/auth/customizing/#substituting-a-custom-user-model
AUTH_USER_MODEL = 'wallflower.User'
