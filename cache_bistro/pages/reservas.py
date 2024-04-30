import reflex as rx
from cache_bistro.views.navbar import navbar
from cache_bistro.views.index.contact import contact
from cache_bistro.views.reservas.reservas import info_wpp, info_ig, info_correo, info_trip
from cache_bistro.views.footer import footer_desktop
from cache_bistro.components.black_line import black_line

@rx.page(
    route="/reservas", 
    title="Reservas | Caché Bistro",
    description="Página de \"Reservas\" de Caché Bistro"
    )
def reservas() -> rx.Component:
    return rx.box(
        navbar(),
        contact(),
        info_wpp(),
        info_ig(),
        info_correo(),
        info_trip(),
        black_line(),
        footer_desktop(),
    )
    
