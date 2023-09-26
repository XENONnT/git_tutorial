"""Third docstring"""

from cowsay import cow


def check_if_script():
    """Tell if this module is run as script or is imported as module."""

    if __name__ == "__main__":
        cow(f"You're running module_1 as a script!\nTherefore {__name__=}")
    else:
        cow(f"module_1 was imported!\nTherefore {__name__=}")


class Herd():
    """Create herd of cow saying things.

    Update on cowsay to have multiple cows chanting the same thing.
    :param n_cows: Number of cows in herd.
    """

    def __init__(self, n_cows: int = 3) -> None:
        self.n_cows = n_cows

    def say(self, message: str) -> None:
        """Print heard of cows saying the message."""
        for _ in range(self.n_cows):
            cow(message)


if __name__ == "__main__":
    check_if_script()
