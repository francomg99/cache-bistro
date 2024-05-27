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
        subtitle("TAPEO"),
        rx.hstack(
            rx.vstack(
                info_menu(),
                estructure(
                    "● PROVOLETA A LA CHAPA \"LA LINQUEÑITA\" - $12.000",
                    "○ Provoleta na chapa",
                    "○ Grilled provoleta"
                ),
                rx.image(src="/punto.png", width=["1em","1.5em"], height=["1em","1.5em"]),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),
                estructure(
                    "● DEGUSTACIÓN DE QUESOS \"LA LINQUEÑITA\" - $18.000",
                    "○ Degustação de queijos",
                    "○ Cheese tasting"
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),      
                estructure(
                    "● CEVICHE DE PESCADO - $13.000",
                    "○ Ceviche de peixe branco",
                    "○ Peruvian ceviche"
                ),
                rx.image(src="/gluten_free.png", width=["1em","1.5em"], height=["1em","1.5em"]),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),
                estructure(
                    "● CAUSA PERUANA, TATAKI DE BIFE Y CHIMI - $12.000",
                    "○ Causa peruana, tataki e chimichurri",
                    "○ Peruvian causa, beef tataki and chimichurri"
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),      
                estructure(
                    "● LANGOSTINOS AL AJILLO Y PIEL DE LIMÓN - $14.000",
                    "○ Camarões ao Alho e Raspas de Limão",
                    "○ Garlic Shrimp with Lemon Zest"
                ),
                rx.hstack(                
                rx.image(src="/gluten_free.png", width=["1em","1.5em"], height=["1em","1.5em"]),
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),      
                estructure(
                    "● MIX VEGANO (HUMMUS, PEPPERONATA, ENCURTIDOS) - $9.500",
                    "○ Mix vegano",
                    "○ Vegan mix"
                ),
                rx.hstack(                
                rx.image(src="/vegan.png", width=["1em","1.5em"], height=["1em","1.5em"]),
                rx.image(src="/veggie.png", width=["1em","1.5em"], height=["1em","1.5em"]),
                rx.image(src="/gluten_free.png", width=["1em","1.5em"], height=["1em","1.5em"]),
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),
                estructure(
                    "● MONGOLIAN BEEF Y PIMIENTOS ASADOS - $13.500",
                    "○ Carne Mongol e pimentões assados",
                    "○ Mongolian beef with grilled peppers"
                ),
                rx.image(src="/punto.png", width=["1em","1.5em"], height=["1em","1.5em"]),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),      
                estructure(
                    "● GIRGOLAS (HONGOS AL AGLI OLIO) - $11.500",
                    "○ Gírgolas (Cogumelos ao Aglio e Olio)",
                    "○ Oyster Mushrooms (Aglio e Olio)"
                ),
                rx.hstack(                
                rx.image(src="/vegan.png", width=["1em","1.5em"], height=["1em","1.5em"]),
                rx.image(src="/veggie.png", width=["1em","1.5em"], height=["1em","1.5em"]),
                rx.image(src="/gluten_free.png", width=["1em","1.5em"], height=["1em","1.5em"]),
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),
                estructure(
                    "● STRACIATELLA CON PESTO Y PAN CASERO - $13.000",
                    "○ Sttaciatella, pesto e páo da casa",
                    "○ Straciatella, pesto and homemade bread"
                ),
            ),
            rx.vstack(
                rx.box(padding_bottom="1.9em"),              
                estructure(
                    "● BERENJENA A LA NAPOLITANA - $8.500",
                    "○ Berenjela à Napolitana",
                    "○ Napolitana eggplant"
                ),
                rx.hstack(                
                rx.image(src="/veggie.png", width=["1em","1.5em"], height=["1em","1.5em"]),
                rx.image(src="/gluten_free.png", width=["1em","1.5em"], height=["1em","1.5em"]),
                ),                
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),                
                estructure(
                    "● ANTICUCHO DE PICAÑA A LA PERUANA - $13.000",
                    "○ Anticucho de picanha",
                    "○ Peruvian anticucho"
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),               
                estructure(
                    "● CROQUETAS DE JAMON SERRANO - $10.000",
                    "○ Croquettes de presunto tipo parma",
                    "○ Prosciutto croquettes"
                ),
                rx.image(src="/punto.png", width=["1em","1.5em"], height=["1em","1.5em"]),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),               
                estructure(
                    "● CHIPIRONES CON CHIMICHURRI - $14.000",
                    "○ Lulas com chimichurri",
                    "○ Squid and chimichurri"
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),                  
                estructure(
                    "● MOLLEJAS CON PURÉ AHUMADO DE COLIFLOR - $14.000",
                    "○ Moelha e pure defumado de couveflor",
                    "○ Thymus whit smoked couliflorwer puree"
                ),
                rx.image(src="/punto.png", width=["1em","1.5em"], height=["1em","1.5em"]),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),                                               
                estructure(
                    "● DUO DE EMPANADAS (CARNE O VERDURAS) - $7.000",
                    "○ Dueto de empanadas (carne ou legumes)",
                    "○ Empanadas duo (beef or veggie)"
                ),               
                rx.image(src="/punto.png", width=["1em","1.5em"], height=["1em","1.5em"]),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),                                               
                estructure(
                    "● LINGOTE DE PAPA CROCANTE Y ROMESCO - $10.500",
                    "○ Lingote de Batata Crocante e Romesco",
                    "○ Crispy Potato Block with Romesco"
                ),               
                rx.hstack(                
                rx.image(src="/veggie.png", width=["1em","1.5em"], height=["1em","1.5em"]),
                rx.image(src="/gluten_free.png", width=["1em","1.5em"], height=["1em","1.5em"]),
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),                                               
                estructure(
                    "● SOPA DEL DÍA - $10.500",
                    "○ Sopa do Dia",
                    "○ Soup of the Day"
                ),               
                rx.hstack(                
                rx.image(src="/vegan.png", width=["1em","1.5em"], height=["1em","1.5em"]),
                rx.image(src="/veggie.png", width=["1em","1.5em"], height=["1em","1.5em"]),
                rx.image(src="/gluten_free.png", width=["1em","1.5em"], height=["1em","1.5em"]),
                ),                ), 
        )   
    )
    )
