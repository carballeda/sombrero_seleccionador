"""
Created on Fri Jun 07 09:36:14 2024

@author: carballeda
"""

# sombrero seleccionador (sorting hat)

import copy
import time
from typing import Any, List

import reflex as rx

from .results import results
from .styles import question_style, page_background


class State(rx.State):
    """The app state."""

    default_answers = [None, None, None, None, None]
    answers: List[Any]
    answer_key = ["1", "4", "3", "1", "2"]
    score: int

    def onload(self):
        self.answers = copy.deepcopy(self.default_answers)

    def set_answers(self, answer, index):
        self.answers[index] = answer

    def submit(self):
        house_scores = {'gryffindor': 0, 'ravenclaw': 0, 'hufflepuff': 0, 'slytherin': 0}
        for i, answer in enumerate(self.answers):
            if i == 0:
                if answer == "1":
                    house_scores['gryffindor'] += 1
                elif answer == "2":
                    house_scores['ravenclaw'] += 1
                elif answer == "3":
                    house_scores['hufflepuff'] += 1
                elif answer == "4":
                    house_scores['slytherin'] += 1
            elif i == 1:
                if answer == "1":
                    house_scores['gryffindor'] += 1
                elif answer == "2":
                    house_scores['ravenclaw'] += 1
                elif answer == "3":
                    house_scores['hufflepuff'] += 1
                elif answer == "4":
                    house_scores['slytherin'] += 1
            elif i == 2:
                if answer == "1":
                    house_scores['gryffindor'] += 1
                elif answer == "2":
                    house_scores['ravenclaw'] += 1
                elif answer == "3":
                    house_scores['hufflepuff'] += 1
                elif answer == "4":
                    house_scores['slytherin'] += 1
            elif i == 3:
                if answer == "1":
                    house_scores['gryffindor'] += 1
                elif answer == "2":
                    house_scores['ravenclaw'] += 1
                elif answer == "3":
                    house_scores['hufflepuff'] += 1
                elif answer == "4":
                    house_scores['slytherin'] += 1
            elif i == 4:
                if answer == "1":
                    house_scores['gryffindor'] += 1
                elif answer == "2":
                    house_scores['ravenclaw'] += 1
                elif answer == "3":
                    house_scores['hufflepuff'] += 1
                elif answer == "4":
                    house_scores['slytherin'] += 1

        self.score = max(house_scores, key=house_scores.get)
        return rx.redirect("/result")

    @rx.var
    def percent_score(self):
        house_names = {
            'gryffindor': 'Gryffindor',
            'ravenclaw': 'Ravenclaw',
            'hufflepuff': 'Hufflepuff',
            'slytherin': 'Slytherin'
        }
        return f"¡Tu casa es {house_names[self.score]}!"


def question1():
    """The main view."""
    return rx.vstack(
        rx.heading("Pregunta #1"),
        rx.text("¿Cuál dirías que es el rasgo que más destaca en tu personalidad?"),
        rx.divider(),
        rx.radio(
            items=[
                "1. Osadía",
                "2. Curiosidad",
                "3. Lealtad",
                "4. Ambición"
            ],
            default_value=State.default_answers[0],
            default_checked=True,
            on_change=lambda answer: State.set_answers(answer, 0),
        ),
    )


def question2():
    return rx.vstack(
        rx.heading("Pregunta #2"),
        rx.text("Entras en un jardín encantado, ¿qué es lo que más llama tu atención?"),
        rx.radio(
            items=[
                "1. Un árbol de hojas de plata con manzanas doradas",
                "2. Unas setas rojas que parecen estar hablando entre sí",
                "3. Un estanque burbujeante en cuyas profundidades hay algo luminoso",
                "4. Una estatua de un viejo mago con un brillo extraño en los ojos"
            ],
            default_value=State.default_answers[1],
            default_check=True,
            on_change=lambda answer: State.set_answers(answer, 1),
        ),
    )


def question3():
    return rx.vstack(
        rx.heading("Pregunta #3"),
        rx.text("Una vez cada siglo el arbusto Flutterby produce flores que adaptan su aroma para atraer a los desprevenidos. Para atraerte a ti debería oler a:"),
        rx.radio(
            items=[
                "1. Un fuego crepitante",
                "2. Pergamino fresco",
                "3. Tu hogar",
                "4. El mar"
            ],
            default_value=State.default_answers[2],
            default_check=True,
            on_change=lambda answer: State.set_answers(answer, 2),
        ),
    )


def question4():
    return rx.vstack(
        rx.heading("Pregunta #4"),
        rx.text("Dos personas se están peleando delante de ti, ¿qué haces?"),
        rx.radio(
            items=[
                "1. Intento separarlas como sea",
                "2. Trato de razonar con ambos y mediar",
                "3. Busco ayuda",
                "4. Dejo que se peleen, la cosa no va conmigo"
            ],
            default_value=State.default_answers[3],
            default_check=True,
            on_change=lambda answer: State.set_answers(answer, 3),
        ),
    )


def question5():
    return rx.vstack(
        rx.heading("Pregunta #5"),
        rx.text("Te gustaría inventar una poción que te asegurase:"),
        rx.radio(
            items=[
                "1. Gloria",
                "2. Sabiduría",
                "3. Amor",
                "4. Poder"
            ],
            default_value=State.default_answers[4],
            default_check=True,
            on_change=lambda answer: State.set_answers(answer, 4),
        ),
    )


def index():
    """The main view."""
    return rx.color_mode.button(position="top-right"), rx.center(
        rx.vstack(
            header(),
            rx.vstack(
                question1(),
                rx.divider(),
                question2(),
                rx.divider(),
                question3(),
                rx.divider(),
                question4(),
                rx.divider(),
                question5(),
                rx.center(
                    rx.button("Submit", width="6em", on_click=State.submit),
                    width="100%",
                ),
                style=question_style,
                spacing="5",
            ),
            align="center",
        ),
        bg=page_background,
        padding_y="2em",
        min_height="100vh",
    )

def result():
    return rx.color_mode.button(position="top-right"), results(State)

app = rx.App(
    theme=rx.theme(
        has_background=True, radius="none", accent_color="orange", appearance="light"
    ),
)
app.add_page(index, title="Quiz - Reflex", on_load=State.onload)
app.add_page(result, title="Quiz Results")
