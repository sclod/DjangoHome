from re import L
from django.urls import path

from exchange.views import list_exchange_rates, currency_table


urlpatterns = [
    path('exchange/', list_exchange_rates),
    path('currency/', currency_table, name='currency-table')
]