def tapas_mobile() -> rx.Component:
    return rx.mobile_only(
        rx.vstack(
        subtitle("TAPEO"),
            rx.vstack(
                info_menu(),
                estructure(
                    "● PROVOLETA A LA CHAPA \"LA LINQUEÑITA\" - $12.000",
                    "○ Provoleta na chapa",
                    "○ Grilled provoleta"
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),
                estructure(
                    "● DEGUSTACIÓND DE QUESOS \"LA LINQUEÑITA\" - $18.000",
                    "○ Degustação de queijos",
                    "○ Cheese tasting"
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),      
                estructure(
                    "● CEVICHE DE PESCADO - $13.000",
                    "○ Ceviche de peixe branco",
                    "○ Peruvian ceviche"
                ),
                rx.image(src="/gluten_free.png", width=["1em","1.5em"], height=["1em","1.5em"]),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),
                estructure(
                    "● CAUSA PERUANA, TATAKI DE BIFE Y CHIMI - $12.000",
                    "○ Causa peruana, tataki e chimichurri",
                    "○ Peruvian causa, beef tataki and chimichurri"
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),      
                estructure(
                    "● LANGOSTINOS AL AJILLO Y PIEL DE LIMÓN - $14.000",
                    "○ Camarões ao Alho e Raspas de Limão",
                    "○ Garlic Shrimp with Lemon Zest"
                ),
                rx.hstack(                
                rx.image(src="/gluten_free.png", width=["1em","1.5em"], height=["1em","1.5em"]),
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),      
                estructure(
                    "● MIX VEGANO (HUMMUS, PEPPERONATA, ENCURTIDOS) - $9.500",
                    "○ Mix vegano",
                    "○ Vegan mix"
                ),
                rx.hstack(                
                rx.image(src="/vegan.png", width=["1em","1.5em"], height=["1em","1.5em"]),
                rx.image(src="/veggie.png", width=["1em","1.5em"], height=["1em","1.5em"]),
                rx.image(src="/gluten_free.png", width=["1em","1.5em"], height=["1em","1.5em"]),
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),
                estructure(
                    "● MONGOLIAN BEEF Y PIMIENTOS ASADOS - $13.500",
                    "○ Carne Mongol e pimentões assados",
                    "○ Mongolian beef with grilled peppers"
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),      
                estructure(
                    "● GIRGOLAS (HONGOS AL AGLI OLIO) - $11.500",
                    "○ Gírgolas (Cogumelos ao Aglio e Olio)",
                    "○ Oyster Mushrooms (Aglio e Olio)"
                ),
                rx.hstack(                
                rx.image(src="/vegan.png", width=["1em","1.5em"], height=["1em","1.5em"]),
                rx.image(src="/veggie.png", width=["1em","1.5em"], height=["1em","1.5em"]),
                rx.image(src="/gluten_free.png", width=["1em","1.5em"], height=["1em","1.5em"]),
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
                rx.hstack(                
                rx.image(src="/veggie.png", width=["1em","1.5em"], height=["1em","1.5em"]),
                rx.image(src="/gluten_free.png", width=["1em","1.5em"], height=["1em","1.5em"]),
                ),                
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),                
                estructure(
                    "● ANTICUCHO DE PICAÑA A LA PERUANA - $13.000",
                    "○ Anticucho de picanha",
                    "○ Peruvian anticucho"
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),               
                estructure(
                    "● CROQUETAS DE JAMON SERRANO - $10.000",
                    "○ Croquettes de presunto tipo parma",
                    "○ Prosciutto croquettes"
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),               
                estructure(
                    "● CHIPIRONES CON CHIMICHURRI - $14.000",
                    "○ Lulas com chimichurri",
                    "○ Squid and chimichurri"
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),                  
                estructure(
                    "● MOLLEJAS CON PURÉ AHUMADO DE COLIFLOR - $14.000",
                    "○ Moelha e pure defumado de couveflor",
                    "○ Thymus whit smoked couliflorwer puree"
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),                                               
                estructure(
                    "● DUO DE EMPANADAS (CARNE O VERDURAS) - $7.000",
                    "○ Dueto de empanadas (carne ou legumes)",
                    "○ Empanadas duo (beef or veggie)"
                ),               
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),                                               
                estructure(
                    "● LINGOTE DE PAPA CROCANTE Y ROMESCO - $10.500",
                    "○ Lingote de Batata Crocante e Romesco",
                    "○ Crispy Potato Block with Romesco"
                ),               
                rx.hstack(                
                rx.image(src="/veggie.png", width=["1em","1.5em"], height=["1em","1.5em"]),
                rx.image(src="/gluten_free.png", width=["1em","1.5em"], height=["1em","1.5em"]),
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),                                               
                estructure(
                    "● SOPA DEL DÍA - $10.500",
                    "○ Sopa do Dia",
                    "○ Soup of the Day"
                ),               
                rx.hstack(                
                rx.image(src="/vegan.png", width=["1em","1.5em"], height=["1em","1.5em"]),
                rx.image(src="/veggie.png", width=["1em","1.5em"], height=["1em","1.5em"]),
                rx.image(src="/gluten_free.png", width=["1em","1.5em"], height=["1em","1.5em"]),
                ),             
        ), 
        )   
    )
        

