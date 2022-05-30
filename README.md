# djangohome

### Startup

pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

### Running celery

celery -A student_records worker -l debug --concurrency 1 -P solo
celery -A student_records beat -l info --concurrency 1 -P solo

##