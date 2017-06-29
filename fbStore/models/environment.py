# environments.py will hold useful multipurpose
# environmental variables in the football world

# todo: create game and date models

from django.db import models


class Year:
    year = models.IntegerField(primary_key=True, help_text="Year (primary key)", max_length=4)


class Region:
    name = models.CharField(max_length=50, help_text="Name of region")
    abbreviation = models.CharField(max_length=15, default="", help_text="Region abbreviations")


class Country:
    name = models.CharField(max_length=100, help_text="Name of country")
    abbreviation = models.CharField(max_length=15, help_text="Country abbreviation")
    regional_association = models.ForeignKey("fbStore.world.FootballAssociation",related_name="country", null=True,
                                             on_delete=models.SET_NULL, help_text= "The football association for that state.")

