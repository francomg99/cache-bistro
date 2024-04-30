import reflex as rx
import cache_bistro.styles.styles as styles

def estructure(spanish=str, portugues=str, english=str)->rx.Component:
    return rx.box(
                rx.text(
                    spanish,
                    style=styles.plates_style,
                ),
                rx.text(
                    portugues,
                    style=styles.plates_other_style,
                ),
                rx.text(
                    english,
                    style=styles.plates_other_style,
                ),
        )