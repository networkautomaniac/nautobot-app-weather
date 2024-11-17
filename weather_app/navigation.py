"""Menu items."""

from nautobot.apps.ui import NavMenuAddButton, NavMenuGroup, NavMenuItem, NavMenuTab

items = (
    NavMenuItem(
        link="plugins:weather_app:weather_list",
        name="Weather",
        permissions=["weather_app.view_weather"],
        # buttons=(
        #     NavMenuAddButton(
        #         link="plugins:weather_app:weather_add",
        #         permissions=["weather_app.add_weather"],
        #     ),
        # ),
    ),
)

menu_items = (
    NavMenuTab(
        name="Apps",
        groups=(NavMenuGroup(name="Weather App", items=tuple(items)),),
    ),
)
