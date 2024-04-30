import reflex as rx
from cache_bistro.styles.styles import Size, Color, TextColor

def link_button(text:str, url:str) -> rx.Component:
    return rx.chakra.link(
            rx.chakra.button(
                text,
                bg=Color.PRIMARY.value,
                color=TextColor.ACCENT.value,
                size="lg",
                _hover={
                    "background": Color.SECONDARY.value,
                    "color": TextColor.PRIMARY.value
                },
            ),
                href=url,
                is_external=True                  
        )