from flet import *

## Colors
COLOR_PRIMARY = "#0575E6"
BLUE_WHITE = "#0575E6"
BLACK = "#333333"
WHITE = "#FFFFFF"

#Titulos
def h1(text:str, color:str):
   return Container(
        content=Row(
            [
                Text(
                    value=text,
                    font_family="Poppins_bold",
                    size=40,
                    color=color
                )
            ]
        )
    )

def h2(text:str):
    return Container(
        content=Row(
            [
                Text(
                    value=text,
                    font_family="Poppins_bold",
                    size=26,
                )
            ]
        )
    )

def h3(text:str, color:str):
      return  Container(
            content=Row(
                [
                    Text(
                        value=text,
                        font_family="Poppins_regular",
                        color=color,
                        size=18,
                    )
                ]
            )
        )

def text_pattern(text:str):
    return Container(
            content=Row(
                [
                    Text(
                        value=text,
                        font_family="Poppins_regular",
                        size=14,
                    )
                ]
            )
        )

## Botão primário
def on_hover_btn(e):
    if e.control.bgcolor == COLOR_PRIMARY :
        e.control.bgcolor = WHITE
        e.control.content.controls[0].color = COLOR_PRIMARY 
    else:
        e.control.bgcolor = COLOR_PRIMARY 
        e.control.content.controls[0].color = WHITE
    e.control.update()

def btn_primary(texto:str,largura:int):
    return Container(
        width=largura,
        padding=18,
        border_radius=30,
        bgcolor=COLOR_PRIMARY,
        border=border.all(2,COLOR_PRIMARY),
        shadow=BoxShadow(
            color="#D6D6D6",
            spread_radius=1,
            blur_radius=5,
            offset=Offset(0,2),
            blur_style=ShadowBlurStyle.NORMAL,
        ),
        animate=animation.Animation(duration=200,curve='EASE_IN'),
        on_hover=lambda e:on_hover_btn(e),
        content=Row(
                controls=[
                    Text(
                        value=texto,
                        color=WHITE,
                        font_family='Poppins_bold',
                        size=14
                    ),
                ],
                alignment='center')
    )


def input_pattern(icon:str, texto:str, largura:int, senha:bool):
    """Atribua o texto que irá ficar de placeholder, ou seja. sumirá a partir do momento que irá digitar"""
    return Container(
        width=largura,
        height=70,
        border=border.all(width=1,color=colors.GREY_100),
        border_radius=50,
        padding=padding.Padding(26,15,15,15),
        content=Row(
            controls=[
                Image(
                    src=icon,
                    width=24,
                    height=24,
                ),
                TextField(
                    width=int(largura - 60),
                    max_lines=1,
                    content_padding=padding.Padding(0,15,15,15),
                    border="NONE",
                    hint_text=texto,
                    text_style=TextStyle(
                        size=14,
                        font_family='Poppins_regular'
                    ),
                    password=senha,

                )
            ]
        )
    )


