#!/usr/bin/env python3
"""Funciones auxiliares para carga de palabras y visualización del estado."""

import os
import random


def get_random_word():
    """Lee wordlist.txt y devuelve una palabra o frase seleccionada al azar."""
    words = []
    wordlist_path = os.path.join(os.path.dirname(__file__), "wordlist.txt")
    with open(wordlist_path, "r", encoding="utf-8") as file:
        for line in file:
            word = line.strip().lower()
            letters_only = word.replace("-", "").replace(" ", "")
            if letters_only.isalpha():
                words.append(word)
    return random.choice(words)


def show_status(game):
    """Muestra en consola el progreso de la palabra, intentos y letras usadas."""
    print("Palabra:", game.display_progress())
    print("Letras adivinadas:", ", ".join(game.guessed_letters))
    print("Letras incorrectas:", ", ".join(game.wrong_letters))
    print(f"Te quedan {game.max_errors - game.errors} intentos")
