import reflex as rx
from cache_bistro.styles.styles import Size

def foto_info(src= str, alt=str, text=str) -> rx.Component:
    return rx.box(
            rx.image(src=src, alt=alt, width="400px", height="400px"),
            rx.text(text, 
            width=["99%","400px"],
            margin_top=Size.MEDIUM.value
            ),
            direction="column",
            align="center",
            padding=[Size.SMALL.value, Size.MEDIUM.value],
            style={
            "font_size": Size.LETTER.value,
            'text_align': 'justify'
            }                        
        )