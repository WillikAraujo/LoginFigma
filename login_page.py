from flet import *
from style import *


login = Container(
    content=Row(
        [
            Container(
                width=860,
                height=900,
                image_src="assets/imgs/Bg.png",
                image_fit="fill",
                content=Container(
                    margin=margin.only(157,371,293,382),
                    content=
                    Column(
                        controls=[
                            h1(text='GoFinance',color='#FFFFFF'),
                            h3(text='The most popular peer to peer lending at SEA',color='#FFFFFF'),
                            Divider(height=10, color='transparent'),
                            ElevatedButton(text='Read More')
                        ],
                    )
                )
            ),
            Container(
                height=356,
                width=307,
                margin=margin.only(left=113),
                content=Column(
                    [
                        Column(
                            [
                                h2(text="Hello Again!"),
                                h3(text="Welcome Back", color=BLACK),
                                Divider(height=30, color='transparent')

                            ],
                            spacing=0
                        ),
                        Column(
                            spacing=8,
                            controls=
                            [
                                input_pattern('assets/imgs/icon_mail.png','Email Address',307,False),
                                input_pattern('assets/imgs/icon_pass.png', 'Password', 307, True),
                                btn_primary("Login",307),
                                Divider(height=15,color="transparent"),
                            ]
                        ),
                        Row([text_pattern('Forgot Password')],alignment='center')
                    ],
                spacing=8,
                )
            )
        ]
    )
)
