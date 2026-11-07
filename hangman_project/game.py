class HangmanGame:
    def __init__(self, word):
        self.word = word
        self.guessed_letters = []
        self.wrong_letters = []
        self.errors = 0
        self.max_errors = 6
    def process_guess(self, letter):
        if letter in self.word:
            self.guessed_letters.append(letter)
            return True

        self.wrong_letters.append(letter)
        self.errors += 1
        return False

    def display_progress(self):
        progress = ""

        for character in self.word:
            if not character.isalpha() or character in self.guessed_letters:
                progress += character
            else:
                progress += "_"

        return progress

    def is_won(self):
        for character in self.word:
            if character.isalpha() and character not in self.guessed_letters:
                return False

        return True

    def is_lost(self):
        return self.errors >= self.max_errors
