import json


class DataGame:
    def __init__(self, player):
        self.nb_image_success = 0
        self.nb_image_total = 0
        self.words_played = {}
        self.player = player

    def win_image(self, word):
        self.nb_image_success += 1
        self.nb_image_total += 1
        self.words_played[word]["win"] = True

    def try_to_find(self, word):
        if word in self.words_played:
            self.words_played[word]["tries"] += 1
            if self.words_played[word]["tries"] >= 10:
                self.fail_image(word)
        else:
            self.words_played[word]["tries"] = 1

    def fail_image(self, word):
        self.words_played[word]["win"] = False

    def to_json(self):
        data = {
            "player": self.player,
            "nb_image_success": self.nb_image_success,
            "nb_image_total": self.nb_image_total,
            "results": {
                word: {
                    "tries": details["tries"],
                    "win": details["win"]
                } for word, details in self.words_played.items()
            }
        }
        return json.dumps(data, indent=4)