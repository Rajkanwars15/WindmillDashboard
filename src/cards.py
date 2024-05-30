from h2o_wave import Q, ui

# Link to repo. Report bugs/features here :)
repo_url = 'https://github.com/rajkanwars15/neuralix-ai-hackathon-task1'
issue_url = f'{repo_url}/issues/new?assignees=rajkanwars15&labels=bug&template=error-report.md&title=%5BERROR%5D'

# app layout
async def app_layout(q: Q):
    q.page["meta"] = ui.meta_card(
        box="",
        themes=[
            ui.theme(
                name='neuralix-dark',
                primary='#5ab5ad',
                text='#ffffff',
                card='#181A1B',
                page='#2d2f30',
            ),
            ui.theme(
                name='neuralix-light',
                primary='#5ab5ad',
                text='#181A1B',
                card='#ffffff',
                page='#DCE3E3',
            )
        ],
        box='',
        title='Neuralix Wind Farm Dashboard',
        icon='https://i.imgur.com/s9w0xce.png',
        theme='neuralix-light',
        layouts=[
            ui.layout(
                breakpoint="xs",
                zones=[
                    ui.zone("header", align="start", justify="around"),
                    ui.zone(
                        name="zone1", direction=ui.ZoneDirection.COLUMN, size="100%", align="center", justify="center"
                    ),
                    ui.zone(
                        name="zone2", direction=ui.ZoneDirection.COLUMN, size="100%", align="center", justify="center"
                    ),
                    ui.zone("footer"),
                ],
            ),
            ui.layout(
                breakpoint="m",
                zones=[
                    ui.zone("header"),
                    ui.zone(
                        "body",
                        direction=ui.ZoneDirection.COLUMN,
                        align="stretch",
                        justify="between",
                        size="60rem",
                        zones=[
                            ui.zone(
                                "zone1", direction=ui.ZoneDirection.ROW, align="center", justify="around", size="50%"
                            ),
                            ui.zone("separate", direction="column", size="10px"),
                            ui.zone(
                                "zone2", direction=ui.ZoneDirection.ROW, align="center", justify="around", size="50%"
                            ),
                        ],
                    ),
                    ui.zone("depression"),
                    ui.zone("footer"),
                ],
            ),
        ],
    )


async def home(q: Q):
    q.page["header"] = ui.header_card(
        box=ui.box("header", width="100%", height="80px"),
        title='neuralix.ai',
        subtitle='',
        image='https://i.imgur.com/yThsZ40.png',
        nav=[
            ui.nav_group('Menu', items=[
                ui.nav_item(name='#menu/monthly_data', label='Monthly Data'),
                ui.nav_item(name='#menu/year_comparison', label='Year Comparison'),
                ui.nav_item(name='#menu/summary_statistics', label='Summary Statistics'),
            ]),
        ],
        items=[
            # dark mode toggle switch
            ui.toggle(name='toggle_theme', label='', value=False, trigger=True),
            # profile in header
            ui.menu(image='default', items=[
                ui.command(name='profile', label='Profile', icon='Contact'),
                ui.command(name='preferences', label='Preferences', icon='Settings'),
                ui.command(name='logout', label='Logout', icon='SignOut'),
            ])
        ]
    )

    q.page["footer"] = ui.footer_card(
        box="footer",
        caption=f'Learn more about <a href="{repo_url}" target="_blank"> this dashboard</a>'
    )
