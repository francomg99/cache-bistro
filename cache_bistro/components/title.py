import reflex as rx
import cache_bistro.styles.styles as styles
from cache_bistro.styles.styles import Size

def title(text: str) -> rx.Component:
    return rx.heading(
                rx.hstack(
                    rx.text(text),        
                    ),
                    align="left",
                    padding=["0.3em",Size.SMALL.value],
                    margin_top=Size.MEDIUM.value,
                    style=styles.title_style,
                )
    
def subtitle(text: str) -> rx.Component:
    return rx.heading(
                rx.hstack(
                    rx.text(
                        text,
                        line_height=["1", "0"],    
                    )     
                    ),
                    align="left",
                    padding_top=Size.MEDIUM.value,
                    padding_bottom="0.3em",
                    style=styles.subtitle_style
                )

def drinks_title(text) -> rx.Component:
    return rx.heading(
                rx.hstack(
                    rx.text(text),        
                    ),
                    align="left",
                    padding_top=Size.SMALL.value,
                    style=styles.drinktitle_style
                )
    