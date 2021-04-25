pip install django
 django-admin startproject demo
 python manage.py runserver
 python manage.py runserver 8888
 python manage.py startapp ourfirstapp

you have to add it in settings.py under installed app
then add it under urls.py
now use like http://127.0.0.1:8000/date/

http://127.0.0.1:8000/ourfirstapp/first


use can use admin also:

python manage.py makemigrations
python  manage.py migrate
python manage.py createsuperuser

