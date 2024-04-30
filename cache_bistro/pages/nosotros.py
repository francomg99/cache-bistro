import reflex as rx
from cache_bistro.views.navbar import navbar
from cache_bistro.views.nosotros.nosotros import info
from cache_bistro.views.footer import footer_desktop
from cache_bistro.components.black_line import black_line

@rx.page(
    route="/nosotros", 
    title="Nosotros | Caché Bistro",
    description="Página de \"Nosotros\" de Caché Bistro"
    )
def nosotros() -> rx.Component:
    return rx.box(
        navbar(),
        info(),
        black_line(),
        footer_desktop(),
    )
    
