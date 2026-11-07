#!/usr/bin/env python3
import random


def get_random_word():
    words = []
    with open("wordlist.txt", "r", encoding="utf-8") as file:
        for line in file:
            word = line.strip().lower()
            letters_only = word.replace("-", "").replace(" ", "")
            if letters_only.isalpha():
                words.append(word)
    return random.choice(words)
