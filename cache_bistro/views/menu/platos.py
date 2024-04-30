import reflex as rx
from cache_bistro.components.title import subtitle, drinks_title
from cache_bistro.components.estructure import estructure
from cache_bistro.components.link_button import link_button
from cache_bistro.styles.styles import TextColor, Size, Color
from cache_bistro.components.info_menu import info_menu
from cache_bistro.views.constants import WINE_LIST_URL
    
def tapas_desktop() -> rx.Component:
    return rx.tablet_and_desktop(
        rx.vstack(
        subtitle("TAPAS"),
        rx.hstack(
            rx.vstack(
                info_menu(),
                estructure(
                    "● PROVOLETA A LA CHAPA \"LA LINQUEÑITA\" - $11.000",
                    "○ Provoleta na chapa",
                    "○ Grilled provoleta"
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value),
                estructure(
                    "● DEGUSTACIÓND DE QUESOS \"LA LINQUEÑITA\" - $14.000",
                    "○ Degustação de queijos",
                    "○ Cheese tasting"
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value),      
                estructure(
                    "● CEVICHE DE PESCADO - $12.000",
                    "○ Ceviche de peixe branco",
                    "○ Peruvian ceviche"
                ),
                rx.image(src="/gluten_free.png", width=["1em","1.5em"], height=["1em","1.5em"]),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value),
                estructure(
                    "● CAUSA LIMEÑA CON CALAMARES CROCANTES - $9.000",
                    "○ Causa de Lima com lulas crocantes",
                    "○ Causa whit crispy squid"
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value),      
                estructure(
                    "● FALAFEL DE GARBANZOS - $9.000",
                    "○ Falafel de grão de bico",
                    "○ Chickpea falafel"
                ),
                rx.hstack(                
                rx.image(src="/vegan.png", width=["1em","1.5em"], height=["1em","1.5em"]),
                rx.image(src="/veggie.png", width=["1em","1.5em"], height=["1em","1.5em"])
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value),      
                estructure(
                    "● GAZPACHO ANDALUZ - $7.000",
                    "○ Camaroes ao alho e limão",
                    "○ Shrimps whit garlic and lemon skin"
                ),
                rx.hstack(                
                rx.image(src="/vegan.png", width=["1em","1.5em"], height=["1em","1.5em"]),
                rx.image(src="/veggie.png", width=["1em","1.5em"], height=["1em","1.5em"]),
                rx.image(src="/gluten_free.png", width=["1em","1.5em"], height=["1em","1.5em"]),                
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value),
                estructure(
                    "● LANGOSTINOS AL AJILLO - $14.000",
                    "○ camarões ao alho",
                    "○ garlic shrimp"
                ),
                rx.image(src="/punto.png", width=["1em","1.5em"], height=["1em","1.5em"]),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value),      
                estructure(
                    "● ESCABECHE DE CONEJO CONFITADO - $9.500",
                    "○ Escbeche de coelho confitado",
                    "○ Rabbit escabeche"
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value),      
                estructure(
                    "● MIX VEGANO - $9.000",
                    "○ mix vegano",
                    "○ Vegan mix"
                ),
                rx.hstack(                
                rx.image(src="/vegan.png", width=["1em","1.5em"], height=["1em","1.5em"]),
                rx.image(src="/veggie.png", width=["1em","1.5em"], height=["1em","1.5em"])
                ),
            ),
            rx.vstack(
                rx.box(padding_bottom="1.9em"),
                estructure(
                    "● STRACIATELLA CON PESTO Y PAN CASERO - $13.000",
                    "○ Sttaciatella, pesto e páo da casa",
                    "○ Straciatella, pesto and homemade bread"
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value),                
                estructure(
                    "● BERENJENA A LA NAPOLITANA - $8.500",
                    "○ Berenjela à Napolitana",
                    "○ Napolitana eggplant"
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value),                
                estructure(
                    "● ANTICUCHO DE PICAÑA - $12.000",
                    "○ Anticucho de picanha",
                    "○ Peruvian anticucho"
                ),
                rx.image(src="/punto.png", width=["1em","1.5em"], height=["1em","1.5em"]),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value),               
                estructure(
                    "● CROQUETAS DE JAMON - $9.000",
                    "○ Croquettes de presunto tipo parma",
                    "○ Prosciutto croquettes"
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value),               
                estructure(
                    "● CROQUETAS DE ESPINACA Y ACELGA - $9.000",
                    "○ Croquettes de espinafre e acelga",
                    "○ Spinach and chard croquetts"
                ),
                rx.image(src="/punto.png", width=["1em","1.5em"], height=["1em","1.5em"]),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value),                  
                estructure(
                    "● PAPAS BRAVAS Y JAMON CRUDO - $8.500",
                    "○ Batatas bravas com presunto tipo parma",
                    "○ Spanish potatoes bravas"
                ),
                rx.image(src="/punto.png", width=["1em","1.5em"], height=["1em","1.5em"]),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value),                
                estructure(
                    "● CHIPIRONES Y CHIMICHURRI - $14.000",
                    "○ Lulas com chimichurri",
                    "○ Squid and chimichurri"
                ),
                rx.image(src="/gluten_free.png", width=["1em","1.5em"], height=["1em","1.5em"]),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value),                
                estructure(
                    "● MOLLEJAS CON PURE AHUMADO DE COLIFLOR - $14.000",
                    "○ Moelha e pure defumado de couveflor",
                    "○ Thymus whit smoked couliflorwer puree"
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value),                
                estructure(
                    "● DUO DE EMPANADAS (CARNE O VERDURAS) - $6.000",
                    "○ Dueto de empanadas (carne ou legumes)",
                    "○ Empanadas duo (beef or veggie)"
                ),               
                rx.image(src="/punto.png", width=["1em","1.5em"], height=["1em","1.5em"]), 
                #padding_top=[Size.ZERO.value, "2.35em"]            
        ), 
        )   
    )
    )
