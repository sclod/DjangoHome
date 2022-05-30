from django.db import models
from .choices import CURRENCIES


class Exchange(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    currency = models.CharField(max_length=4)
    source = models.CharField(max_length=20, default='privatbank')
    buy_price = models.DecimalField(max_digits=19, decimal_places=2)
    sell_price = models.DecimalField(max_digits=19, decimal_places=2)

    def __str__(self):
        return f'{self.created_at}::{self.currency}, {self.source}, BUY: {self.buy_price} SELL: {self.sell_price}'