from django.db import models


class Teachers(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField(default=10)
    seniority = models.IntegerField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