def tapas_mobile() -> rx.Component:
    return rx.mobile_only(
        rx.vstack(
        subtitle("TAPAS"),
            rx.vstack(
                info_menu(),
                estructure(
                    "● PROVOLETA A LA CHAPA \"LA LINQUEÑITA\" - $11.000",
                    "○ Provoleta na chapa",
                    "○ Grilled provoleta"
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),
                estructure(
                    "● DEGUSTACIÓND DE QUESOS \"LA LINQUEÑITA\" - $14.000",
                    "○ Degustação de queijos",
                    "○ Cheese tasting"
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),      
                estructure(
                    "● CEVICHE DE PESCADO - $12.000",
                    "○ Ceviche de peixe branco",
                    "○ Peruvian ceviche"
                ),
                rx.image(src="/gluten_free.png", width=["1em","1.5em"], height=["1em","1.5em"]),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),
                estructure(
                    "● CAUSA LIMEÑA CON CALAMARES CROCANTES - $9.000",
                    "○ Causa de Lima com lulas crocantes",
                    "○ Causa whit crispy squid"
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),      
                estructure(
                    "● FALAFEL DE GARBANZOS - $9.000",
                    "○ Falafel de grão de bico",
                    "○ Chickpea falafel"
                ),
                rx.hstack(                
                rx.image(src="/vegan.png", width=["1em","1.5em"], height=["1em","1.5em"]),
                rx.image(src="/veggie.png", width=["1em","1.5em"], height=["1em","1.5em"])
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),      
                estructure(
                    "● GAZPACHO ANDALUZ - $7.000",
                    "○ Camaroes ao alho e limão",
                    "○ Shrimps whit garlic and lemon skin"
                ),
                rx.hstack(                
                rx.image(src="/vegan.png", width=["1em","1.5em"], height=["1em","1.5em"]),
                rx.image(src="/veggie.png", width=["1em","1.5em"], height=["1em","1.5em"]),
                rx.image(src="/gluten_free.png", width=["1em","1.5em"], height=["1em","1.5em"]),                
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),
                estructure(
                    "● LANGOSTINOS AL AJILLO - $14.000",
                    "○ camarões ao alho",
                    "○ garlic shrimp"
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),      
                estructure(
                    "● ESCABECHE DE CONEJO CONFITADO - $9.500",
                    "○ Escbeche de coelho confitado",
                    "○ Rabbit escabeche"
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),      
                estructure(
                    "● MIX VEGANO - $9.000",
                    "○ mix vegano",
                    "○ Vegan mix"
                ),
                rx.hstack(                
                rx.image(src="/vegan.png", width=["1em","1.5em"], height=["1em","1.5em"]),
                rx.image(src="/veggie.png", width=["1em","1.5em"], height=["1em","1.5em"])
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),
                estructure(
                    "● STRACIATELLA CON PESTO Y PAN CASERO - $13.000",
                    "○ Sttaciatella, pesto e páo da casa",
                    "○ Straciatella, pesto and homemade bread"
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),                
                estructure(
                    "● BERENJENA A LA NAPOLITANA - $8.500",
                    "○ Berenjela à Napolitana",
                    "○ Napolitana eggplant"
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),                
                estructure(
                    "● ANTICUCHO DE PICAÑA - $12.000",
                    "○ Anticucho de picanha",
                    "○ Peruvian anticucho"
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),               
                estructure(
                    "● CROQUETAS DE JAMON - $9.000",
                    "○ Croquettes de presunto tipo parma",
                    "○ Prosciutto croquettes"
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),               
                estructure(
                    "● CROQUETAS DE ESPINACA Y ACELGA - $9.000",
                    "○ Croquettes de espinafre e acelga",
                    "○ Spinach and chard croquetts"
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),                  
                estructure(
                    "● PAPAS BRAVAS Y JAMON CRUDO - $8.500",
                    "○ Batatas bravas com presunto tipo parma",
                    "○ Spanish potatoes bravas"
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),                
                estructure(
                    "● CHIPIRONES Y CHIMICHURRI - $14.000",
                    "○ Lulas com chimichurri",
                    "○ Squid and chimichurri"
                ),
                rx.image(src="/gluten_free.png", width=["1em","1.5em"], height=["1em","1.5em"]),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),                
                estructure(
                    "● MOLLEJAS CON PURE AHUMADO DE COLIFLOR - $14.000",
                    "○ Moelha e pure defumado de couveflor",
                    "○ Thymus whit smoked couliflorwer puree"
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),                
                estructure(
                    "● DUO DE EMPANADAS (CARNE O VERDURAS) - $6.000",
                    "○ Dueto de empanadas (carne ou legumes)",
                    "○ Empanadas duo (beef or veggie)"
                ),               
        ), 
        )   
    )
        
    
    return rx.vstack(
        subtitle("TAPAS"),
        rx.hstack(
            rx.vstack(
                info_menu(),
                estructure(
                    "● PROVOLETA A LA CHAPA \"LA LINQUEÑITA\" - $11.000",
                    "○ Provoleta na chapa",
                    "○ Grilled provoleta"
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value),
                estructure(
                    "● DEGUSTACIÓND DE QUESOS \"LA LINQUEÑITA\" - $14.000",
                    "○ Degustação de queijos",
                    "○ Cheese tasting"
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value),      
                estructure(
                    "● CEVICHE DE PESCADO - $12.000",
                    "○ Ceviche de peixe branco",
                    "○ Peruvian ceviche"
                ),
                rx.image(src="gluten_free.png", width="1.5em", height="1.5em"),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value),
                estructure(
                    "● CAUSA LIMEÑA CON CALAMARES CROCANTES - $9.000",
                    "○ Causa de Lima com lulas crocantes",
                    "○ Causa whit crispy squid"
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value),      
                estructure(
                    "● FALAFEL DE GARBANZOS - $9.000",
                    "○ Falafel de grão de bico",
                    "○ Chickpea falafel"
                ),
                rx.hstack(                
                rx.image(src="vegan.png", width="1.5em", height="1.5em"),
                rx.image(src="veggie.png", width="1.5em", height="1.5em")
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value),      
                estructure(
                    "● GAZPACHO ANDALUZ - $7.000",
                    "○ Camaroes ao alho e limão",
                    "○ Shrimps whit garlic and lemon skin"
                ),
                rx.hstack(                
                rx.image(src="vegan.png", width="1.5em", height="1.5em"),
                rx.image(src="veggie.png", width="1.5em", height="1.5em"),
                rx.image(src="gluten_free.png", width="1.5em", height="1.5em"),                
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value),
                estructure(
                    "● LANGOSTINOS AL AJILLO - $14.000",
                    "○ camarões ao alho",
                    "○ garlic shrimp"
                ),
                rx.image(src="punto.png", width="1.5em", height="1.5em"),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value),      
                estructure(
                    "● ESCABECHE DE CONEJO CONFITADO - $9.500",
                    "○ Escbeche de coelho confitado",
                    "○ Rabbit escabeche"
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value),      
                estructure(
                    "● MIX VEGANO - $9.000",
                    "○ mix vegano",
                    "○ Vegan mix"
                ),
                rx.hstack(                
                rx.image(src="vegan.png", width="1.5em", height="1.5em"),
                rx.image(src="veggie.png", width="1.5em", height="1.5em")
                ),
            ),
            rx.vstack(
                estructure(
                    "● STRACIATELLA CON PESTO Y PAN CASERO - $13.000",
                    "○ Sttaciatella, pesto e páo da casa",
                    "○ Straciatella, pesto and homemade bread"
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value),                
                estructure(
                    "● BERENJENA A LA NAPOLITANA - $8.500",
                    "○ Berenjela à Napolitana",
                    "○ Napolitana eggplant"
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value),                
                estructure(
                    "● ANTICUCHO DE PICAÑA - $12.000",
                    "○ Anticucho de picanha",
                    "○ Peruvian anticucho"
                ),
                rx.image(src="punto.png", width="1.5em", height="1.5em"),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value),               
                estructure(
                    "● CROQUETAS DE JAMON - $9.000",
                    "○ Croquettes de presunto tipo parma",
                    "○ Prosciutto croquettes"
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value),               
                estructure(
                    "● CROQUETAS DE ESPINACA Y ACELGA - $9.000",
                    "○ Croquettes de espinafre e acelga",
                    "○ Spinach and chard croquetts"
                ),
                rx.image(src="punto.png", width="1.5em", height="1.5em"),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value),                  
                estructure(
                    "● PAPAS BRAVAS Y JAMON CRUDO - $8.500",
                    "○ Batatas bravas com presunto tipo parma",
                    "○ Spanish potatoes bravas"
                ),
                rx.image(src="punto.png", width="1.5em", height="1.5em"),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value),                
                estructure(
                    "● CHIPIRONES Y CHIMICHURRI - $14.000",
                    "○ Lulas com chimichurri",
                    "○ Squid and chimichurri"
                ),
                rx.image(src="gluten_free.png", width="1.5em", height="1.5em"),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value),                
                estructure(
                    "● MOLLEJAS CON PURE AHUMADO DE COLIFLOR - $14.000",
                    "○ Moelha e pure defumado de couveflor",
                    "○ Thymus whit smoked couliflorwer puree"
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value),                
                estructure(
                    "● DUO DE EMPANADAS (CARNE O VERDURAS) - $6.000",
                    "○ Dueto de empanadas (carne ou legumes)",
                    "○ Empanadas duo (beef or veggie)"
                ),               
                rx.image(src="punto.png", width="1.5em", height="1.5em"), 
                padding_top="2.35em"            
        ), 
        ) 
        
    )

