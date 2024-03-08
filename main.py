import flet as ft
from login_page import login



def main(page: ft.Page):
    page,
    page.window_max_width = 1440
    page.window_min_width = 1440
    page.window_max_height = 900
    page.window_min_height = 900
    page.window_maximizable = False
    page.window_width = 1440
    page.window_height = 900
    page.window_center()
    page.padding = 0
    page.margin = 0
    page.fonts={
        "Poppins_bold": "fonts/Poppins_bold.ttf",
        "Poppins_regular": "fonts/Poppins_regular.ttf"

    }
    page.update()
    page.add(login)



ft.app(target=main)