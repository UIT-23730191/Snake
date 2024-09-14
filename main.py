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