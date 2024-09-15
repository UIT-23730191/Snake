"""
Module event.py

Module này chứa các hàm xử lý sự kiện cho trò chơi con rắn, bao gồm sự kiện rắn ăn thức ăn, đụng tường, và đụng thân
mình.

Functions:
    snake_eat_food(snake, food, score_msg): Xử lý sự kiện khi rắn ăn thức ăn.
    snake_hit_wall(snake, game_over_msg, status): Xử lý sự kiện khi rắn đụng tường.
    snake_hit_self(snake, game_over_msg, status): Xử lý sự kiện khi rắn đụng thân mình.
"""

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
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_over_msg.show()
            status.game_over()
            return True
    return False
    
