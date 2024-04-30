import reflex as rx
from cache_bistro.styles.styles import Size

def info_menu():
    return rx.box(
            rx.hstack(
                    rx.text(
                        "VEGAN",
                        style={'font_size':[Size.MEDIUM.value, Size.LETTER.value]}
                        ),
                    rx.image(src="/vegan.png", widht=["1em","1.5em"], height=["1em","1.5em"], padding_right="1em"),
                    rx.text(
                        "VEGGIE",
                        style={'font_size':[Size.MEDIUM.value, Size.LETTER.value]}
                        ),
                    rx.image(src="/veggie.png", widht=["1em","1.5em"], height=["1em","1.5em"], padding_right="1em"),
                    rx.text(
                        "GLUTEN FREE",
                        style={'font_size':[Size.MEDIUM.value, Size.LETTER.value]}
                        ),
                    rx.image(src="/gluten_free.png", widht=["1em","1.5em"], height=["1em","1.5em"])    
                    ),
            widht="100%"
            )
    