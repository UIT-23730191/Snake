from turtle import Turtle

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    
    def reset(self):
        self.remove_snake()
        self.__init__()

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("black")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def remove_snake(self):
        for segment in self.segments:
            segment.hideturtle()
            segment.clear()

    def extend(self):
        self.add_segment(self.segments[-1].position())




