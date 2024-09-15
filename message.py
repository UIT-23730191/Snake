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
        """
        Khởi tạo đối tượng Message với các thuộc tính mặc định.
        """
        super().__init__()
        self.color("red")   # Set màu chữ
        self.penup()# Đặt bút lên để không vẽ khi di chuyển.
        self.hideturtle()# Trạng thái hiển thị của thông báo.

    def write_message(self, arg):
        """
        Viết thông báo lên màn hình.

        Parameters:
        arg (str): Nội dung thông báo.

        Returns:
        None
        """
        super().write(arg, align=ALIGNMENT, font=FONT)

class ScoreMessage(Message):
    """
    Lớp ScoreMessage kế thừa từ Message để hiển thị và cập nhật điểm số.

    Attributes:
        score (int): Điểm số của người chơi.
    """
    def __init__(self):
        """
        Khởi tạo đối tượng ScoreMessage với điểm số ban đầu là 0 và đặt vị trí hiển thị.
        """
        super().__init__()
        self.score = 0 
        self.goto(0, 260)
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Cập nhật bảng điểm với điểm số hiện tại.

        Returns:
        None
        """
        self.goto(0, 260)
        self.write_message(f"Score: {self.score}")

    def increase_score(self):
        """
        Tăng điểm số và cập nhật bảng điểm.
        Returns:
        None
        """
        self.score += 1
        self.clear()
        self.update_scoreboard()
    def reset(self):
        """
        Đặt lại điểm số về 0 và cập nhật bảng điểm.

        Returns:
        None
        """
        self.score = 0
        self.clear()
        self.update_scoreboard()
    
class StartMessage(Message):
    """
    Lớp StartMessage kế thừa từ Message để hiển thị thông báo bắt đầu trò chơi.
    """
    def __init__(self):
        """
        Khởi tạo đối tượng StartMessage và đặt vị trí hiển thị.
        """
        super().__init__()
        self.goto(0, 40)

    def show(self):
        """
        Hiển thị thông báo bắt đầu trò chơi.
        Returns:
        None
        """
        self.write_message("Press enter to start")

    def hide(self):
        """
        Ẩn thông báo bắt đầu trò chơi.
        Returns:
        None
        """
        self.clear()

class GameOverMessage(Message):
    """
    Lớp GameOverMessage kế thừa từ Message để hiển thị thông báo kết thúc trò chơi.
    """
    def __init__(self):
        """
        Khởi tạo đối tượng GameOverMessage và đặt vị trí hiển thị.
        """
        super().__init__()
        self.goto(0,80)

    def show(self):
        """
        Hiển thị thông báo kết thúc trò chơi.

        Returns:
        None
        """
        if not self.is_showing:
            self.write_message("Game Over! Try again?")
            self.is_showing = True

    def hide(self):
        self.clear()




