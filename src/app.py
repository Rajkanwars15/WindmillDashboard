from h2o_wave import Q, ui, main, app, on
import pandas as pd

with open('../JupyterOutputs/monthly_sum_of_lv_activepower.html', 'r') as file:
    html_content = file.read()

@on('toggle_theme')
async def toggle_theme(q: Q):
    """
    Toggle between light and dark themes.
    """
    if q.args.toggle_theme:
        q.client.theme_dark = True
        q.page['meta'].theme = 'neuralix-dark'
        q.page['header'].image = 'https://i.imgur.com/ZS6G3f4.png'
        logging.info('Updating theme to dark mode')
    else:
        q.client.theme_dark = False
        q.page['meta'].theme = 'neuralix-light'
        q.page['header'].image = 'https://i.imgur.com/yThsZ40.png'
        logging.info('Updating theme to light mode')
    # Save the updated page state
    await q.page.save()

@app("/")
async def serve(q: Q):
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
        title='Neuralix Wind Farm Dashboard',
        icon='https://i.imgur.com/s9w0xce.png',
        theme='neuralix-light',
    )
    q.page["header"] = ui.header_card(
        box=("1 1 10 1"),
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
            ui.toggle(name='toggle_theme', label='', value=q.client.theme_dark, trigger=True),
            # profile in header
            ui.menu(image='default', items=[
                ui.command(name='profile', label='Profile', icon='Contact'),
                ui.command(name='preferences', label='Preferences', icon='Settings'),
                ui.command(name='logout', label='Logout', icon='SignOut'),
            ])
        ]
    )


    q.page["streaming_service"] = ui.frame_card(
        box=("4 2 3 5"),
        title="",
        content=html_content,
    )



    await q.page.save()