def parrilla_desktop() -> rx.Component:
    return rx.tablet_and_desktop(
        rx.vstack(
        subtitle("LAS BRASAS / GRELHADOS / GRILL"),
        rx.vstack(
        rx.text.strong(rx.text.em("ACOMPAÑA PAPAS, ENSALADA, VEGETALES O PURÉ DE PAPA", style={'font_size':Size.MEDIUM.value, 'color':TextColor.ACCENT.value})),
        rx.text.strong(rx.text.em("SERVED WITH POTATOES, SALAD, VEGETABLES OR SMASH POTATOES", style={'font_size':Size.MEDIUM.value, 'color':TextColor.ACCENT.value})),
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
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),
                estructure(
                    "● PICAÑA - $22.000",
                    "○ Picanha",
                    "○ Picanha"
                )
            ),
            rx.vstack(
                estructure(
                    "● OJO DE BIFE - $22.000",
                    "○ Contrafilé",
                    "○ Rib Eye"                    

                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),                
                estructure(
                    "● MATAMBRE DE CERDO - $20.000",
                    "○ Matambre de Porco",
                    "○ Pork Matambre"
                ), 
                padding_left="4.5em"             
        ), 
        )    
    )
    )
    
def parrilla_mobile() -> rx.Component:
    return rx.mobile_only(
        rx.vstack(
        subtitle("lAS BRASAS / GRELHADOS / GRILL"),
        rx.vstack(
        rx.text.strong(rx.text.em("ACOMPAÑA PAPAS, ENSALADA, VEGETALES O PURÉ DE PAPA", style={'font_size':Size.MEDIUM.value, 'color':TextColor.ACCENT.value})),
        rx.text.strong(rx.text.em("SERVED WITH POTATOES, SALAD, VEGETABLES OR SMASH POTATOES", style={'font_size':Size.MEDIUM.value, 'color':TextColor.ACCENT.value})),
        bg=Color.PRIMARY.value,
        padding=Size.SMALL.value,
        margin_bottom=Size.MEDIUM.value,
        width="95%"
        ),      
        rx.vstack(
                estructure(
                    "● COLITA DE CUADRIL (para compartir) (700grs) - $37.000",
                    "○ Maminha",
                    "○ Tri-trip"
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),
                estructure(
                    "● PICAÑA (350grs) - $22.000",
                    "○ Picanha",
                    "○ Picanha"
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),
                estructure(
                    "● OJO DE BIFE (350grs) - $22.000",
                    "○ Contrafilé",
                    "○ Rib Eye"                    

                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),                
                estructure(
                    "● MATAMBRE DE CERDO (350grs) - $20.000",
                    "○ Matambre de Porco",
                    "○ Pork Matambre"
                ),  
                padding_left=[Size.ZERO.value, "4.5em"]             
        ), 
        )    
    )
       

