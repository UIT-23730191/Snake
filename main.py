"""
Module main.py

Module này khởi động trò chơi con rắn, thiết lập màn hình và quản lý các sự kiện trò chơi.

Imports:
    time: Thư viện để quản lý thời gian.
    Screen: Class từ thư viện turtle để tạo màn hình trò chơi.
    event: Module chứa các hàm xử lý sự kiện.
    Food: Class để tạo thức ăn cho rắn.
    ScoreMessage, StartMessage, GameOverMessage: Các class để hiển thị thông báo trong trò chơi.
    Snake: Class để tạo và điều khiển con rắn.
    Status: Class để quản lý trạng thái của trò chơi.
"""

import time
from turtle import Screen

import event
from food import Food
from message import ScoreMessage, StartMessage, GameOverMessage
from snake import Snake
from status import Status

# Thiết lập màn hình trò chơi
screen = Screen()
screen.setup(width=600, height=600)  # Kích thước trò chơi
screen.bgcolor("white")  # Set Màu nền
screen.title("SNAKE GAME")  # Set title
screen.tracer(0)

# Khởi tạo các đối tượng trò chơi
snake = Snake()
food = Food()
score_msg = ScoreMessage()
start_msg = StartMessage()
game_over_msg = GameOverMessage()
status = Status()

# Thiết lập các sự kiện bàn phím
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(status.start, "Return")

# Vòng lặp chính của trò chơi
while True:
    screen.update()
    time.sleep(0.1)  # Tốt độ game, càng nhỏ game càng nhanh
    if status.is_start:
        start_msg.hide()
        game_over_msg.hide()
        if status.is_game_over:
            snake.reset()
            score_msg.reset()
            status.is_game_over = False
        snake.move()
        # Các sự kiện của rắn
        event.snake_eat_food(snake, food, score_msg)
        event.snake_hit_wall(snake, game_over_msg, status)
        event.snake_hit_self(snake, game_over_msg, status)
    else:
        start_msg.show()
