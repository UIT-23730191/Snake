from turtle import Turtle

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    
    def reset(self):
        self.remove_snake()
        self.__init__()





