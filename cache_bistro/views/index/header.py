import reflex as rx
from cache_bistro.styles.styles import Size
from cache_bistro.styles.fonts import Font
from cache_bistro.styles.colors import Color, TextColor

def header_with_image_and_text():
    return rx.hstack(
        rx.box(
            rx.text(
                "Casual dinning and", 
                align="left", 
                size="9", 
                as_="div",
                font_family=Font.TITLE.value
            ),
            rx.text(
                "tasting room", 
                align="left", 
                size="9", 
                as_="div",
                font_family=Font.TITLE.value
            ),
            rx.link(
                rx.button(
                    rx.icon(tag="phone"),                    
                    "Hacenos tu reserva.",
                    color=Color.TERTIARY.value,
                    bg=Color.CUARTIARY.value,
                    size="3",
                    margin_top=Size.MEDIUM.value,
                    _hover={
                        "background": Color.TERTIARY.value,
                        "color": TextColor.CUARTIARY.value
                    }                  
                    ),
                    href="https://wa.me/+342613400065",
                    is_external=True,
            ),
                bg="center/cover url('/brindis.jpeg')",
                align_items="center",
                spacing="4",
                width="100%",
                height=["25em","37em"],
                padding_x="3em",
                padding_y=["5em","14em"],
                z_index="999",
                top="0"
                ),
    )


