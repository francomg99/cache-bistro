import reflex as rx
from cache_bistro.styles.styles import Size, Color
from cache_bistro.components.link import link
from cache_bistro.components.menu import menu_item

def navbar() -> rx.Component:
    return rx.hstack(
        rx.hstack(
            rx.link(
            rx.image(
                src="/logo.png",
                alt="Logo de Cache Bistro - Fondo negro con letras doradas",
                width="8em",
                margin_left=["2em","10em"],
            ),
                href="/",
            ),
            rx.spacer(),
            rx.mobile_only(
                rx.menu.root(
                    rx.menu.trigger(
                        rx.button("☰", variant="ghost", size="4", color=Color.PRIMARY.value),
                    ),
                    rx.menu.content(
                        menu_item(
                            "INICIO",
                            "/"
                        ),                        
                        menu_item(
                            "NOSOTROS",
                            "/nosotros"
                        ),
                        menu_item(
                            "MENÚ",
                            "/menu"
                        ),                         
                        menu_item(
                            "RESERVAS",
                            "/reservas"
                        ),                       
                        style={
                            "background_color": Color.PRIMARY.value
                        },
                    ),
                    style={
                        "background_color": Color.PRIMARY.value, 
                        "color": Color.ACCENT.value
                    },
                ),
            ),
            rx.tablet_and_desktop(
                link(
                    "INICIO",
                    "/"
                ),
                link(
                    "NOSOTROS",
                    "/nosotros"               
                ),
                link(
                    "MENÚ",
                    "/menu"
                ),
                link(
                    "RESERVAS",
                    "/reservas"
                )
            ),            
            width="100%",
            align_items="center",
            spacing="4",
            margin_right=Size.BIG.value            
        ),
        position="sticky",
        bg=Color.ACCENT.value,
        z_index="9999",
        top="0",
        width="100%",
        align="center"
    )
    
                