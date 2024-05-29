import reflex as rx
from cache_bistro.views.index.quienes_somos import quienes_somos
from cache_bistro.components.title import title
from cache_bistro.styles.styles import Size, Color, TextColor
from cache_bistro.views.constants import WHATSAPP_URL

def info() -> rx.Component:
    return rx.vstack(
            rx.box(
        quienes_somos(),
            rx.chakra.responsive_grid(
            rx.box(
                rx.image(
                    src="/dispenser.jpeg",
                    alt="dispenser de vino usandose",
                    widht="100%",
                    height=["auto","30em"],
                    padding_top=Size.BIG.value,
                    padding_left=[Size.SMALL.value, Size.BIG.value],
                    padding_right=[Size.SMALL.value, Size.BIG.value]
                )
            ),
            rx.box(
                rx.vstack(
                rx.box(
                rx.text(
                    """En""", rx.text.strong(rx.text.em(" Caché Bistro"), color=TextColor.SECONDARY.value), """, nos enorgullecemos de ofrecer una cuidadosa seleccion
                    de más de 700 etiquetas de vino distintas, desde pequeños prodcutores, hasta bodegas de renombre internacional.
                    Nuestro restaurante es un paraíso para los amantes del vino, donde puedes explorar una amplia 
                    variedad de sabores y aromas de todo Mendoza y Argentina.""",
                ),
                rx.text(
                    """Para aquellos aventurados que creen que con probar solo uno no es suficiente, 
                    ofrecemos la opción de probar varias copas con nuestros dispensers de vinos, el cual cuenta 
                    con 8 opciones distintas para degustar, garantizando frescura y calidad en cada copa.""",
                ),
                rx.text(
                    """Te invitamos a descubrir cada rincon que""",rx.text.strong(rx.text.em(" Caché "), color=TextColor.SECONDARY.value),"""tiene para ofrecerte, ya sea entre las paredes de nuestra 
                    salas repletas de vinos, disfrutando de la frescura de nuestro jardín. Únete a nosotros para una experiencia 
                    gastronómica única y memorable. ¡Te esperamos!"""),                
                padding_top="26px",
                padding_right=[Size.SMALL.value, Size.BIG.value],
                padding_left=[Size.SMALL.value, Size.ZERO.value],
                padding_bottom="0.2em",
                widht="100%",            
                style={
                    "text_indent": Size.DEFAULT.value,
                    "font_size": Size.LETTER.value,
                    'text_align': 'justify'
                }
                ),
                rx.chakra.link(
                    rx.chakra.button(
                    "Reservar",
                    size="lg",
                    margin_left= [Size.SMALL.value, Size.ZERO.value],
                    bg=Color.CUARTIARY.value,
                    color=Color.TERTIARY.value,
                    _hover={
                        "background": Color.TERTIARY.value,
                        "color": TextColor.CUARTIARY.value
                    },
                    ),
                    href=WHATSAPP_URL,
                    is_external=True
                )                        
                )
            ),
            columns=[1,2],
            widht="100%"
            ),
            title("ANDRES"),
            rx.chakra.responsive_grid(
            rx.box(
                rx.vstack(
                rx.box(
                rx.text(
                    """Detrás de la magia de""", rx.text.strong(rx.text.em(" Caché "), color=TextColor.SECONDARY.value), """se encuentra un verdadero apasionado y visionario culinario: 
                    Andrés Leyes. Como fundador y propietario del restaurante, Andrés ha dedicado su vida desde 2019 a llevar 
                    lo mejor de la gastronomía a la encantadora ciudad de Mendoza.""",
                ),
                rx.text(
                    """Con una visión clara y un deseo de compartir su amor por la comida y el vino, Andrés fundó""", 
                    rx.text.strong(rx.text.em(" Caché Bistro"), color=TextColor.SECONDARY.value), """. 
                    Inspirado por la rica tradición culinaria de Mendoza y su aprecio por la industria 
                    local de renombre mundial, Andrés creó un destino gastronómico que captura la esencia misma de la 
                    región.""",
                ),
                rx.text(
                    """Entre todas sus pasiones culinarias, hay una que brilla con especial intensidad en el corazón de 
                    Andrés: su amor por el vino. Desde las delicadas notas de un Malbec hasta la frescura de un Torrontés, 
                    aprecia la diversidad y la complejidad de los vinos argentinos. Su conocimiento experto y su 
                    paladar refinado lo convierten en un verdadero conocedor del vino, y es esta pasión la que impulsa 
                    la excepcional selección de más de 700 etiquetas de vino en""", 
                    rx.text.strong(rx.text.em(" Caché"), color=TextColor.SECONDARY.value), """. Y aún creciendo."""
                ),                
                padding_top="26px",
                padding_left=[Size.SMALL.value, Size.BIG.value],
                padding_right=[Size.SMALL.value, Size.ZERO.value],
                padding_bottom="0.2em",
                widht="100%",            
                style={
                    "text_indent": Size.DEFAULT.value,
                    "font_size": Size.LETTER.value,
                    'text_align': 'justify'
                }
                )
        )
            ),
                rx.box(
                rx.image(
                    src="/andres.jpg",
                    alt="Andres, dueño de Caché Bistro",
                    widht="100%",
                    height=["auto","30em"],
                    align="right",
                    padding_top=Size.BIG.value,
                    padding_left=[Size.SMALL.value, Size.BIG.value],
                    padding_right=[Size.SMALL.value, Size.VERY_BIG.value]
                )
            ),
            columns=[1,2],
            widht="100%"
            )
            )
    )
    