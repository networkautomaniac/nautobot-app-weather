from nautobot.apps.ui import NavMenuGroup, NavMenuItem, NavMenuTab

menu_items = (
    NavMenuTab(
        name="Plugins",
        groups=(
            NavMenuGroup(
                name="Weather",
                items=(
                    NavMenuItem(
                        link="dcim:location_list",
                        name="Weather",
                        permissions=["dcim.view_location"],
                    ),
                ),
            ),
        ),
    ),
)
