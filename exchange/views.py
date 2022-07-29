from re import I
from tkinter import E
from django.shortcuts import render
from .models import Exchange

from django.http import HttpResponse

from .models import Exchange

def list_exchange_rates(request):
    exchange_result = Exchange.objects.all()
    return HttpResponse(exchange_result)

def currency_table(request):
    exchange_result = Exchange.objects.all()
    return render(request, 'exchange/currency.html', {
        'currencyUSD': exchange_result[0].currency,
        'currencyEUR': exchange_result[1].currency,
        'currencyBTC': exchange_result[2].currency,
        'buyUSD': exchange_result[0].buy_price,
        'buyEUR': exchange_result[1].buy_price,
        'buyBTC': exchange_result[2].buy_price,
        'sellUSD': exchange_result[0].sell_price,
        'sellEUR': exchange_result[1].sell_price,
        'sellBTC': exchange_result[2].sell_price,
        }
    )
