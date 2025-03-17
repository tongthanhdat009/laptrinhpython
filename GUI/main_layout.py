from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QListWidget, QStackedWidget, QLabel
from user.UserMenu import UserMenu
from user.UserContent import UserContent
from user.MusicPlayerBar import MusicPlayerBar

class MainLayout(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("SGU Music")
        self.setFixedSize(1500, 750)
        
        # Layout chính
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)

        center_layout = QHBoxLayout()
        center_layout.setSpacing(0)
        
        # Thanh menu bên trái
        self.menu = UserMenu()
        center_layout.addWidget(self.menu)
        
        # Nội dung bên phải
        self.content = UserContent()
        center_layout.addWidget(self.content)
        

        player_widget = MusicPlayerBar()
        bot_layout = QVBoxLayout()
        bot_layout.addWidget(player_widget)
        bot_layout.setContentsMargins(0, 0, 0, 0)
        bot_layout.setSpacing(0)

        main_layout.addLayout(center_layout)
        main_layout.addLayout(bot_layout)
        
        self.setLayout(main_layout)

# Chạy ứng dụng
if __name__ == "__main__":
    app = QApplication([])
    window = MainLayout()
    window.show()
    app.exec()