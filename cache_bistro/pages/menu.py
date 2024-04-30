import reflex as rx
from cache_bistro.views.navbar import navbar
import cache_bistro.styles.styles as styles
from cache_bistro.views.menu.platos import tapas_desktop, tapas_mobile, parrilla_desktop, parrilla_mobile, principales_desktop, principales_mobile
from cache_bistro.views.menu.platos import ensaladas_desktop, ensaladas_mobile, postres_desktop, postres_mobile, menu_infantil_desktop, menu_infantil_mobile, bebidas_desktop, bebidas_mobile, vinos
from cache_bistro.styles.styles import Size
from cache_bistro.views.footer import  footer_desktop
from cache_bistro.components.black_line import black_line

@rx.page(
    route="/menu", 
    title="Menú | Caché Bistro",
    description="Página de \"Menú\" de Caché Bistro"
    )
def menu() -> rx.Component:
    return rx.vstack(
        rx.box(
            navbar(),
            width="100%",
        ),
            rx.vstack(
                rx.heading(
                    rx.hstack(
                        rx.text("MENÚ"),        
                        ),
                        align="left",
                        padding_top=Size.MEDIUM.value,
                        style=styles.title_style,
                    ),
                tapas_desktop(),
                tapas_mobile(),
                parrilla_desktop(),
                parrilla_mobile(),
                principales_desktop(),
                principales_mobile(),
                ensaladas_desktop(),
                ensaladas_mobile(),
                postres_desktop(),
                postres_mobile(),
                menu_infantil_desktop(),
                menu_infantil_mobile(),
                bebidas_desktop(),
                bebidas_mobile(),
                vinos(),
                black_line(),
        padding_left=Size.MEDIUM.value,
        ),
        rx.box(
            footer_desktop(),
            width="100%"
        ),
    )

    
