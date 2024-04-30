import reflex as rx
from cache_bistro.styles.styles import Color

def menu_item(text:str, url:str) -> rx.Component:
    return rx.menu.item(
                text, 
                on_click=rx.redirect(url),
                width="10em", 
                style={
                    "background_color": Color.PRIMARY.value, 
                    "color": Color.ACCENT.value
                }
            )