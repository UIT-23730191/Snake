from turtle import Turtle
import random


class Food(Turtle):
    """
    Lớp Food kế thừa từ Turtle để tạo ra thức ăn cho trò chơi con rắn.
    """

    def __init__(self):
        """
        Khởi tạo đối tượng Food với các thuộc tính mặc định.
        """
        super().__init__()
        self.shape("circle")  # Hình dạng của thức ăn.
        self.penup()  # Đặt bút lên để không vẽ khi di chuyển.
        self.shapesize(stretch_len=0.7, stretch_wid=0.7)  # Kích thước của thức ăn.
        self.color("blue")  # Màu sắc của thức ăn.
        self.speed("fastest")  # Tốc độ di chuyển của thức ăn.
        self.refresh()

def refresh(self):
    random_x = random.randint(-150, 150)
    random_y = random.randint(-150, 150)
    self.goto(random_x, random_y)

