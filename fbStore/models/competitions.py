from django.db import models


class Tournaments:
    full_name = models.CharField(max_length=150, db_index=True, default="", help_tex="Full name of the tournamemnt.")
    abbrev_name = models.CharField(max_length=15, db_index=True, default="", help_text="Abbreviated name of the tournament.")
    associated_league = models.ForeignKey("fbStore.competitions.Leagues", related_name="tournament", null=True,
                                             on_delete=models.SET_NULL, help_text= "Associated league.")
    associated_country = models.ForeignKey("fbStore.environment.Countries", related_name="tournament", null=True,
                                             on_delete=models.SET_NULL, help_text= "Associated country.")
    associated_org = models.ForeignKey("fbStore.world.FootballAssociations", related_name="tournament", null=True,
                                             on_delete=models.SET_NULL, help_text= "The governing org.")


class Leagues:
    full_name = models.CharField(max_length=150, db_index=True, default="", help_text= "Full name of the league.")
    abbrev_name = models.CharField(max_length=15, db_index=True, default="", help_text="Abbreviated name of the ;eague.")
    associated_country = models.ForeignKey("fbStore.environment.Countries", related_name="league", null=True,
                                             on_delete=models.SET_NULL, help_text= "Associated country.")