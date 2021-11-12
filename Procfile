
web: gunicorn developsnews.wsgi --log-file -
celery: celery -A developsnews.celery worker & celery -A developsnews.celery beat -l INFO & wait -n
