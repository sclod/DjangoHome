import requests

from celery import shared_task 

from .models import Exchange


@shared_task
def get_currency_rates():
    exchange_models = Exchange.objects.all()
    exchange_models.delete()

    exchange_response = requests.get('https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5')
    
    exchange_result = exchange_response.json()
    for rate in exchange_result:
        exchange = Exchange(
            currency=rate.get('ccy'),
            buy_price=rate.get('buy'),
            sell_price=rate.get('sale')
        )
        exchange.save()
    return 'All saved successfully'
