import reflex as rx

from .styles import base_style as answer_style
from .styles import page_background


def results(State):
    house_names = {
        'gryffindor': 'Gryffindor',
        'ravenclaw': 'Ravenclaw',
        'hufflepuff': 'Hufflepuff',
        'slytherin': 'Slytherin'
    }

    house_descriptions = {
        'gryffindor': '¡Tu casa es la de los valientes Gryffindor!',
        'ravenclaw': '¡Tu casa es la de los sabios Ravenclaw!',
        'hufflepuff': '¡Tu casa es la de los leales Hufflepuff!',
        'slytherin': '¡Tu casa es la de los ambiciosos Slytherin!'
    }

    return rx.center(
        rx.vstack(
            rx.heading("Resultados"),
            rx.text("Aquí está el resultado de tu quiz."),
            rx.divider(),
            rx.text(
                f"¡Felicitaciones! {house_descriptions[State.score]}",
                style={"font-size": "2em", "color": "orange"},
                text_align="center",
            ),
            rx.divider(),
            rx.link(rx.button("Volver a realizar el quiz"), href="/"),
            style=answer_style,
        ),
        bg=page_background,
        min_height="100vh",
    )
