# django-soft-choice-fields

Choice fields that don't record the actual `choices` lists in migrations.

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
