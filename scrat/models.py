from django.db import models


class Photo(models.Model):
    link = models.URLField()

    class Meta:
        db_table = "link"


class Characteristic(models.Model):
    name = models.CharField()
    value = models.CharField(blank=True, null=True)


class Item(models.Model):
    title = models.CharField()
    colour = models.CharField()
    memory = models.CharField()
    price = models.DecimalField(max_digits=16, decimal_places=2)
    action_price = models.DecimalField(max_digits=16, decimal_places=2, blank=True, null=True)

    photo_links = models.ManyToManyField(
        "Photo",
        related_name="items"
    )

    code = models.CharField()
    reviews_count = models.IntegerField(default=0)
    screen_size = models.CharField()
    characteristics = models.ManyToManyField(
        "Characteristic",
        related_name="items"
    )

    class Meta:
        db_table = "items"
