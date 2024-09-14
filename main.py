# Vòng lặp chính của trò chơi
while True:
    # Các sự kiện của rắn
    event.snake_eat_food(snake, food, score_msg)
    event.snake_hit_wall(snake, game_over_msg, status)
    event.snake_hit_self(snake, game_over_msg, status)