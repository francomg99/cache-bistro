import reflex as rx
from cache_bistro.components.title import title
from cache_bistro.components.link_button import link_button
from cache_bistro.styles.styles import Size, Color
from cache_bistro.views.constants import UBICACION_URL

def ubicacion() -> rx.Component:
    return rx.vstack(
        title("UBICACIÓN"),
            rx.html(
                '''
                <iframe
                src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3350.3845205136126!2d-68.84846112446886!3d-32.88800037361743!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x967e09fbd8383861%3A0xd4948ae0794e0736!2sCach%C3%A8%20Bistro!5e0!3m2!1ses!2ses!4v1712849500042!5m2!1ses!2ses"
                width="100%"
                height="100%"
                style="border:0;"
                allowfullscreen=""
                loading="lazy"
                referrerpolicy="no-referrer-when-downgrade">
                </iframe>
                ''',
                style={"width": "100%", "height":"30em"},
                padding_left=[Size.SMALL.value, Size.BIG.value],
                padding_right=[Size.SMALL.value, Size.BIG.value],
            ),
            rx.flex(
                rx.vstack(
                    rx.hstack(
                        rx.icon("map_pin", color=Color.PRIMARY.value, size=40),
                        rx.text("Espejo 529, Mendoza, Argentina.", style={"font_size":Size.LETTER.value}, padding_bottom="1em")
                    ),
                    link_button(
                        "¿Cómo llegar?",
                        UBICACION_URL
                    )
                ),
                    gap="2",
                    padding_left=[Size.SMALL.value, Size.BIG.value],
                    padding_top=Size.BIG.value,
                    padding_bottom=Size.BIG.value,
                    align_items="center",
                )
    )