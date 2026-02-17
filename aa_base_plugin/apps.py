"""App configuration"""

# Django
from django.apps import AppConfig
from django.utils.text import format_lazy

# AA Base Plugin
from aa_base_plugin import __title_translated__, __version__


class ExampleConfig(AppConfig):
    """App config"""

    name = "aa_base_plugin"
    label = "aa_base_plugin"
    verbose_name = format_lazy(
        "{app_title} v{version}", app_title=__title_translated__, version=__version__
    )
