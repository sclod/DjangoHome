from re import I
from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import Teachers


@receiver(pre_save, sender=Teachers)
def teacher_edit_handler(sender, **kwargs):
    last_name = kwargs['instance'].last_name
    first_name = kwargs['instance'].first_name
    #phone = kwargs['instance'].phone
    kwargs['instance'].last_name = str(last_name.capitalize())
    kwargs['instance'].first_name = str(first_name.capitalize())
    #kwargs['instance'].phone = int(phone.strip('').replace('+', '').replace('(', '').replace(')', ''))