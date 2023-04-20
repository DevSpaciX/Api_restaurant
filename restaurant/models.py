from django.db import models

from user.models import Employee


class Restaurant(models.Model):
    name = models.CharField(max_length=128)
    address = models.CharField(max_length=128)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Menu(models.Model):
    DAYS_OF_WEEK_CHOICES = (
        (0, "Monday"),
        (1, "Tuesday"),
        (2, "Wednesday"),
        (3, "Thursday"),
        (4, "Friday"),
        (5, "Saturday"),
        (6, "Sunday"),
    )
    users_voted = models.ManyToManyField(Employee, null=True, blank=True)
    daily_menu = models.IntegerField(choices=DAYS_OF_WEEK_CHOICES)
    drink = models.CharField(max_length=128)
    main_dish = models.CharField(max_length=128)
    dessert = models.CharField(max_length=128)
    price = models.PositiveIntegerField()
    restaurant = models.ForeignKey(
        Restaurant, on_delete=models.CASCADE, null=True, related_name="menu"
    )

    def __str__(self):
        return self.main_dish
