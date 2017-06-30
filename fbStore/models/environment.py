# environments.py will hold useful multipurpose
# environmental variables in the football world

# todo: create game and date models

from django.db import models


class Years:
    year = models.IntegerField(primary_key=True, help_text="Year (primary key)", max_length=4)


class Regions:
    full_name = models.CharField(max_length=50, help_text="Name of region")
    abbreviation = models.CharField(max_length=15, default="", help_text="Region abbreviations")


class Countries:
    full_name = models.CharField(max_length=100, help_text="Name of country")
    abbreviation = models.CharField(max_length=15, help_text="Country abbreviation")
    regional_association = models.ForeignKey("fbStore.world.FootballAssociations", related_name="country", null=True,
                                             on_delete=models.SET_NULL, help_text="The football association for that state.")


class Cities:
    full_name = models.CharField(max_length=150, help_text="Name of city")
    country = models.ForeignKey(Countries, elated_name="city", null=True, on_delete=models.SET_NULL,
                                help_text="The country a city is in")