def parrilla_desktop() -> rx.Component:
    return rx.tablet_and_desktop(
        rx.vstack(
        subtitle("PARRILLA"),
        rx.vstack(
        rx.text.strong(
            rx.text.em(
                "ACOMPAÑA PAPAS, ENSALADA, VEGETALES O PURÉ DE PAPA", 
                style={
                    'font_size':Size.MEDIUM.value, 
                    'color':TextColor.ACCENT.value
                }
            )
        ),
        bg=Color.PRIMARY.value,
        padding=Size.SMALL.value,
        margin_bottom=Size.MEDIUM.value
        ),        
        rx.hstack(
            rx.vstack(
                estructure(
                    "● COLITA DE CUADRIL (para compartir) - $37.000",
                    "○ Maminha",
                    "○ Tri-trip"
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value),
                estructure(
                    "● PICAÑA - $21.000",
                    "○ Picanha",
                    "○ Picanha"
                )
            ),
            rx.vstack(
                estructure(
                    "● OJO DE BIFE - $21.000",
                    "○ Contrafilé",
                    "○ Rib Eye"                    

                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value),                
                estructure(
                    "● ASADO DE TIRA - $21.000",
                    "○ Costela de ripa",
                    "○ Short ribs"
                ), 
                padding_left="4.5em"             
        ), 
        )    
    )
    )
