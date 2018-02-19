from django.db import models
from erp.core.models import TimeStampedModel


class Country(TimeStampedModel):
    """
    Country model holding the country code and name of country
    """
    code = models.CharField(max_length=2)
    name = models.CharField(max_length=40, unique=True)

    class Meta:
        verbose_name_plural = 'Countries'

    def __str__(self):
        return '{} {}'.format(self.code, self.name)


class State(TimeStampedModel):
    """
    State model, holding the state name, code, and the related country
    """
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=165)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='states')

    def __str__(self):
        return self.name


class Suburb(TimeStampedModel):
    """
    Suburb model, containing name of suburb and the related state of the suburb 
    """
    name = models.CharField(max_length=165)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='suburbs')

    def __str__(self):
        return self.name


class PostCode(TimeStampedModel):
    """
    Postcode model, containing the post code and the state in which it resides
    """
    post_code = models.CharField(max_length=10)
    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='post codes')

    def __str__(self):
        return self.post_code


class Address(TimeStampedModel):
    """
    Address model, containing the street (number and street name, including unit/apartment number etc.)
    as well as the related suburb, post code, state and country
    """
    street = models.CharField(max_length=255)
    suburb = models.ForeignKey(Suburb, on_delete=models.PROTECT)
    post_code = models.ForeignKey(PostCode, on_delete=models.PROTECT)
    state = models.ForeignKey(State, on_delete=models.PROTECT)
    country = models.ForeignKey(Country, on_delete=models.PROTECT)

    class Meta:
        verbose_name_plural='Addresses'

    def __str__(self):
        return '{} \n {} {} {} {}'.format(self.street, self.suburb, self.state, self.post_code, self.country)

