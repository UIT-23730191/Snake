def snake_eat_food(snake, food, score_msg):
    if snake.head.distance(food) < 10:
        food.refresh()
        snake.extend()
        score_msg.increase_score()


def snake_hit_wall(snake, game_over_msg, status):
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_over_msg.show()
        status.game_over()
        return True
    return False


def snake_hit_self(snake, game_over_msg, status):

