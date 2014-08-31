from django.db import models

class Canvas(models.Model):
    name = models.CharField(max_length = 200)

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
    canvas = models.ForeignKey('Canvas')
    box = models.CharField(max_length = 3, choices = BOXES)
    bundle = models.CharField(max_length = 1, choices = BUNDLES)
    title = models.CharField(max_length = 200)
