from datetime import datetime, date
from celery import shared_task
import datetime

from restaurant.models import Menu
from restaurant.models import Restaurant


@shared_task
def clear_votes_and_users():
    now = datetime.datetime.now()
    day_of_week = now.weekday()
    menu = Menu.objects.filter(daily_menu=day_of_week)
    for item in menu:
        item.users_voted.clear()
        item.save()
    restaurant = Restaurant.objects.filter(menu__daily_menu=day_of_week)
    for item in restaurant:
        item.votes = 0
        item.save()
