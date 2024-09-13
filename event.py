def snake_eat_food(snake, food, score_msg):
    if snake.head.distance(food) < 10:
        food.refresh()
        snake.extend()
        score_msg.increase_score()


def snake_hit_wall(snake, game_over_msg, status):



def snake_hit_self(snake, game_over_msg, status):

