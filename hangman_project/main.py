#!/usr/bin/env python3
"""Punto de entrada y flujo principal del juego del Ahorcado."""

from game import HangmanGame
from utils import get_random_word, show_status


def get_valid_letter(game):
    """Solicita y valida que se ingrese una letra única y no repetida."""
    while True:
        print("")
        inp = input("Ingresa una letra: ").strip().lower()
        print("\n")
        if len(inp) != 1 or not inp.isalpha():
            print("")
            print("No ingresaste ninguna letra válida.")
        elif inp in game.guessed_letters or inp in game.wrong_letters:
            print("")
            print("La letra ya fue ingresada anteriormente.")
        else:
            return inp


def main():
    """Inicializa la partida y ejecuta el bucle principal del juego."""
    word = get_random_word()
    game = HangmanGame(word)

    while not game.is_won() and not game.is_lost():
        show_status(game)
        letter = get_valid_letter(game)
        if game.process_guess(letter):
            print(f'Bien! La letra "{letter}" está.')
        else:
            print(f'Incorrecto. La letra "{letter}" no está.')

    print("")
    show_status(game)
    print("")
    if game.is_won():
        print(f"¡Ganaste! Crack. La palabra era: '{game.word}'")
    else:
        print(f"Fin del juego. La palabra era: '{game.word}'")


if __name__ == "__main__":
    main()
