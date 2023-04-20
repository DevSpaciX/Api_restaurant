import asyncio
from datetime import datetime, date
from django.utils.timezone import now
from celery import shared_task


@shared_task
def clear_votes_and_users():
    print("Hello")