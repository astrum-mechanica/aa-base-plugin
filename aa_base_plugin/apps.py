# Django
from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _

# Fleet Dash
# AA Base Plugin
from aa_base_plugin import __version__


class ExampleConfig(AppConfig):
    name = "aa_base_plugin"
    label = "aa_base_plugin"
    verbose_name = _(f"AA Base Plugin v{__version__}")
