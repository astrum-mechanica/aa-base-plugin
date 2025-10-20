"""Hook into Alliance Auth"""

# Alliance Auth
from allianceauth import hooks
from allianceauth.services.hooks import MenuItemHook, UrlHook

# Fleet Dash
# AA Base Plugin
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
        """Render the menu item"""
        if request.user.has_perm("aa_base_plugin.basic_access"):
            return MenuItemHook.render(self, request)
        return ""


@hooks.register("menu_item_hook")
def register_menu():
    """Register the menu item"""
    return ExampleMenuItem()


@hooks.register("url_hook")
def register_urls():
    """Register app urls"""
    return UrlHook(urls, namespace="aa_base_plugin", base_url=r"^aa_base_plugin/")