def parrilla_mobile() -> rx.Component:
    return rx.mobile_only(
        rx.vstack(
        subtitle("PARRILLA"),
        rx.vstack(
        rx.text.strong(
            rx.text.em(
                "ACOMPAÑA PAPAS, ENSALADA, VEGETALES O PURÉ DE PAPA", 
                style={
                    'font_size':Size.MEDIUM.value, 
                    'color':TextColor.ACCENT.value
                }
            )
        ),
        bg=Color.PRIMARY.value,
        padding=Size.SMALL.value,
        width="95%",
        margin_bottom=Size.MEDIUM.value
        ),        
        rx.vstack(
                estructure(
                    "● COLITA DE CUADRIL (para compartir) - $37.000",
                    "○ Maminha",
                    "○ Tri-trip"
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),
                estructure(
                    "● PICAÑA - $21.000",
                    "○ Picanha",
                    "○ Picanha"
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),
                estructure(
                    "● OJO DE BIFE - $21.000",
                    "○ Contrafilé",
                    "○ Rib Eye"                    

                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),                
                estructure(
                    "● ASADO DE TIRA - $21.000",
                    "○ Costela de ripa",
                    "○ Short ribs"
                ), 
                padding_left=[Size.ZERO.value, "4.5em"]             
        ), 
        )    
    )
       

