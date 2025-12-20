from flet import Page, SafeArea, app, FloatingActionButton, Icons
from widgets.Counter import Counter

def main(page: Page):
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"

    counter = Counter()

    page.floating_action_button = FloatingActionButton(
        icon=Icons.ADD,
        on_click=counter.add_count
    )

    page.add(
        SafeArea(
            content=counter,
            expand=True
        )
    )
    page.update()

app(target=main)