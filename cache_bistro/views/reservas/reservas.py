import reflex as rx
from cache_bistro.components.title import title
from cache_bistro.components.link_button import link_button
from cache_bistro.styles.styles import Size
from cache_bistro.views.constants import INSTAGRAM_URL, WHATSAPP_URL, TRIPADVISOR_URL, MAIL_URL

def info_wpp() -> rx.Component:
    return rx.vstack(
        title("WHAT'S APP"),
        rx.box(
            rx.text(rx.text.strong("¿Quieres hacer una reserva de forma rápida y sencilla? "),
                    """¡Hazlo directamente desde tu teléfono! 
                    Solo tienes que enviarnos un mensaje o llamarnos a nuestro número de""", rx.text.em(" What's App "),
                    """y nuestro equipo estará encantado de ayudarte a asegurar tu reserva"""),
            rx.text(
                """Ya sea para una cena romántica, una reunión de negocios o una celebración especial, 
                    estamos aquí para hacer que tu experiencia sea inolvidable. ¡Esperamos tu mensaje!""",
                padding_bottom=Size.DEFAULT.value),  
            link_button(
                "What's App",
                WHATSAPP_URL
            ),            
            padding_left=[Size.SMALL.value, Size.BIG.value],
            padding_right=[Size.SMALL.value, Size.BIG.value],
            style={
                'font_size': Size.LETTER.value
            }   
        ),

    )
    
def info_ig() -> rx.Component:
    return rx.vstack(
        title("INSTAGRAM"),
        rx.box(
            rx.text("""Después de disfrutar de nuestro perfil lleno de platos irresistibles y momentos encantadores, 
                    ¿qué te parece llevar tu experiencia al siguiente nivel reservando una mesa con nosotros? 
                    ¡Es tan fácil como enviar un mensaje directo!"""),  
            rx.text(
                """Envianos un mensaje y déjanos saber la fecha, hora y número de personas para tu reserva. 
                    Nuestro equipo estará encantado de asegurarse de que tu visita sea perfecta en cada detalle.""",
                padding_bottom=Size.DEFAULT.value
            ),                
            link_button(
                "Instagram",
                INSTAGRAM_URL
            ),            
            padding_left=[Size.SMALL.value, Size.BIG.value],
            padding_right=[Size.SMALL.value, Size.BIG.value],
            style={
                'font_size': Size.LETTER.value
            }   
        ),
    )
    
def info_correo() -> rx.Component:
    return rx.vstack(
        title("CORREO"),
        rx.box(

            rx.text("""Si te gusta la idea de organizar tu próxima cena o evento a través del correo electrónico, 
                    solo necesitas enviar tus detalles de reserva. Incluye la fecha, hora y el número de personas, 
                    ¡y nosotros nos encargaremos del resto!"""),  
            rx.text(
                """Nuestro equipo estará atento a tu solicitud y te confirmará la reserva lo antes posible. 
                    ¿Tienes alguna preferencia especial o necesitas ajustes? No dudes en hacérnoslo saber en tu 
                    correo electrónico.""",
                    padding_bottom=Size.DEFAULT.value
            ),
            link_button(
                "Correo",
                MAIL_URL
                ),            
            padding_left=[Size.SMALL.value, Size.BIG.value],
            padding_right=[Size.SMALL.value, Size.BIG.value],
            style={
                'font_size': Size.LETTER.value
            }   
        ),

    )    

def info_trip() -> rx.Component:
    return rx.vstack(
        title("TRIPADVISOR"),
        rx.box(
            rx.text("""Y a los que ya que han reservado y disfrutado de una deliciosa experiencia 
                    culinaria con nosotros. Ahora, nos encantaría escuchar sus opiniones y comentarios en TripAdvisor."""),  
            rx.text(
                """Si te cautivaron nuestros platos exquisitos, el ambiente acogedor y el servicio excepcional, 
                ¿por qué no compartir tu experiencia con otros viajeros y amantes de la buena comida?""",
                padding_bottom=Size.DEFAULT.value
            ),                    
            link_button(
                "Tripadvisor",
                TRIPADVISOR_URL
            ),                     
            padding_left=[Size.SMALL.value, Size.BIG.value],
            padding_right=[Size.SMALL.value, Size.BIG.value],
            style={
                'font_size': Size.LETTER.value
            }   
        ),

    )