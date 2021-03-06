import pytest
from django.core.exceptions import ImproperlyConfigured
from django.forms.fields import ChoiceField
from django.utils.encoding import force_text

from softchoice.fields import SoftChoiceMixin
from softchoice.fields.language import LanguageField
from tests.models import Dummy


def test_deconstruction():
    """
    Test that deconstructions for soft choice fields don't include the `choices=` kwarg.
    """
    for field in Dummy._meta.get_fields():
        if isinstance(field, SoftChoiceMixin):
            kwargs = field.deconstruct()[3]
            assert 'choices' not in kwargs
            assert 'default' not in kwargs


@pytest.mark.parametrize('field', [
    'currency',
    'language',
    'timezone',
])
def test_field(field):
    m = Dummy()
    formfield = m._meta.get_field(field).formfield()
    assert isinstance(formfield, ChoiceField)
    assert len(formfield.choices)


def test_language_validation():
    with pytest.raises(ImproperlyConfigured):
        LanguageField(languages=['neenerneenerneener'])


@pytest.mark.django_db
def test_admin(admin_client):
    content = force_text(admin_client.get('/admin/tests/dummy/add/', follow=True).content)
    assert 'Finnish' in content
    assert 'English' in content
    assert 'Swedish' in content
    assert 'oooooooooooo' in content
    assert 'America/Chihuahua' in content  # it's apparently a common timezone


@pytest.mark.parametrize('soft', (False, True))
def test_soft_default(soft):
    nsd_language_field = LanguageField(soft_default=soft, default='en')
    kwargs = nsd_language_field.deconstruct()[3]
    assert 'choices' not in kwargs
    if soft:
        assert 'default' not in kwargs
    else:
        assert kwargs['default'] == 'en'
