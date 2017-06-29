# world.py will hold data that is attributed to football at the global level
# examples of such are world football associations (FIFA, UEFA, etc.), countries, etc.

from django.db import models


class IntlOrg:
    full_name = models.CharField(max_length=150, db_index=True, default="", help_text= "Full name of the organization.")
    abbrev_name = models.CharField(max_length=15, db_index=True, default="", help_text="Abbreviated name of the org.")


class FootballAssociation:
    full_name = models.CharField(max_length=150, db_index=True, default="", help_text= "Full name of the organization.")
    abbrev_name = models.CharField(max_length=15, db_index=True, default="", help_text="Abbreviated name of the org.")
    region = models.ForeignKey("fbStore.environment.Region", related_name="association", null=True, on_delete=models.SET_NULL,
                               help_text= "The region that association represents.")
    gov_org = models.ForeignKey("fbStore.world.IntlOrg", related_name="asspciation", null=True, on_delete=models.SET_NULL,
                                help_text="The intl governing body.")