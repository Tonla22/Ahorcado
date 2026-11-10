#!/usr/bin/env python3
"""Módulo que define la clase principal con la lógica del juego del Ahorcado."""


class HangmanGame:
    """Representa una partida del juego del Ahorcado y su estado actual."""

    def __init__(self, word):
        """Inicializa el juego con la palabra objetivo y contadores en cero."""
        self.word = word.lower()
        self.guessed_letters = []
        self.wrong_letters = []
        self.errors = 0
        self.max_errors = 6

    def process_guess(self, letter):
        """Procesa una letra ingresada y actualiza aciertos o errores."""
        letter = letter.lower()
        if letter in self.word:
            if letter not in self.guessed_letters:
                self.guessed_letters.append(letter)
            return True

        if letter not in self.wrong_letters:
            self.wrong_letters.append(letter)
        self.errors += 1
        return False

    def display_progress(self):
        """Devuelve el estado actual de la palabra con guiones bajos y letras reveladas."""
        progress = []

        for character in self.word:
            if not character.isalpha() or character in self.guessed_letters:
                progress.append(character)
            else:
                progress.append("_")

        return " ".join(progress)

    def is_won(self):
        """Indica si todas las letras alfabéticas de la palabra fueron adivinadas."""
        for character in self.word:
            if character.isalpha() and character not in self.guessed_letters:
                return False

        return True

    def is_lost(self):
        """Indica si el jugador alcanzó el límite máximo de errores."""
        return self.errors >= self.max_errors
