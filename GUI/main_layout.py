from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout
from user.UserContent import UserContent
from user.MusicPlayerBar import MusicPlayerBar
from admin.AdminContent import AdminContent
from DTO.DTONguoiDung import DTONguoiDung

class MainLayout(QWidget):
    def __init__(self, user: DTONguoiDung):
        super().__init__()
        self.setWindowTitle("SGU Music")
        self.setFixedSize(1500, 750)

        # Layout chính
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)

        # Center layout chứa UserContent hoặc AdminContent
        self.center_layout = QHBoxLayout()
        self.center_layout.setSpacing(0)

        # Nội dung ban đầu là UserContent
        self.player_widget = MusicPlayerBar()
        self.content = UserContent(user, self.switch_content, self.player_widget.load_song_list)
        self.center_layout.addWidget(self.content)

        # Thanh điều khiển âm nhạc

        # Thêm vào main_layout
        main_layout.addLayout(self.center_layout)
        main_layout.addWidget(self.player_widget)

        self.setLayout(main_layout)

    def switch_content(self, page):
        # Xóa widget hiện tại
        self.content.deleteLater()

        if page == "User":
            # Tạo lại UserContent nếu chuyển về User
            self.content = UserContent(user, self.switch_content, self.player_widget.load_song_list)
        elif page == "Admin":
            # Tạo lại AdminContent nếu chuyển sang Admin
            self.content = AdminContent(self.switch_content)
        self.center_layout.addWidget(self.content)
        
    def switch_songs(self, songs):
        self.player_widget.update_songs(songs)
# Chạy ứng dụng
if __name__ == "__main__":
    app = QApplication([])
    user = DTONguoiDung(1, "Nguyễn Minh A", "user1", "123", "admin", "assets/Avatar/0.png", 1)
    window = MainLayout(user)
    window.show()
    app.exec()