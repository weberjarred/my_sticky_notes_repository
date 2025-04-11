"""Configures the application."""

from django.apps import AppConfig


class MyNotesAppConfig(AppConfig):
    """
    Configuration class for the 'myNotesApp' Django application.

    This class inherits from Django's AppConfig and is used to define
    application-specific settings such as the default primary key field type
    and the application name.

    Attributes:
        default_auto_field (str): Specifies the type of primary key field to
            use for models in this application by default.
        name (str): The full Python path to the application.
    """
    default_auto_field = "django.db.models.BigAutoField"
    name = "myNotesApp"
