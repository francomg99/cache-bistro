import reflex as rx
from cache_bistro.components.icon import link_icon_footer
from cache_bistro.views.constants import INSTAGRAM_URL, WHATSAPP_URL, TRIPADVISOR_URL

def footer_desktop():
    return rx.flex(
                rx.image(
                    src="/logo_fondo_gris.png",
                    alt="Logo del restaurante Cache Bistro",
                    width="9em",
                    padding="1em",
                    align_items="center"
                ),
                rx.spacer(),
                rx.spacer(),
                rx.tablet_and_desktop(
                rx.flex(
                    link_icon_footer(
                    "/ig.png",
                    "Icono con el logo de Instagram",
                    INSTAGRAM_URL                 
                    ),
                    link_icon_footer(
                    "/wpp.png",
                    "Icono con el logo de What's App",
                    WHATSAPP_URL
                    ),
                    link_icon_footer(
                    "/trip.png",
                    "Icono con el logo de Tripadvisor",
                    TRIPADVISOR_URL                    
                    ),
                direction="row", # Alineación horizontal por defecto
                justify="center",
                spacing="4",
                class_name="footer-icons",
                ),
                ),                
                rx.spacer(),
                rx.link(
                    "©Pagina creada por Franco Martínez - Reflex | Python",
                    href="https://hermesdev.es",
                    is_external=True,
                    margin="1em",
                    color="#828282"
                        ),
                columns=[1,3],
                bg="#393a3d",
                direction="row", # Alineación horizontal por defecto
                justify="between",
                align="center",
                class_name="footer-container",
                width="100%",
            )
    
