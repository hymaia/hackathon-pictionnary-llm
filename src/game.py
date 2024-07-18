import random
from src.chatbot import generate_answer

WORDS = [
    'voiture',
    'chateau',
    'maison',
    'chien',
    'chat',
    'velo',
    'feuille',
    'arbre',
    'soleil',
    'bateau',
]

class Game:

    def __init__(self):
        self.new_game()

    def new_game(self):
        self.words = WORDS
        random.shuffle(self.words)

        self.current_word_idx = 0

    def next_word(self):
        self.current_word_idx = self.current_word_idx + 1

    def current_word(self):
        return self.words[self.current_word_idx % len(self.words)]

    def evaluate_paint(self, image_data) -> bool:
        print("Word to find: ", self.current_word())
        response = generate_answer(image_data, WORDS)
        print("Word predicted: ", response)
        if response.lower() == self.current_word().lower():
            print("Yeah it's good !")
            return True
        else:
            print("Nope")
            return False
