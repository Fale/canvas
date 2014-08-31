from django.db import models

class Canvas(models.Model):
    name = models.CharField(max_length = 200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Canvasses"

class Item(models.Model):
    BOXES = (
        ('KP', 'Key Partners'),
        ('KA', 'Key Activities'),
        ('KR', 'Key Resources'),
        ('VP', 'Value Proposition'),
        ('CR', 'Customer Relationships'),
        ('CH', 'Channels'),
        ('CS', 'Customer Segments'),
        ('CSS', 'Cost Structure'),
        ('RSS', 'Revenue Streams'),
    )

    BUNDLES = (
        ('P', 'Product Innovation'),
        ('C', 'Customer Relationship Management'),
        ('I', 'Infrastructure Management'),
    )
    canvas = models.ForeignKey('Canvas', related_name="items", related_query_name="item")
    box = models.CharField(max_length = 3, choices = BOXES)
    bundle = models.CharField(max_length = 1, choices = BUNDLES)
    title = models.CharField(max_length = 200)

    def __str__(self):
        return self.title
