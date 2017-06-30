from django.db import models


class Clubs:
    full_name = models.CharField(max_length=150, db_index=True, default="", help_text="Full name of the team.")
    abbrev_name = models.CharField(max_length=15, db_index=True, default="", help_text="Abbreviated name of the team (THFC).")
    country_affiliation = models.ForeignKey("fbStore.competitions.Countries", related_name="club", null=True, on_delete=models.SET_NULL,
                               help_text= "The country that club belongs to.")
    league_affiliation = models.ForeignKey("fbStore.environment.Leagues", related_name="club", null=True, on_delete=models.SET_NULL,
                               help_text= "The league that club belongs to.")
    city_affiliation = models.ForeignKey("fbStore.environment.Cities", related_name="club", null=True, on_delete=models.SET_NULL,
                                         help_text="The city a clubs in.")
    stadium = models.CharField(max_length=150, help_text="The stadium a club plays at.")


class Players:
    first_name = models.CharField(max_length=150, db_index=True, default="", help_text="Player first name.")
    last_name = models.CharField(max_length=150, db_index=True, default="", help_text="Player last name.")
    club = models.ForeignKey("Clubs", related_name="player", null=True, on_delete=models.SET_NULL,
                                         help_text="The club a player plays")
    country = models.ForeignKey("fbStore.environment.Countries", related_name="player", null=True, on_delete=models.SET_NULL,
                             help_text="The country a player is from (home)")
    international_team = models.ForeignKey("fbStore.environment.Countries", related_name="player", null=True, on_delete=models.SET_NULL,
                             help_text="The country a player plays for (USMNT)")


class Managers:
    first_name = models.CharField(max_length=150, db_index=True, default="", help_text="Manager first name.")
    last_name = models.CharField(max_length=150, db_index=True, default="", help_text="Manager last name.")
    country = models.ForeignKey("fbStore.environment.Countries", related_name="manager", null=True, on_delete=models.SET_NULL,
                                help_text="The country a manager is from (home)")
    # could be null if intl manager
    club = models.ForeignKey("Clubs", related_name="player", null=True, on_delete=models.SET_NULL,
                             help_text="The club a player plays")
    # could be null if manger does not manage intl team
    international_team = models.ForeignKey("fbStore.environment.Countries", related_name="player", null=True, on_delete=models.SET_NULL,
                                           help_text="The country a player plays for (USMNT)")
