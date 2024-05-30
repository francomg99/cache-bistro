import reflex as rx
from cache_bistro.components.title import title
from cache_bistro.components.foto_info import foto_info
from cache_bistro.styles.styles import Size

def nuestros_rincones() -> rx.Component:
    return rx.vstack(
        title("NUESTROS RINCONES"),
            rx.chakra.responsive_grid(
                    rx.chakra.box(
                        foto_info(
                            "/entrada.jpg",
                            "Entrada al restaurante, con mesas y plantas a su alrededor",
                            """La entrada a un restaurante es mucho más que simplemente una puerta que permite a los clientes 
                            entrar y salir. Es el umbral entre el mundo exterior y una experiencia culinaria única. 
                            Es el primer contacto que los comensales tienen con el ambiente, la atmósfera y la hospitalidad 
                            que el restaurante tiene para ofrecer."""                            
                        )                      
                    ),
                    rx.chakra.box(
                        foto_info(
                            "/jardin.jpg",
                            "Barrica de vino junto a un horno de barro",
                            """Tener un jardín en un restaurante es como añadir un toque de magia natural al ambiente 
                            gastronómico. No se trata solamente de un área al aire libre; es un oasis de tranquilidad y belleza 
                            que complementa la experiencia culinaria de los comensales de una manera única."""                            
                        )                                                
                    ),
                    rx.chakra.box(
                        foto_info(
                            "/cava.jpg",
                            "Vinos en la pared, parte de una cava",
                            """La cava de vinos es el corazón latente de un restaurante, la morada completa donde se albergan 
                            no solo botellas de vino, sino también historias, tradiciones y pasiones enológicas. 
                            Va más alla de un espacio de almacenamiento; es un santuario dedicado al noble arte de la 
                            vinificación y al placer de disfrutar de una buena copa."""                            
                        )                                                
                    ),
                    columns=[1, 3],      
                    width="100%"
                )
        )
