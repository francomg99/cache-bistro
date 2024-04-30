import reflex as rx
from rxconfig import config
from cache_bistro.pages.index import index
from cache_bistro.pages.menu import menu
from cache_bistro.pages.reservas import reservas
from cache_bistro.pages.nosotros import nosotros
import cache_bistro.styles.styles as styles

docs_url = "https://reflex.dev/docs/getting-started/introduction/"
filename = f"{config.app_name}/{config.app_name}.py"


class State(rx.State):
    """The app state."""


app = rx.App(
    stylesheets=styles.STYLESHEETS,
    style=styles.BASE_STYLE
)

