class Status:
    """
    Lớp Status để quản lý trạng thái của trò chơi.
    Attributes:
        is_start (bool): Trạng thái bắt đầu của trò chơi.
        is_game_over (bool): Trạng thái kết thúc của trò chơi.
        is_running (bool): Trạng thái đang chạy của trò chơi.
    """
    def __init__(self): #Khởi tạo đối tượng
        self.is_start = False
        self.is_game_over = False
        self.is_running = False
    def start(self): #Set trạng thái bắt đầu
        """
        Đặt trạng thái bắt đầu của trò chơi thành True.
        Returns:
        None
        """
        self.is_start = True


    def game_over(self): #Trạng thái game over
        """
        Đặt trạng thái kết thúc của trò chơi thành True và trạng thái bắt đầu thành False.
        Returns:
        None
        """
        self.is_game_over = True
        self.is_start = False
