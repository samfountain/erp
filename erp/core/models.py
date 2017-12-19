from django.db import models


class TimeStampedModel(models.Model):
    """
    Base model to add created date time and modified date time
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Address(TimeStampedModel):
    """
    System wide addresses
    """

