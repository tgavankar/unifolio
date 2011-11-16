from django.db import models
from django.db.models.signals import pre_delete


def delete_files_for_obj(sender, **kwargs):
    """Signal receiver of a model class and instance. Deletes its files."""
    obj = kwargs.pop('instance')
    for field_name in sender._meta.get_all_field_names():
        # Skip related models' attrs.
        if not hasattr(obj, field_name):
            continue
        # Get the class and value of the field.
        field_class = sender._meta.get_field(field_name)
        field_value = getattr(obj, field_name)
        # Check if it's a FileField instance and the field is set.
        if isinstance(field_class, models.FileField) and field_value:
            field_value.delete()


def auto_delete_files(cls):
    """Deletes all FileFields when model instances are deleted.

    Meant to be used on model classes.
    Django disabled auto-deletion of files when deleting a model in
    ticket #6456, to prevent dataloss.

    """
    pre_delete.connect(delete_files_for_obj, sender=cls)
    return cls
