# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'hy#x2vf70*hgk9wfbgw1rqd4gwkjdn%i0hp2=!=eml_^#*p)4v'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'sports_engine2',
        'USER': 'hrumba',
        'PASSWORD': '',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