def principales_desktop() -> rx.Component:
    return rx.tablet_and_desktop(
        rx.vstack(
        subtitle("ENTRE OLLAS / PANELAS / COOKING POTS"),
        rx.hstack(
            rx.vstack(
                estructure(
                    "● ARROZ CON LANGOTINOS Y COCO THAI - $16.000",
                    "○ Arroz com camaroes e coco Thai",
                    "○ Rice with shrimps and coconut thai"
                ),
                rx.image(src="/gluten_free.png", width=["1em","1.5em"], height=["1em","1.5em"]),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),
                estructure(
                    "● FALSO ARROZ DE COLIFLOR CHINESSE - $14.000",
                    "○ Falso arroz de couve-flor chinese",
                    "○ Fake rice couliflower chinese style"
                ),
                rx.hstack(                
                rx.image(src="/vegan.png", width=["1em","1.5em"], height=["1em","1.5em"]),
                rx.image(src="/veggie.png", width=["1em","1.5em"], height=["1em","1.5em"]),
                rx.image(src="/gluten_free.png", width=["1em","1.5em"], height=["1em","1.5em"]),
                ),                   
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),
                estructure(
                    "● OSSOBUCO EN SU JUGO DE 4 HORAS - $17.000",
                    "○ Ossobuco ao molho de 4 horas",
                    "○ Slow cook Ossobuco"
                ),
            ),
            rx.vstack(
                estructure(
                    "● PASTA ALLA AMATRICIANA - $16.000",
                    "○ Massa alla Amatriciana",
                    "○ Amatriciana Pasta"                    
                ),
                rx.image(src="/punto.png", width=["1em","1.5em"], height=["1em","1.5em"]),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),                
                estructure(
                    "● BUCATINI CON MEJILLONES - $16.000",
                    "○ Bucatini com mexilhoes",
                    "○ Bucatini with mussels"
                ),
                rx.image(src="/punto.png", width=["1em","1.5em"], height=["1em","1.5em"]),                
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),                
                estructure(
                    "● GOULASH DE CORDERO AL HORNO DE BARRO - $18.000",
                    "○ Goulash de cordeiro ao forno de barro",
                    "○ Lamb goulash"
                ), 
                padding_left="3.8em"             
        ), 
        )    
    )
    )
