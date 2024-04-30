import reflex as rx
from cache_bistro.styles.styles import Size, Color, TextColor

def link(name=str, url=str) -> rx.Component:
    return rx.link(
            name, 
            href=url,
            style={"font_size":Size.MEDIUM.value, "color":TextColor.SECONDARY.value},
            padding=Size.MEDIUM.value,
            _hover={
                "color": TextColor.PRIMARY.value
            }
            )
            