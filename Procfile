release: python manage.py migrate --no-input --settings=chs_weather.production
web: gunicorn chs_weather.wsgi --log-file -