def principales_desktop() -> rx.Component:
    return rx.tablet_and_desktop(
        rx.vstack(
        subtitle("PRINCIPALES"),
        rx.hstack(
            rx.vstack(
                estructure(
                    "● ARROZ CON LANGOSTINOS AL LIMON - $14.500",
                    "○ Arroz com camaroes e limão",
                    "○ Rice with shrimp and lemon skin"
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value),
                estructure(
                    "● PASTA CON VEGETALES ASADOS - $13.500",
                    "○ Massa com legumes asadas",
                    "○ Pasta with sauted vegetables"
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value),
                estructure(
                    "● MILANESA DE OJO DE BIFE - $20.000",
                    "○ Milanesa de filé mignon",
                    "○ Rib eye milanese"
                ),
            ),
            rx.vstack(
                estructure(
                    "● PASTA ALLA AMATRICIANA - $14.500",
                    "○ Massa alla Amatriciana",
                    "○ Amatriciana Pasta"                    

                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value),                
                estructure(
                    "● BUCATINI CON MEJILLONES - $16.000",
                    "○ Bucatini com mexilhoes",
                    "○ Bucatini with mussels"
                ), 
                padding_left="3.8em"             
        ), 
        )    
    )
    )
def principales_mobile() -> rx.Component:
    return rx.mobile_only(
        rx.vstack(
        subtitle("PRINCIPALES"),
            rx.vstack(
                estructure(
                    "● ARROZ CON LANGOSTINOS AL LIMON - $14.500",
                    "○ Arroz com camaroes e limão",
                    "○ Rice with shrimp and lemon skin"
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),
                estructure(
                    "● PASTA CON VEGETALES ASADOS - $13.500",
                    "○ Massa com legumes asadas",
                    "○ Pasta with sauted vegetables"
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),
                estructure(
                    "● MILANESA DE OJO DE BIFE - $20.000",
                    "○ Milanesa de filé mignon",
                    "○ Rib eye milanese"
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),                
                estructure(
                    "● PASTA ALLA AMATRICIANA - $14.500",
                    "○ Massa alla Amatriciana",
                    "○ Amatriciana Pasta"                    

                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),                
                estructure(
                    "● BUCATINI CON MEJILLONES - $16.000",
                    "○ Bucatini com mexilhoes",
                    "○ Bucatini with mussels"
                ), 
        ), 
        )    
    )
    
