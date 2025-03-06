#!/usr/bin/env python
"""
Django's command-line utility for administrative tasks.
This module allows for interaction with the Django project.
→ Sets the default settings module to the project's settings module.
→ Uses defensive error reporting if Django isn’t installed.

No modifications are made in this file.
"""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE", "sticky_notes_project.settings"
    )
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
