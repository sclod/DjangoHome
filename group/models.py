from django.db import models


class Group(models.Model):
    name_group = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f'{self.name_group}'
