from django.utils.translation import gettext_lazy as _

from allianceauth import hooks
from allianceauth.services.hooks import MenuItemHook, UrlHook

from aa_base_plugin import __title__


from . import urls


class ExampleMenuItem(MenuItemHook):
    """This class ensures only authorized users will see the menu entry"""

    def __init__(self):
        # setup menu entry for sidebar
        MenuItemHook.__init__(
            self,
            __title__,
            "fas fa-cube fa-fw",
            "aa_base_plugin:index",
            navactive=["aa_base_plugin:"],
        )

    def render(self, request):
        if request.user.has_perm("aa_base_plugin.basic_access"):
            return MenuItemHook.render(self, request)
        return ""


@hooks.register("menu_item_hook")
def register_menu():
    return ExampleMenuItem()


@hooks.register("url_hook")
def register_urls():
    return UrlHook(urls, "aa_base_plugin", r"^aa_base_plugin/")
