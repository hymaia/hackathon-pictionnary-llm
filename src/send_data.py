import json


class DataGame:
    def __init__(self):
        self.nb_image_success = 0
        self.nb_image_total = 0
        self.words_played = {}

    def win_image(self, word):
        self.nb_image_success += 1
        self.nb_image_total += 1
        self.words_played[word]["win"] = True

    def try_to_find(self, word):
        if word in self.words_played:
            self.words_played[word]["tries"] += 1
        else:
            self.words_played[word] = {}
            self.words_played[word]["tries"] = 1
            self.words_played[word]["win"] = False

    def fail_image(self, word):
        self.words_played[word]["win"] = False

    def to_json(self, player):
        data = {
            "player": player,
            "game": 1,  # Assuming game is always 1 for this example, modify as needed
            "results": [
                {
                    "word": word,
                    "tries": details["tries"],
                    "win": details["win"]
                } for word, details in self.words_played.items()
            ]
        }
        return json.dumps(data, indent=4)