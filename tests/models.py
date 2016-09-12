from django.db import models

from softchoice.fields import SoftChoiceCharField
from softchoice.fields.currency import CurrencyField
from softchoice.fields.language import LanguageField
from softchoice.fields.timezone import TimezoneField


def generate_choices():
    for x in range(10):
        yield [str(x), 'oo' * x]


class Model(models.Model):
    currency = CurrencyField(currencies=['EUR', 'USD', 'JPY'])
    language = LanguageField(languages=['en', 'fi', 'sv'])
    timezone = TimezoneField()
    custom = SoftChoiceCharField(max_length=20, choices=generate_choices)
