import reflex as rx
from cache_bistro.components.title import title
from cache_bistro.styles.styles import Size, TextColor
from cache_bistro.components.link_button import link_button

def quienes_somos() -> rx.Component:
    return rx.vstack(
        title("¿QUIÉNES SOMOS?"),
            rx.box(
                rx.text(               
                    """Somos un restaurante ubicado en el corazón de la Capital Internacional del Vino, Mendoza.
                    Un lugar formado por nuestra gran pasión hacía el vino y la gastronomía. En el 2019, cuando
                    comenzo""", rx.text.strong(rx.text.em(" Caché Bistro "), color=TextColor.SECONDARY.value), """no creíamos alcanzar en tan poco tiempo estar posicionados en el top 3
                    de restaurantes de la provincia, consiguiendo por dos años consecutivos el premio \"Traveller\'s Choice\"
                    de Tripadvisor, del cual nos sentimos muy orgullosos."""),
                rx.tablet_and_desktop(
                rx.text(
                    """Contamos con una cava con más de 700 etiquetas de las mejores bodegas de la región,
                    en donde encontraras todos los sabores, texturas variedades, para que encuentres la que más 
                    te guste. Creemos que cada botella cuenta una historia, y nos esforzamos por ofrecer una variedad que
                    satisfaga cada paladar."""
                ),
                rx.text(
                    """En""",rx.text.strong(rx.text.em(" Caché "), color=TextColor.SECONDARY.value),"""creemos en la calidad, la autenticidad y el buen servicio. Nuestro equipo está dedicado a 
                    proporcionar una experiencia gastronómica memorable en un ambiente acogedor y elegante. Desde la tranquilidad de
                    nuestros jardines, hasta los lugares mas reconditos en nuestras cavas. La frescura de nuestros ingredientes hasta
                    la creatividad en nuestros platos, cada detalle está cuidadosamente considerado para brindarle una experiencia
                    gastronómica excepcional."""
                )
                ),
                rx.mobile_only(
                    link_button(
                        "Saber más",
                        "/nosotros"
                    ),
                    padding_top=Size.SMALL.value,
                    style={
                    "text_indent": Size.ZERO.value,
                    "font_size": Size.LETTER.value
                }
                ),
                padding_top=[Size.ZERO.value, Size.SMALL.value],
                padding_left=[Size.SMALL.value, Size.BIG.value],
                padding_right=[Size.SMALL.value, Size.BIG.value],
                style={
                    "text_indent": Size.DEFAULT.value,
                    "font_size": Size.LETTER.value,
                    'text_align': 'justify'
                }
            )
        )    
    