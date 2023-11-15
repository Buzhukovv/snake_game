from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = -1
        self.color("red")
        self.penup()
        self.hideturtle()
        top_height = 320
        self.goto(0, top_height)
        self.score_change()

    def change_the_score(self):
        self.score += 1
        self.clear()

    def score_change(self):
        self.change_the_score()
        self.write(f"Score: {self.score}", move=False, align='center', font=("arial", 20, "normal"))

    def end_game(self):
        self.goto(0, 0)
        self.write("Game Over!!!", align='center', font=("arial", 20, "normal"))

    def score_res(self):
        print(self.score)
        return self.score