def ensaladas_desktop() -> rx.Component:
    return rx.tablet_and_desktop(
        rx.vstack(
        subtitle("ENSALADAS"),
        rx.hstack(
            rx.vstack(
                estructure(
                    "● CAPRESSE A NUESTRO ESTILO - $9.500",
                    "○ Capresse ao nosso estilo",
                    "○ Our style capresse"
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),
                estructure(
                    "● BISTRO - $10.500",
                    "○ Folhas verdes, citricos, cuartirollo e tomates",
                    "○ Lettuce mix, citrics, cuartirollo cheese and tomatoes"
                ),
            ),
            rx.vstack(
                estructure(
                    "● GRIEGA - $8.900",
                    "○ Lentilha, legumes, rucula e azeite extra",
                    "○ Lentils, vegetables, and olive oil"                    

                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),
                estructure(
                    "● FRANCESA - $9.900",
                    "○ Peras caramelizadas, nozes e queijo azul",
                    "○ Caramelized pears, blue cheese and nuts"
                ), 
                padding_left="7em"             
        ), 
        )    
    )
    )
def ensaladas_mobile() -> rx.Component:
    return rx.mobile_only(
        rx.vstack(
        subtitle("ENSALADAS"),
            rx.vstack(
                estructure(
                    "● CAPRESSE A NUESTRO ESTILO - $9.500",
                    "○ Capresse ao nosso estilo",
                    "○ Our style capresse"
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),
                estructure(
                    "● BISTRO - $10.500",
                    "○ Folhas verdes, citricos, cuartirollo e tomates",
                    "○ Lettuce mix, citrics, cuartirollo cheese and tomatoes"
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),
                estructure(
                    "● GRIEGA - $8.900",
                    "○ Lentilha, legumes, rucula e azeite extra",
                    "○ Lentils, vegetables, and olive oil"                    

                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),
                estructure(
                    "● FRANCESA - $9.900",
                    "○ Peras caramelizadas, nozes e queijo azul",
                    "○ Caramelized pears, blue cheese and nuts"
                ), 
        ), 
        )    
    )
    
        
def postres_desktop() -> rx.Component:
    return rx.tablet_and_desktop(
        rx.vstack(
        subtitle("POSTRES"),
        rx.hstack(
            rx.vstack(
                estructure(
                    "● PROFITEROLES, HELADO Y DULCE DE LECHE - $7.500",
                    "○ Profiteroles, sorvete e doçe de leite",
                    "○ Profiteroles, ice cream and dulce de leche"
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value),
                estructure(
                    "● BRIGADEIRO AL PISCO APIMENTADO - $7.500",
                    "○ Brigadeiro com pisco apimentado",
                    "○ Brigadeiro with spicy pisco"
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),
                estructure(
                    "● PANNACOTTA (con romero y maracuyá) - $7.500",
                    "○ Pannacotta (com alecrim e maracujá)",
                    "○ Pannacotta (with rosemary and passion fruit)"
                )            ),
            rx.vstack(
                estructure(
                    "● BOMBITA DE CHOCOLATEA - $8.000",
                    "○ Brownie, sorvete e calda de chocolate",
                    "○ Brownie, chocolate ice cream and chocolate sauce"                    

                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value),                
                estructure(
                    "● DEGUSTACION DE QUESOS & DULCES - $11.000",
                    "○ Degustação de queijos e doçes",
                    "○ Cheese tasting and traditional sweets"
                ),                 
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),               
                estructure(
                    "● TIRAMISU - $7.500",
                    "○ Tiramisu",
                    "○ Tiramisu"
                ), 
                padding_left="1em"             
        ), 
        )    
    )
    )
