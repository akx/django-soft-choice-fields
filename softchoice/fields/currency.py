from . import SoftChoiceCharField

try:
    import babel

    currency_names = babel.Locale('en').currencies
except ImportError:  # pragma: no cover
    currency_names = {}


class CurrencyField(SoftChoiceCharField):
    # TODO: add locale support to .formfield()
    def __init__(self, **kwargs):
        self.currencies = kwargs.pop('currencies', ('EUR',))
        kwargs.setdefault('max_length', 3)
        super(CurrencyField, self).__init__(**kwargs)

    def construct_choices(self):
        return [(code, currency_names.get(code, code)) for code in self.currencies]
