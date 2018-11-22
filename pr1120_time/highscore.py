from pico2d import *
import time
import pickle
import ui

class Highscore:
    class Entry:
        def __init__(self, score):
            self.score = score
            self.time = time.time()
    MAX_SCORE_COUNT = 5
    FILENAME = "Highscore.pickle"
    def __init__(self):
        self.scores = []
        self.font = ui.getFont(ui.FONT_1, 40)
        self.lastIndex = 0
        self.load()
    def add(self, score):
        inserted = False
        for i in range(len(self.scores)):
            e = self.scores[i]
            if e.score < score.score:
                self.scores.insert(i, score)
                inserted = True
                self.lastRank = i + 1
                break
        if (not inserted):
            self.scores.append(score)
            self.lastRank = len(self.scores)

        if (len(self.scores) > Highscore.MAX_SCORE_COUNT):
            self.scores.pop(-1)
        if self.lastRank <= Highscore.MAX_SCORE_COUNT:
            self.save()
    def load(self):
        try:
            f = open(Highscore.FILENAME, "rb")
            self.scores = pickle.load(f)
            f.close()
            print("Scores:", self.scores)
        except FileNotFoundError:
            print("No highscore file")

    def save(self):
        f = open(Highscore.FILENAME, "wb")
        pickle.dump(self.scores, f)
        f.close()
    def draw(self):
        no = 1
        y = 160
        for e in self.scores:
            str = "{:2d} {:5.1f}".format(no, e.score)
            color = (255, 255, 128) if no == self.lastRank else (223, 255, 223)
            self.font.draw(30, y, str, color)
            self.font.draw(220, y, time.asctime(time.localtime(e.time)), color)
            y -= 30
            no += 1
