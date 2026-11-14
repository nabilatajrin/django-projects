from django.db import models


class Weight(models.Model):
    date = models.DateField()
    max_weight = models.IntegerField()
    min_weight = models.IntegerField()

    def __str__(self):
        return str(self.date)
