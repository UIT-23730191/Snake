# Thiết lập màn hình trò chơi
screen = Screen()
screen.setup(width=600, height=600)  # Kích thước trò chơi
screen.bgcolor("white")  # Set Màu nền
screen.title("SNAKE GAME")  # Set title
screen.tracer(0)

# Thiết lập các sự kiện bàn phím
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(status.start, "Return")