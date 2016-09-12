from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

from . import SoftChoiceCharField

try:
    import babel

    language_names = babel.Locale('en').languages
except ImportError:  # pragma: no cover
    language_names = dict(settings.LANGUAGES)


class LanguageField(SoftChoiceCharField):
    # TODO: add locale support to .formfield()
    def __init__(self, **kwargs):
        kwargs.setdefault('max_length', 10)
        self.languages = kwargs.pop('languages', settings.LANGUAGES)
        if not all(len(code) <= kwargs['max_length'] for code in self.languages):
            raise ImproperlyConfigured(
                'not all languages fit in max_length=%d characters' % kwargs['max_length']
            )
        super(LanguageField, self).__init__(**kwargs)

    def construct_choices(self):
        return [(code, language_names.get(code, code)) for code in self.languages]