def postres_mobile() -> rx.Component:
    return rx.mobile_only(
        rx.vstack(
        subtitle("POSTRES"),
            rx.vstack(
                estructure(
                    "● PROFITEROLES, HELADO Y DULCE DE LECHE - $7.500",
                    "○ Profiteroles, sorvete e doçe de leite",
                    "○ Profiteroles, ice cream and dulce de leche"
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),
                estructure(
                    "● BRIGADEIRO AL PISCO APIMENTADO - $7.500",
                    "○ Brigadeiro com pisco apimentado",
                    "○ Brigadeiro with spicy pisco"
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),
                estructure(
                    "● PANNACOTTA (con romero y maracuyá) - $7.500",
                    "○ Pannacotta (com alecrim e maracujá)",
                    "○ Pannacotta (with rosemary and passion fruit)"
                ),                 
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),           
                estructure(
                    "● BOMBITA DE CHOCOLATEA - $8.000",
                    "○ Brownie, sorvete e calda de chocolate",
                    "○ Brownie, chocolate ice cream and chocolate sauce"                    

                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),
                estructure(
                    "● DEGUSTACION DE QUESOS & DULCES - $11.000",
                    "○ Degustação de queijos e doçes",
                    "○ Cheese tasting and traditional sweets"
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),                
                estructure(
                    "● TIRAMISU - $7.500",
                    "○ Tiramisu",
                    "○ Tiramisu"
                ), 
        ), 
        )    
    )
        
def menu_infantil_desktop() -> rx.Component:
    return rx.tablet_and_desktop(
        rx.vstack(
        subtitle("MENÚ INFANTIL"),
        rx.vstack(
        rx.text.strong(rx.text.em("INCLUYE BEBIDA Y HELADO", style={'font_size':Size.MEDIUM.value, 'color':TextColor.ACCENT.value})),
        rx.text.strong(rx.text.em("INCLUI BEBIDA E SORVETE", style={'font_size':Size.MEDIUM.value, 'color':TextColor.ACCENT.value})),
        rx.text.strong(rx.text.em("BEVERAGE AND ICE CREAM INCLUDED", style={'font_size':Size.MEDIUM.value, 'color':TextColor.ACCENT.value})),
        bg=Color.PRIMARY.value,
        padding=Size.SMALL.value,
        margin_bottom=Size.MEDIUM.value
        ),
        rx.hstack(
            rx.vstack(
                estructure(
                    "● MILANESA O CHURRASQUITO - $10.000",
                    "○ Milanesa o churrasquinho",
                    "○ Breaded steak or grilled steak"
                ),
            ),
            rx.vstack(
                estructure(
                    "● PASTA A LA CREMA O POMODORO - $10.000",
                    "○ Macarrão com creme o molho de tomate",
                    "○ Pasta with cream or tomato sauce"                    

                ), 
                padding_left="1em"             
        ), 
        )    
    )
        )
def menu_infantil_mobile() -> rx.Component:
    return rx.mobile_only(
        rx.vstack(
        subtitle("MENÚ INFANTIL"),
        rx.vstack(
        rx.text.strong(rx.text.em("INCLUYE BEBIDA Y HELADO", style={'font_size':Size.MEDIUM.value, 'color':TextColor.ACCENT.value})),
        rx.text.strong(rx.text.em("INCLUI BEBIDA E SORVETE", style={'font_size':Size.MEDIUM.value, 'color':TextColor.ACCENT.value})),
        rx.text.strong(rx.text.em("BEVERAGE AND ICE CREAM INCLUDED", style={'font_size':Size.MEDIUM.value, 'color':TextColor.ACCENT.value})),
        bg=Color.PRIMARY.value,
        padding=Size.SMALL.value,
        margin_bottom=Size.MEDIUM.value
        ),
            rx.vstack(
                estructure(
                    "● MILANESA O CHURRASQUITO - $10.000",
                    "○ Milanesa o churrasquinho",
                    "○ Breaded steak or grilled steak"
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),                
                estructure(
                    "● PASTA A LA CREMA O POMODORO - $10.000",
                    "○ Macarrão com creme o molho de tomate",
                    "○ Pasta with cream or tomato sauce"                    

                ), 
        ), 
        )    
    )
        
    
