from django.db import models


class SoftChoiceMixin(object):
    def __init__(self, **kwargs):
        if callable(kwargs.get('choices')):
            self.construct_choices = kwargs['choices']
        kwargs['choices'] = self.construct_choices()
        super(SoftChoiceMixin, self).__init__(**kwargs)

    def construct_choices(self):  # pragma: no cover
        return []

    def deconstruct(self):  # pragma: no cover
        # only run when creating migrations, so no-cover
        name, path, args, kwargs = super(SoftChoiceMixin, self).deconstruct()
        kwargs.pop('choices', None)
        return (name, path, args, kwargs)


class SoftChoiceCharField(SoftChoiceMixin, models.CharField):
    pass
