# Case-Study-Backend

pip install --upgrade  -r requirements.txt

After that command create a Database and add them in setting.py

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'casestudy',
        'USER': 'yourusername',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

#Migrations
python manage.py makemigrations
python manage.py migrate
