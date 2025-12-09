from django.db import models
from django.db.models import CASCADE


class Photo(models.Model):
    link = models.URLField(max_length=255)
    item = models.ForeignKey("Item", on_delete=CASCADE, related_name="photos")

    class Meta:
        db_table = "link"


class Characteristic(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    value = models.CharField(blank=True, null=True)


class Item(models.Model):
    title = models.CharField(max_length=255, blank=True, null=True)
    colour = models.CharField(max_length=255, blank=True, null=True)
    memory = models.CharField(max_length=255, blank=True, null=True)
    price = models.CharField(max_length=255, blank=True, null=True)
    action_price = models.CharField(max_length=255, blank=True, null=True)

    code = models.CharField(max_length=255, blank=True, null=True)
    reviews_count = models.IntegerField(default=0)
    screen_size = models.CharField(max_length=255, blank=True, null=True)
    screen_power = models.CharField(max_length=255, blank=True, null=True)

    characteristics = models.ManyToManyField(
        "Characteristic",
        related_name="items"
    )

    class Meta:
        db_table = "items"
