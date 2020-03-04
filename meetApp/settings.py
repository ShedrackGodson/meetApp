import os


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'cjnwtz!5c=ujck1(pz2-mn36s+ja-u(3!u_5yrp1+m=c9gpdqc'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home',
    'users',
    'widget_tweaks',
    'social_django',
    'tempus_dominus',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',
]

AUTHENTICATION_BACKENDS = (
    # 'social_core.backends.github.GithubOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
    'django.contrib.auth.backends.ModelBackend',
)

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    'social.pipeline.user.user_details',
    # 'users.pipeline.save_profile',
)

ROOT_URLCONF = 'meetApp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'meetApp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

# MySQL DB
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'meetapp',
        'HOST': 'localhost',
        'PASSWORD': 'magnifico23',
        'USER': 'root'
    }
}



# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media_root')
MEDIA_URL = '/media/'

STATICFILES_DIRS = [os.path.join(
    BASE_DIR, 'static'), os.path.join(BASE_DIR, 'media')]


LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = 'home' # Redirection link when user logged in
LOGOUT_URL = 'logout'
LOGOUT_REDIRECT_URL = 'login' 

# Facebook Auth
SOCIAL_AUTH_FACEBOOK_KEY = '123931219060215'  # App ID
SOCIAL_AUTH_FACEBOOK_SECRET = 'b07dc7039c6c586c8b3b2eaf82a0ca5d' # secret key
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
  'fields': 'id, name, email, picture.type(large), link'
}
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email', 'user_link']

SOCIAL_AUTH_FACEBOOK_EXTRA_DATA = [
    ('name', 'name'),
    ('email', 'email'),
    ('picture', 'picture'),
    ('link', 'profile_url'),
]

# Twitter Auth
SOCIAL_AUTH_TWITTER_KEY = '1eb9CmB5u6W5QweJIwa3lpiIK'
SOCIAL_AUTH_TWITTER_SECRET = 'IEj7hNw435j6PeZ9yYeIfRcffsV5YEYjTCZc1oTHOSC0zlKXZb'
TWITTER_EXTRA_DATA = [('profile_image_url','profile_picture')]

# Google+ Auth
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '842550580760-4v9eimd2hekkmf5kmdusbc79jl27340o.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'XW_oq6BIADnECw5ti8PZYb7C'

SOCIAL_AUTH_LOGIN_ERROR_URL = '/settings/'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/settings/'
SOCIAL_AUTH_RAISE_EXCEPTIONS = False

#Tempus Dominus
TEMPUS_DOMINUS_INCLUDE_ASSETS = True
TEMPUS_DOMINUS_LOCALIZE = False