from h2o_wave import Q, ui, main, app, on
import pandas as pd

with open('../JupyterOutputs/monthly_sum_of_lv_activepower.html', 'r') as file:
    monthly_sum_of_lv_activepower = file.read()
with open('../JupyterOutputs/difference_between_year_2_and_year_1_.html', 'r') as file:
    difference_between_year_2_and_year_1_ = file.read()
with open('../JupyterOutputs/gps_coordinates_visualization.html', 'r') as file:
    gps_coordinates_visualization = file.read()
with open('../JupyterOutputs/quarterly_summary_of_changes.html', 'r') as file:
    quarterly_summary_of_changes = file.read()
with open('../JupyterOutputs/mean_time_until_failure_by_machine_model.html', 'r') as file:
    mean_time_until_failure_by_machine_model = file.read()
with open('../JupyterOutputs/top_3_root_causes_of_failure.html', 'r') as file:
    top_3_root_causes_of_failure = file.read()
with open('../JupyterOutputs/failures_by_model.html', 'r') as file:
    failures_by_model = file.read()
with open('../JupyterOutputs/time_series_data_with_threshold.html', 'r') as file:
    time_series_data_with_threshold = file.read()
with open('../JupyterOutputs/stacked_time_series_plot.html', 'r') as file:
    stacked_time_series_plot = file.read()
with open('../JupyterOutputs/turbine_bearings_status.html', 'r') as file:
    turbine_bearings_status = file.read()

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

    q.page["monthly_sum_of_lv_activepower"] = ui.frame_card(
        box=("1 2 10 5"),
        title="",
        content=monthly_sum_of_lv_activepower,
    )


    q.page["difference_between_year_2_and_year_1_"] = ui.frame_card(
        box=("1 7 10 5"),
        title="",
        content=difference_between_year_2_and_year_1_,
    )

    q.page["gps_coordinates_visualization"] = ui.frame_card(
        box=("1 12 5 5"),
        title="",
        content=gps_coordinates_visualization,
    )

    q.page["quarterly_summary_of_changes"] = ui.frame_card(
        box=("6 12 5 5"),
        title="",
        content=quarterly_summary_of_changes,
    )

    q.page["mean_time_until_failure_by_machine_model"] = ui.frame_card(
        box=("6 17 5 5"),
        title="",
        content=mean_time_until_failure_by_machine_model,
    )

    q.page["top_3_root_causes_of_failure"] = ui.frame_card(
        box=("1 22 10 5"),
        title="",
        content=top_3_root_causes_of_failure,
    )

    q.page["failures_by_model"] = ui.frame_card(
        box=("1 27 10 5"),
        title="",
        content=failures_by_model,
    )

    q.page["time_series_data_with_threshold"] = ui.frame_card(
        box=("1 32 10 5"),
        title="",
        content=time_series_data_with_threshold,
    )

    q.page["stacked_time_series_plot"] = ui.frame_card(
        box=("1 37 10 5"),
        title="",
        content=stacked_time_series_plot,
    )

    q.page["turbine_bearings_status"] = ui.frame_card(
        box=("1 42 10 5"),
        title="",
        content=turbine_bearings_status,
    )


    await q.page.save()