def principales_mobile() -> rx.Component:
    return rx.mobile_only(
        rx.vstack(
        subtitle("ENTRE OLLAS / PANELAS / COOKING POTS"),
            rx.vstack(
                estructure(
                    "● ARROZ CON LANGOTINOS Y COCO THAI - $16.000",
                    "○ Arroz com camaroes e coco Thai",
                    "○ Rice with shrimps and coconut thai"
                ),
                rx.image(src="/gluten_free.png", width=["1em","1.5em"], height=["1em","1.5em"]),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),
                estructure(
                    "● FALSO ARROZ DE COLIFLOR CHINESSE - $14.000",
                    "○ Falso arroz de couve-flor chinese",
                    "○ Fake rice couliflower chinese style"
                ),
                rx.hstack(                
                rx.image(src="/vegan.png", width=["1em","1.5em"], height=["1em","1.5em"]),
                rx.image(src="/veggie.png", width=["1em","1.5em"], height=["1em","1.5em"]),
                rx.image(src="/gluten_free.png", width=["1em","1.5em"], height=["1em","1.5em"]),
                ),                   
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),
                estructure(
                    "● OSSOBUCO EN SU JUGO DE 4 HORAS - $17.000",
                    "○ Ossobuco ao molho de 4 horas",
                    "○ Slow cook Ossobuco"
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
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),                
                estructure(
                    "● GOULASH DE CORDERO AL HORNO DE BARRO - $18.000",
                    "○ Goulash de cordeiro ao forno de barro",
                    "○ Lamb goulash"
                ),        ), 
        )    
    )
    
