from django.db.models import TextChoices


class Book(TextChoices):
    DAILY = 'Booking daily'
    HOURLY = 'Booking hourly'


class RoomType(TextChoices):
    LUX = 'Lux'
    BUSINESS = 'Business'
    ACTUAL = 'Actual'
