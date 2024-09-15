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
    """
    Xử lý sự kiện khi rắn ăn thức ăn.

    Hàm này kiểm tra xem đầu rắn có gần thức ăn không. Nếu đúng, nó sẽ:
    1. Làm mới vị trí của thức ăn.
    2. Tăng kích thước của rắn.
    3. Tăng điểm số của người chơi.

    Parameters:
    snake (Snake): Đối tượng rắn.
    food (Food): Đối tượng thức ăn.

    Returns:
    None
    """
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_msg.increase_score()

def snake_hit_wall(snake, game_over_msg, status):
    """
    Xử lý sự kiện khi rắn đụng tường.

    Hàm này kiểm tra tọa độ x và y của đầu rắn có vượt quá phạm vi từ -280 đến 280 hay không.
    Nếu đầu rắn vượt quá phạm vi này, hàm sẽ hiển thị thông báo "game over" và cập nhật trạng thái game.

    Parameters:
    snake (Snake): Đối tượng rắn.
    game_over_msg (GameOverMessage): Đối tượng thông báo game over.
    status (Status): Đối tượng trạng thái game.

    Returns:
    None
    """
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
    