def bebidas_desktop() -> rx.Component:
    return rx.tablet_and_desktop(
        rx.vstack(
        subtitle("BEBIDAS"),
        rx.hstack(
            rx.vstack(
                drinks_title("FRÍAS"),
                rx.text("● Agua con/sin gas - $2.000", style={'font_size':Size.LETTER.value, 'color':TextColor.PRIMARY.value}),
                rx.text("○ Agua de frutas y flores - $3.000", style={'font_size':Size.LETTER.value, 'color':TextColor.PRIMARY.value}),
                rx.text("● Gaseosa - $2.400", style={'font_size':Size.LETTER.value, 'color':TextColor.PRIMARY.value}),
                rx.text("○ Cerveza - $5.000", style={'font_size':Size.LETTER.value, 'color':TextColor.PRIMARY.value}),
                padding_right=Size.BIG.value,
            ),
            rx.vstack(
                drinks_title("CALIENTES"),
                rx.text("● Café - $3.000", style={'font_size':Size.LETTER.value, 'color':TextColor.PRIMARY.value}),
                rx.text("○ Infusiones - $3.500", style={'font_size':Size.LETTER.value, 'color':TextColor.PRIMARY.value}),
                padding_right=Size.BIG.value,
            ),             
            rx.vstack(
                drinks_title("Cócteles"),
                rx.text("● Aperol - $6.000", style={'font_size':Size.LETTER.value, 'color':TextColor.PRIMARY.value}),
                rx.text("○ Negroni - $6.500", style={'font_size':Size.LETTER.value, 'color':TextColor.PRIMARY.value}),
                rx.text("● Gin Tonic - $6.500", style={'font_size':Size.LETTER.value, 'color':TextColor.PRIMARY.value}),
                rx.text("○ Martini Dry - $6.000", style={'font_size':Size.LETTER.value, 'color':TextColor.PRIMARY.value}),
                rx.text("● Manhattan - $7.000", style={'font_size':Size.LETTER.value, 'color':TextColor.PRIMARY.value}),
            ),  
            )
    )
    )
def bebidas_mobile() -> rx.Component:
    return rx.mobile_only(
        rx.vstack(
        subtitle("BEBIDAS"),
            rx.vstack(
                drinks_title("FRÍAS"),
                rx.text("● Agua con/sin gas - $2.000", style={'font_size':Size.LETTER.value, 'color':TextColor.PRIMARY.value}),
                rx.text("○ Agua de frutas y flores - $3.000", style={'font_size':Size.LETTER.value, 'color':TextColor.PRIMARY.value}),
                rx.text("● Gaseosa - $2.400", style={'font_size':Size.LETTER.value, 'color':TextColor.PRIMARY.value}),
                rx.text("○ Cerveza - $5.000", style={'font_size':Size.LETTER.value, 'color':TextColor.PRIMARY.value}, padding_bottom=Size.SMALL.value),
                padding_right=Size.BIG.value,
            ),
            rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),
            rx.vstack(
                drinks_title("CALIENTES"),
                rx.text("● Café - $3.000", style={'font_size':Size.LETTER.value, 'color':TextColor.PRIMARY.value}),
                rx.text("○ Infusiones - $3.500", style={'font_size':Size.LETTER.value, 'color':TextColor.PRIMARY.value}, padding_bottom=Size.SMALL.value),
                padding_right=Size.BIG.value,
            ),             
            rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),
            rx.vstack(
                drinks_title("Cócteles"),
                rx.text("● Aperol - $6.000", style={'font_size':Size.LETTER.value, 'color':TextColor.PRIMARY.value}),
                rx.text("○ Negroni - $6.500", style={'font_size':Size.LETTER.value, 'color':TextColor.PRIMARY.value}),
                rx.text("● Gin Tonic - $6.500", style={'font_size':Size.LETTER.value, 'color':TextColor.PRIMARY.value}),
                rx.text("○ Martini Dry - $6.000", style={'font_size':Size.LETTER.value, 'color':TextColor.PRIMARY.value}),
                rx.text("● Manhattan - $7.000", style={'font_size':Size.LETTER.value, 'color':TextColor.PRIMARY.value}),
            ),
            )
    )
    
        
def vinos() -> rx.Component:
    return rx.vstack(
        subtitle("VINOS"),
        rx.image(src="/qr.png", width="15em", height="15em"),
        link_button(
            "Carta de Vinos",
            WINE_LIST_URL
            ),
        spacing="4"
    )