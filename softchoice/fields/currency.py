from django.core.exceptions import ImproperlyConfigured
from django.utils.six import string_types

from . import SoftChoiceCharField

try:
    import babel

    currency_names = babel.Locale('en').currencies
except ImportError:  # pragma: no cover
    currency_names = {}


class CurrencyField(SoftChoiceCharField):
    # TODO: add locale support to .formfield()

    def __init__(self, **kwargs):
        self.currencies = list(kwargs.pop('currencies', ('EUR',)))
        if not all(isinstance(code, string_types) for code in self.currencies):
            raise ImproperlyConfigured(
                '`currencies` must be a list of currency codes (strings)'
            )
        kwargs.setdefault('max_length', 3)
        super(CurrencyField, self).__init__(**kwargs)

    def construct_choices(self):
        return [(code, currency_names.get(code, code)) for code in self.currencies]
