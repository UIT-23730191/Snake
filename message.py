from turtle import Turtle


class Message(Turtle):

    def __init__(self):




        super().__init__()
        self.color("red")   # Set màu chữ
        self.penup()
        self.hideturtle()

class ScoreMessage(Message):

    def __init__(self):





class StartMessage(Message):
    def __init__(self):



class GameOverMessage(Message):
    def __init__(self):



