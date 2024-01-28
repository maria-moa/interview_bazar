#! /bin/sh
python manage.py collectstatic --noinput
sleep 3  # be sure db is ready to listen
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser --noinput --username admin --email admin@me.com
gunicorn -c gunicorn_conf.py bazar.wsgi
