from django.db import models


class Visitors(models.Model):
    counter = models.IntegerField(default=0)

    def increase_count(self):
        self.counter += 1
        self.save()
