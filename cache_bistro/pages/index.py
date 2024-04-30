import reflex as rx
from cache_bistro.views.navbar import navbar
from cache_bistro.views.index.header import header_with_image_and_text
from cache_bistro.views.index.nuestros_rincones import nuestros_rincones
from cache_bistro.views.index.quienes_somos import quienes_somos
from cache_bistro.views.index.ubicacion import ubicacion
from cache_bistro.views.index.contact import contact
from cache_bistro.views.footer import footer_desktop
from cache_bistro.components.black_line import black_line

@rx.page(
    route="/", 
    title="Caché Bistro | Casual dinning and tasting room",
    description="Página de \"Inicio\" de Caché Bistro"
    )
def index() -> rx.Component:
    return rx.box(
        navbar(),
        header_with_image_and_text(),
        quienes_somos(),
        nuestros_rincones(),
        ubicacion(),
        contact(),
        black_line(),
        footer_desktop(),
    )
    