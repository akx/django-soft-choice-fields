from django.core.exceptions import ImproperlyConfigured

from . import SoftChoiceCharField


class TimezoneField(SoftChoiceCharField):
    # TODO: add locale support to .formfield()
    def __init__(self, **kwargs):
        if 'timezones' not in kwargs:
            try:
                import pytz
                kwargs['timezones'] = pytz.common_timezones
            except ImportError:  # pragma: no cover
                raise ImproperlyConfigured('either declare `timezones` for %r or install `pytz`' % self)
        self.timezones = kwargs.pop('timezones', ())
        kwargs.setdefault('max_length', 65)
        super(TimezoneField, self).__init__(**kwargs)

    def construct_choices(self):
        return [(tz, tz.replace("_", " ")) for tz in self.timezones]
