class Status: 
    def __init__(self): #Khởi tạo đối tượng
        self.is_start = False
        self.is_game_over = False
        self.is_running = False


    def start(sefl): #Set trạng thái bắt đầu
        self.is_start = True


    def game_over(sefl) #Trạng thái game over
        self.is_game_over = True
        self.is_start = False


