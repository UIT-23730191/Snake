from turtle import Turtle

START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    """
    Lớp Snake để tạo và điều khiển con rắn trong trò chơi.

    Attributes:
        segments (list): Danh sách các đoạn của con rắn.
        head (Turtle): Đoạn đầu tiên của con rắn.
    """

    def __init__(self):
        """
        Khởi tạo đối tượng Snake với các đoạn ban đầu và đặt đầu rắn là vị trí đầu tiên
        """
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
    
    def reset(self):
        """
        Đặt lại con rắn về trạng thái ban đầu.
        """
        self.remove_snake()
        self.__init__()
    
    def create_snake(self):
        """
        Tạo con rắn với các đoạn ban đầu tại các vị trí xác định.
        """
        for position in START_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        """
        Thêm một đoạn mới vào con rắn tại vị trí xác định.

        Parameters:
        position (tuple): Vị trí (x, y) để thêm đoạn mới.

        Returns:
        None
        """
        new_segment = Turtle("square")
        new_segment.color("black")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def remove_snake(self):
        """
        Xóa tất cả các đoạn của con rắn khỏi màn hình.
        """
        for segment in self.segments:
            segment.hideturtle()
            segment.clear()

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)





