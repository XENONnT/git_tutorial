"""Doscstring"""

import package.module_1 as m1


def main() -> None:
    herd = m1.Herd(2)
    herd.say("Welcome to XENONnT")


if __name__ == "__main__":
    m1.check_if_script()
    main()
