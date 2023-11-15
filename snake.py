from turtle import Turtle
from score_record import Score
class Snake:
    def __init__(self):
        self.snake_segments = None
        self.position_for_x = 0
        self.position_for_y = 0
        self.whole_snake = []
        self.score_result = 3
      #  self.score_result = self.score_result + score.score
        self.create_snake()
        self.head = self.whole_snake[0]

    def create_snake(self):
        for i in range(self.score_result):
            self.snake_char()
            self.position_for_x -= 20
            self.snake_segments.goto(self.position_for_x, self.position_for_y)
            self.whole_snake.append(self.snake_segments)

    def snake_char(self):
        self.snake_segments = Turtle()
        self.snake_segments.penup()
        self.snake_segments.shape("square")
        self.snake_segments.color("white")

    def upgrade_snake(self):
        self.snake_char()
        self.snake_segments.goto(self.whole_snake[-1].xcor(), self.whole_snake[-1].ycor())
        self.whole_snake.append(self.snake_segments)

    def up(self):
        current_direction = self.head.heading()
        if current_direction == 180:
            self.head.right(90)
        elif current_direction == 0:
            self.head.left(90)

    def down(self):
        current_direction = self.head.heading()
        if current_direction == 180:
            self.head.left(90)
        elif current_direction == 0:
            self.head.right(90)

    def left(self):
        current_direction = self.head.heading()
        if current_direction == 90:
            self.head.left(90)
        elif current_direction == 270:
            self.head.right(90)

    def right(self):
        current_direction = self.head.heading()
        if current_direction == 90:
            self.head.right(90)
        elif current_direction == 270:
            self.head.left(90)

    def movement(self):
        for number_of_seg in range((len(self.whole_snake) - 1), 0, -1):
            new_x = self.whole_snake[number_of_seg - 1].xcor()
            new_y = self.whole_snake[number_of_seg - 1].ycor()
            self.whole_snake[number_of_seg].goto(new_x, new_y)
        self.head.forward(20)
