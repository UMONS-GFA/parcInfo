parcInfo
========

A Django app to manage IT park

Requirements
------------

+ Django 1.4 

+ Django-admin 

Setup
-----
add parcInfo to your apps

```
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    'parcInfo',
)
```

run
```
python manage.py syncdb
```

you are good to go !

