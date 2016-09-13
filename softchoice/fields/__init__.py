from django.db import models


class SoftChoiceMixin(object):
    soft_default = True

    def __init__(self, **kwargs):
        self.soft_default = bool(kwargs.pop('soft_default', self.soft_default))
        if callable(kwargs.get('choices')):
            self.construct_choices = kwargs['choices']
        kwargs['choices'] = list(self.construct_choices())
        super(SoftChoiceMixin, self).__init__(**kwargs)

    def construct_choices(self):  # pragma: no cover
        return []

    def deconstruct(self):  # pragma: no cover
        # only run when creating migrations, so no-cover
        name, path, args, kwargs = super(SoftChoiceMixin, self).deconstruct()
        kwargs.pop('choices', None)
        if self.soft_default:
            kwargs.pop('default', None)
        return (name, path, args, kwargs)


class SoftChoiceCharField(SoftChoiceMixin, models.CharField):
    pass
