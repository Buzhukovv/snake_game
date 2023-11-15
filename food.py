from turtle import Turtle
import random
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x_rand = random.randint(-330, 330)
        y_rand = random.randint(-330, 330)
        self.goto(x_rand, y_rand)


