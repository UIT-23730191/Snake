from turtle import Turtle


class Message(Turtle):

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



class GameOverMessage(Message):
    def __init__(self):



