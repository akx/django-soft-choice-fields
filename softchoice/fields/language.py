from django.conf import settings
from django.core.exceptions import ImproperlyConfigured
from django.utils.six import string_types

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
        kwargs.setdefault('default', getattr(settings, 'LANGUAGE_CODE', None))
        self.languages = kwargs.pop('languages', None)
        if self.languages is None:
            self.languages = [code for (code, name) in settings.LANGUAGES]
        self.languages = list(self.languages)
        if not all(isinstance(code, string_types) for code in self.languages):
            raise ImproperlyConfigured(
                '`languages` must be a list of language codes (strings)'
            )
        if not all(len(code) <= kwargs['max_length'] for code in self.languages):
            raise ImproperlyConfigured(
                'not all languages fit in max_length=%d characters' % kwargs['max_length']
            )
        super(LanguageField, self).__init__(**kwargs)

    def construct_choices(self):
        return [(code, language_names.get(code, code)) for code in self.languages]
