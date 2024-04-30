import reflex as rx
from cache_bistro.styles.styles import Size

def icon(icon: str, text: str, text_2: str):
    return rx.flex(
        rx.icon(icon, size=80),
        rx.text(text, align="center",font_size=Size.MEDIUM.value),
        rx.text(text_2, align="center",font_size=Size.MEDIUM.value),
        direction="column",
        align_items="center",
        gap="1",
        padding=Size.MEDIUM.value
    )

def link_icon_footer(image: str, alt:str, url: str) -> rx.Component:
    return rx.link(
                rx.image(
                    src=image,
                    alt=alt,
                    width="2em",
                    height="2em",
                    padding="0.05em"               
                ),
            href=url,
            is_external=True,
            color="#828282",  
            align="center",
            )
