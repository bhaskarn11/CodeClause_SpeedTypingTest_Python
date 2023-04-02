import pyjokes
from datetime import datetime as dt
from math import ceil


class Game:
    input_text = ""
    words = None
    sentence = ""
    accuracy = 0
    start_time = dt.now()
    total_time = dt.now()
    w_count = 0

    def start_game(self):
        print("Speed Typing Test Game")
        print("============================")
        self.sentence = pyjokes.get_joke()
        print(self.sentence)
        print("============================")
        self.start_time = dt.now()
        self.input_text = input()
        self.total_time = dt.now() - self.start_time
        self.words = self.sentence.split()

        for word in self.input_text.split():
            if word in self.words:
                self.w_count += 1

        self.show_result()

    def show_result(self):
        self.accuracy = self.w_count / len(self.words) * 100
        wps = len(self.input_text.split()) / self.total_time.total_seconds()
        print(f"Total time taken: {ceil(self.total_time.total_seconds())} sec., Accuracy: {ceil(self.accuracy)}%, WPS: {ceil(wps)}")

    def reset_game(self):
        self.input_text = ""
        self.words = None
        self.accuracy = 0
        self.start_time = None
        self.total_time = 0
        self.w_count = 0
        self.start_game()


if __name__ == "__main__":
    g = Game()
    g.start_game()
    op = input("Want to play again? Y or N -> ")
    if op.upper() in ["Y", "YES"]:
        g.reset_game()

    else:
        exit(0)
