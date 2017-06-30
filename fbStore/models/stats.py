from django.db import models


class PlayerStats:
    player = models.ForeignKey("fbStore.agents.Players")


class ManagerStats:
    manager = models.ForeignKey("fbStore.agents.Managers")


class Results:
    club_a = models.ForeignKey("fbStore.agents.Clubs")
    club_b = models.ForeignKey("fbStore.agents.Clubs")
    winner = models.ForeignKey("fbStore.agents.Clubs")
    year = models.ForeignKey("fbStore.environment.Years", related_name="result", help_text="Year of game")
    date = models.DateField(null=True, help_text="Date of game")
    a_score = models.IntegerField(max_length=2, help_text="Club A score")
    b_score = models.IntegerField(max_length=2, help_text="Club B score")