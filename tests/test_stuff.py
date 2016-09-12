import pytest
from django.core.exceptions import ImproperlyConfigured
from django.db.migrations.autodetector import MigrationAutodetector
from django.db.migrations.loader import MigrationLoader
from django.db.migrations.state import ProjectState
from django.apps import apps
from django.db.migrations.writer import MigrationWriter
from django.forms.fields import ChoiceField

from softchoice.fields.language import LanguageField
from tests.models import Model


def test_migration():
    """
    Test that migrations for soft choice fields don't include the `choices=` kwarg.
    """
    loader = MigrationLoader(None, ignore_no_migrations=True)
    autodetector = MigrationAutodetector(
        loader.project_state(),
        ProjectState.from_apps(apps),
    )
    changes = autodetector.changes(
        graph=loader.graph,
    )
    writer = MigrationWriter(changes['tests'][0])
    migration_string = writer.as_string()
    assert b'choices=' not in migration_string


@pytest.mark.parametrize('field', [
    'currency',
    'language',
    'timezone',
])
def test_field(field):
    m = Model()
    formfield = m._meta.get_field(field).formfield()
    assert isinstance(formfield, ChoiceField)
    assert len(formfield.choices)


def test_language_validation():
    with pytest.raises(ImproperlyConfigured):
        LanguageField(languages=['neenerneenerneener'])
