SNAKE GAME

GIỚI THIỆU
	- Đây là một trò chơi con rắn đơn giản được viết bằng Python sử dụng thư viện turtle. Người chơi điều khiển con rắn để ăn thức ăn và ghi điểm. Trò chơi kết thúc khi con rắn đâm vào tường hoặc tự cắn vào thân mình.

CÀI ĐẶT
	- Đảm bảo bạn đã cài đặt Python trên máy tính của mình. Bạn có thể tải Python từ python.org.
	- Cài đặt thư viện turtle nếu chưa có:
		> pip install PythonTurtle

HƯỚNG DẪN CHƠI
	- Chạy tệp main.py để bắt đầu trò chơi.
		> python main.py

	- Sử dụng các phím mũi tên để điều khiển con rắn:
		- Up: Di chuyển lên
		- Down: Di chuyển xuống
		- Left: Di chuyển sang trái
		- Right: Di chuyển sang phải
		- Nhấn phím Enter để bắt đầu trò chơi.

	- Con rắn sẽ di chuyển và bạn cần điều khiển nó để ăn thức ăn xuất hiện ngẫu nhiên trên màn hình.
	- Trò chơi kết thúc khi con rắn đâm vào tường hoặc tự cắn vào thân mình. Điểm số sẽ được hiển thị trên màn hình.

CẤU TRÚC DỰ ÁN
	- main.py: Tệp chính để khởi động trò chơi.
	- food.py: Định nghĩa lớp Food để tạo và làm mới thức ăn.
	- message.py: Định nghĩa các lớp Message, ScoreMessage, StartMessage, và GameOverMessage để hiển thị các thông báo trong trò chơi.
	- snake.py: Định nghĩa lớp Snake để tạo và điều khiển con rắn.
	- status.py: Định nghĩa lớp Status để quản lý trạng thái của trò chơi.
	- event.py: Chứa các hàm xử lý sự kiện như con rắn ăn thức ăn, đâm vào tường, hoặc tự cắn vào thân mình.

ĐÓNG GÓP
	- Nếu bạn muốn đóng góp vào dự án, vui lòng tạo một pull request hoặc mở một issue trên GitHub.
