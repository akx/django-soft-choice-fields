# django-soft-choice-fields

Choice fields that don't record the actual `choices` lists in migrations.

[![Build Status](https://travis-ci.org/akx/django-soft-choice-fields.svg?branch=master)](https://travis-ci.org/akx/django-soft-choice-fields)

## Usage

### Class-based

Derive a subclass from `softchoice.fields.SoftChoiceCharField`
and declare `construct_choices()`:

```python
class NiceChoiceField(SoftChoiceCharField):
    def construct_choices(self):
        return [('a', 'a'), ('b', 'b')]
        
class NiceModel(Model):
    field = NiceChoiceField()
```

### Function-based

Pass a callable in as `choices` to `SoftChoiceCharField`:

```python
def construct_choices(self):
    return [('a', 'a'), ('b', 'b')]
    
class NiceModel(Model):
    field = SoftChoiceCharField(choices=construct_choices)
```

### Soft defaults

By default, soft choice fields also have soft `default`s (i.e. defaults
are also not deconstructed into migrations).

You can override this on a per-field basis by setting `soft_default=False`
in the kwargs, or on the class level, as the class variable `soft_default`:
 
```python
class NiceChoiceField(SoftChoiceCharField):
    soft_default = False

class NiceModel(Model):
    field = SoftChoiceCharField(
        soft_default=False,
        default='foo',  # Will be recorded in migration!
        choices=...  # But these won't.
    )
```

## Predefined fields

The predefined fields make use of several external libraries which are not
hard dependencies:

* For timezone fields, install `pytz`.
* For nicer formatting of language and currency fields, install `babel`.

```python
class User(AbstractUser):
    currency = CurrencyField()
    language = LanguageField()
    timezone = TimezoneField()
```
