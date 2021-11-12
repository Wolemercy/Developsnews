from celery import shared_task
from api.models import Vote


@shared_task
def refresh_votes():
    Vote.objects.all().delete()
    return "Votes successfully reset"
