"""Doc"""
from utils import get_next, render_to_frontend, render_bg


class Orange:
    """Represents the fruit orange."""

    orange = "#FFA500"

    # Other class implementations

    def get_orange(self):
        """Doc"""
        return self.orange


def render():
    """Doc"""
    fruit = Orange()
    render_to_frontend(
        fruit.orange
    )  # Rendering a color, but one can get confused with the fruit
    render_bg(fruit.get_orange)


def play_with_magic_numbers():
    """Doc"""
    magic_numbers = {0, 1, 1, 2, 3, 5}

    for elem in magic_numbers:
        magic_numbers.add(get_next(elem))
    return magic_numbers


x = int(input())

if x < 0:
    print("Number is negative")
else:
    if x < 100:
        print("Number is small")
