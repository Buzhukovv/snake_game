from turtle import Screen
import time
from snake import Snake
from food import Food
from score_record import Score


screen = Screen()
screen.title("Snake from Nokia 3310")
screen.setup(700, 700)
screen.bgcolor("black")

screen.tracer(0)
snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

is_game_work = True
while is_game_work:
    screen.update()
    time.sleep(0.1)
    snake.movement()

    if snake.head.distance(food) < 15:
        food.refresh()
        score.score_change()
        snake.score_result += 1
        snake.upgrade_snake()
    if snake.head.xcor() > 340 or snake.head.xcor() < -340 or snake.head.ycor() > 340 or snake.head.ycor() < -340:
        score.end_game()
        is_game_work = False

    for segments in snake.whole_snake[1:]:
        if snake.head.distance(segments) < 10:
            score.end_game()
            is_game_work = False

screen.exitonclick()