def ensaladas_desktop() -> rx.Component:
    return rx.tablet_and_desktop(
        rx.vstack(
        subtitle("ENSALADAS"),
        rx.hstack(
            rx.vstack(
                estructure(
                    "● BISTRO - $10.500",
                    "○ Folhas verdes, citricos, cuartirollo e tomates",
                    "○ Lettuce mix, citrics, cuartirollo cheese and tomatoes"
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),
                estructure(
                    "● GRIEGA - $8.500",
                    "○ Lentilha, legumes, rucula e azeite extra",
                    "○ Lentils, vegetables, and olive oil"                    
                ),            
                ),
            rx.vstack(
                estructure(
                    "● FRANCESA - $9.000",
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
                    "● BISTRO - $10.500",
                    "○ Folhas verdes, citricos, cuartirollo e tomates",
                    "○ Lettuce mix, citrics, cuartirollo cheese and tomatoes"
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),
                estructure(
                    "● GRIEGA - $8.500",
                    "○ Lentilha, legumes, rucula e azeite extra",
                    "○ Lentils, vegetables, and olive oil"                    

                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),
                estructure(
                    "● FRANCESA - $9.000",
                    "○ Peras caramelizadas, nozes e queijo azul",
                    "○ Caramelized pears, blue cheese and nuts"
                ), 
        ), 
        )    
    )
    
        
def postres_desktop() -> rx.Component:
    return rx.tablet_and_desktop(
        rx.vstack(
        subtitle("POSTRES / SOBREMESAS / DESSERTS"),
        rx.hstack(
            rx.vstack(
                estructure(
                    "● DEGUSTACION DE QUESOS & DULCES - $11.000",
                    "○ Degustação de queijos e doçes",
                    "○ Cheese tasting and traditional sweets"

                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),
                estructure(
                    "● TIRAMISU A NUESTRO ESTILO- $9.000",
                    "○ Tiramisu ao nosso estilo",
                    "○ Our style tiramisu"
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),
                estructure(
                    "● PANNACOTTA (con romero y maracuyá) - $8.000",
                    "○ Pannacotta (com alecrim e maracujá)",
                    "○ Pannacotta (with rosemary and passion fruit)"
                )            
                ),
            rx.vstack(
                estructure(
                    "● CHEESECAKE DE QUESO DE CABRA Y MEMBRILLO - $9.000",
                    "○ Cheesecake de queijo de cabra e marmelo",
                    "○ Goat cheese cheeesecake and quince jelly"                    
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),                
                estructure(
                    "● PROFITEROLES, HELADO Y DULCE DE LECHE - $9.500",
                    "○ Profiteroles, sorvete e doçe de leite",
                    "○ Profiteroles, ice cream and dulce de leche"
                ),                 
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),               
                estructure(
                    "● TRIO DE CHOCOLATES (Brownie, helado y salsa) - $9.000",
                    "○ Trio de chocolate (Brownie, sorvete e molho)",
                    "○ Three chocolates (Brownie, ice cream and sauce)"
                ), 
                padding_left="2em",
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
                    "● PROFITEROLES, HELADO Y DULCE DE LECHE - $9.500",
                    "○ Profiteroles, sorvete e doçe de leite",
                    "○ Profiteroles, ice cream and dulce de leche"
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),
                estructure(
                    "● TRIO DE CHOCOLATES (Brownie, helado y salsa) - $9.000",
                    "○ Trio de chocolate (Brownie, sorvete e molho)",
                    "○ Three chocolates (Brownie, ice cream and sauce)"
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),
                estructure(
                    "● PANNACOTTA (con romero y maracuyá) - $8.000",
                    "○ Pannacotta (com alecrim e maracujá)",
                    "○ Pannacotta (with rosemary and passion fruit)"
                ),                 
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),           
                estructure(
                    "● CHEESECAKE DE QUESO DE CABRA Y MEMBRILLO - $9.000",
                    "○ Cheesecake de queijo de cabra e marmelo",
                    "○ Goat cheese cheeesecake and quince jelly"                    
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),                
                estructure(
                    "● DEGUSTACION DE QUESOS & DULCES - $11.000",
                    "○ Degustação de queijos e doçes",
                    "○ Cheese tasting and traditional sweets"
                ),                 
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),               
                estructure(
                    "● TIRAMISU A NUESTRO ESTILO- $9.000",
                    "○ Tiramisu ao nosso estilo",
                    "○ Our style tiramisu"
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
                    "● MILANESA O CHURRASQUITO DE RES - $10.000",
                    "○ Bife a Milanesa ou bife na grelha",
                    "○ Beef milanesa or grilled beef"
                ),
            ),
            rx.vstack(
                estructure(
                    "● PASTA A LA CREMA O POMODORO - $10.000",
                    "○ Masa ao creme ou pomodoro",
                    "○ Pasta with crea mor pomodoro"                    

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
                    "● MILANESA O CHURRASQUITO DE RES - $10.000",
                    "○ Bife a Milanesa ou bife na grelha",
                    "○ Beef milanesa or grilled beef"
                ),
                rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),                
                estructure(
                    "● PASTA A LA CREMA O POMODORO - $10.000",
                    "○ Masa ao creme ou pomodoro",
                    "○ Pasta with crea mor pomodoro"                   

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
                drinks_title("FRÍAS / COLD"),
                rx.text("● Agua con/sin gas - $2.000", style={'font_size':Size.LETTER.value, 'color':TextColor.PRIMARY.value}),
                rx.text("○ Agua de frutas y flores - $3.000", style={'font_size':Size.LETTER.value, 'color':TextColor.PRIMARY.value}),
                rx.text("● Gaseosa - $2.500", style={'font_size':Size.LETTER.value, 'color':TextColor.PRIMARY.value}),
                rx.text("○ Cerveza - $5.000", style={'font_size':Size.LETTER.value, 'color':TextColor.PRIMARY.value}),
                padding_right=Size.BIG.value,
            ),
            rx.vstack(
                drinks_title("CALIENTES"),
                rx.text("● Café - $3.000", style={'font_size':Size.LETTER.value, 'color':TextColor.PRIMARY.value}),
                rx.text("○ Infusiones - $3.500", style={'font_size':Size.LETTER.value, 'color':TextColor.PRIMARY.value}),
                rx.text("○ Carajillo (Expresso – Whiskey) - $5.500", style={'font_size':Size.LETTER.value, 'color':TextColor.PRIMARY.value}),                
                padding_right=Size.BIG.value,
            ), 
        ),            
            rx.vstack(
                drinks_title("CÓCTELES / DRINKS / COCKTAILS"),
                rx.text("● Expresso Martini (Vodka - Licor de café - Café shot) - $7.000", style={'font_size':Size.LETTER.value, 'color':TextColor.PRIMARY.value}),
                rx.text("○ Negroni (Gin - Campari - Vermut Rosso) - $6.500", style={'font_size':Size.LETTER.value, 'color':TextColor.PRIMARY.value}),
                rx.text("● Martini Dry (Gin - Vermut - Aceituna) - $6.000", style={'font_size':Size.LETTER.value, 'color':TextColor.PRIMARY.value}),
                rx.text("○ Manhattan (Whiskey - Vermut - rosso) - $6.000", style={'font_size':Size.LETTER.value, 'color':TextColor.PRIMARY.value}),
                rx.text("● Ramazotti (Licor de hibiscos – Espumante - naranja) - $6.000", style={'font_size':Size.LETTER.value, 'color':TextColor.PRIMARY.value}),
                rx.text("○ Boulevardier (Whiskey – Vermut - Campari) - $6.500", style={'font_size':Size.LETTER.value, 'color':TextColor.PRIMARY.value}),
                rx.text("● Pisco Sour (Pisco – Limon – clara de huevo) - $6.000", style={'font_size':Size.LETTER.value, 'color':TextColor.PRIMARY.value}),
                rx.text("○ Limoncello (Gin infusionado 21 dias) - $5.500", style={'font_size':Size.LETTER.value, 'color':TextColor.PRIMARY.value}),
                rx.text("● Vermut con Soda (vermute rosso – Soda – Naranja) - $6.000", style={'font_size':Size.LETTER.value, 'color':TextColor.PRIMARY.value}),
),  
            
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
                rx.text("● Gaseosa - $2.500", style={'font_size':Size.LETTER.value, 'color':TextColor.PRIMARY.value}),
                rx.text("○ Cerveza - $5.000", style={'font_size':Size.LETTER.value, 'color':TextColor.PRIMARY.value}),
                padding_right=Size.BIG.value,
            ),
            rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),
            rx.vstack(
                drinks_title("CALIENTES"),
                rx.text("● Café - $3.000", style={'font_size':Size.LETTER.value, 'color':TextColor.PRIMARY.value}),
                rx.text("○ Infusiones - $3.500", style={'font_size':Size.LETTER.value, 'color':TextColor.PRIMARY.value}),
                rx.text("○ Carajillo (Expresso – Whiskey) - $5.500", style={'font_size':Size.LETTER.value, 'color':TextColor.PRIMARY.value}),
                padding_right=Size.BIG.value,
            ),             
            rx.chakra.divider(border_color=TextColor.SECONDARY.value, width="95%"),
            rx.vstack(
                drinks_title("CÓCTELES / DRINKS / COCKTAILS"),
                rx.text("● Expresso Martini (Vodka - Licor de café - Café shot) - $7.000", style={'font_size':Size.LETTER.value, 'color':TextColor.PRIMARY.value}),
                rx.text("○ Negroni (Gin - Campari - Vermut Rosso) - $6.500", style={'font_size':Size.LETTER.value, 'color':TextColor.PRIMARY.value}),
                rx.text("● Martini Dry (Gin - Vermut - Aceituna) - $6.000", style={'font_size':Size.LETTER.value, 'color':TextColor.PRIMARY.value}),
                rx.text("○ Manhattan (Whiskey - Vermut - rosso) - $6.000", style={'font_size':Size.LETTER.value, 'color':TextColor.PRIMARY.value}),
                rx.text("● Ramazotti (Licor de hibiscos – Espumante - naranja) - $6.000", style={'font_size':Size.LETTER.value, 'color':TextColor.PRIMARY.value}),
                rx.text("○ Boulevardier (Whiskey – Vermut - Campari) - $6.500", style={'font_size':Size.LETTER.value, 'color':TextColor.PRIMARY.value}),
                rx.text("● Pisco Sour (Pisco – Limon – clara de huevo) - $6.000", style={'font_size':Size.LETTER.value, 'color':TextColor.PRIMARY.value}),
                rx.text("○ Limoncello (Gin infusionado 21 dias) - $5.500", style={'font_size':Size.LETTER.value, 'color':TextColor.PRIMARY.value}),
                rx.text("● Vermut con Soda (vermute rosso – Soda – Naranja) - $6.000", style={'font_size':Size.LETTER.value, 'color':TextColor.PRIMARY.value}),
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