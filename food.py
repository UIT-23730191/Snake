from turtle import Turtle


class Food(Turtle):

    def __init__(self):

def refresh(self):
    random_x = random.randint(-150, 150)
    random_y = random.randint(-150, 150)
    self.goto(random_x, random_y)

