from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Message(Turtle):
 """
    Lớp Message kế thừa từ Turtle để hiển thị các thông báo trong trò chơi.

    Attributes:
        is_showing (bool): Trạng thái hiển thị của thông báo.
    """
    def __init__(self):
        super().__init__()
        self.color("red")   # Set màu chữ
        self.penup()
        self.hideturtle()

class ScoreMessage(Message):

    def __init__(self):
        super().__init__()
        self.score = 0 
        self.goto(0, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(0, 260)
        self.write_message(f"Score: {self.score}")

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
    def reset(self):
        self.score = 0
        self.clear()
        self.update_scoreboard()
    
class StartMessage(Message):
    def __init__(self):
        super().__init__()
        self.goto(0, 40)

    def show(self):
        self.write_message("Press enter to start")

    def hide(self):
        self.clear()

class GameOverMessage(Message):
    def __init__(self):
        super().__init__()

    def show(self):
        self.goto(0, 80)
        self.write_message("Game Over! Try again?")

    def hide(self):
        self.clear()




