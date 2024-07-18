import random
from src.chatbot import generate_answer

WORDS = [
    'voiture',
    'chateau',
    'maison',
    'velo',
    'feuille',
    'arbre',
    'soleil',
    'bateau',
    'pyramide',
]

class Game:

    def __init__(self):
        self.new_game()
        self.last_prediction = ''

    def new_game(self):
        self.words = WORDS
        random.shuffle(self.words)

        self.current_word_idx = 0

    def next_word(self):
        self.current_word_idx = self.current_word_idx + 1

    def current_word(self):
        return self.words[self.current_word_idx % len(self.words)]

    def evaluate_paint(self, image_data) -> str:
        response = generate_answer(image_data)
        self.last_prediction = response
        return response
