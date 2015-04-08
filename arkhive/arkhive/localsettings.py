DB_REL = 'default'
DB_NONREL = 'arkhive_nonrel'

DATABASES = {
    DB_REL: {
        'NAME': 'arkhive',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'root',
        'PASSWORD': 'pass123'
    },

    DB_NONREL: {
        'NAME': 'arkhive',
        'ENGINE' : 'django_mongodb_engine',
    }
}
