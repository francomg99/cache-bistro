import reflex as rx
from cache_bistro.components.title import title

def contact():
    return rx.vstack(
        title("RESERVANOS"),
        rx.html(
            """<iframe id="" allowtransparency="true" allowfullscreen="true" allow="geolocation; microphone; camera" src="https://my.forms.app/form/662a6e0006d2c67545697738" frameborder="0" style="width: 99vw; min-width:100%; height:600px; border:none;"></iframe>"""
            )
    )

    
