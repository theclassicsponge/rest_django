from django.db import models

# Create your models here.

currency = {
    ('GBP', 'Pounds'),
    ('USD', 'Dollars'),
    ('EUR', 'Euros')
}


class UserData(models.Model):
    username = models.CharField(max_length=100, unique=True, primary_key=True)
    bio = models.TextField(max_length=280)
    website_link_1 = models.URLField(max_length=200, null=True, blank=True)
    website_link_2 = models.URLField(max_length=200, null=True, blank=True)
    website_link_3 = models.URLField(max_length=200, null=True, blank=True)
    profile_pic = models.URLField(max_length=200, null=True, blank=True)
    currency = models.CharField(max_length=3, choices=currency)

    class Meta:
        ordering = ['username']


    # add later:
    # select_price_tiers =
    # price_tiers =
    # max_price =
    # min_price =
    # donor_choose_price =
    # social_media_link =
