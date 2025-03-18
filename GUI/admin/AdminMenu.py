from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QFrame
from PyQt6.QtCore import Qt

class AdminMenu(QWidget):
    def __init__(self, switch_callback):
        super().__init__()
        self.setFixedSize(250, 650)

        # **Dùng QFrame để giữ màu nền**
        frame = QFrame(self)
        frame.setStyleSheet("background-color: #f2f2f2;")
        frame.setFixedSize(250, 650)

        layout = QVBoxLayout(frame)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)  # Đưa nội dung lên trên cùng

        # Tiêu đề "SGU Music"
        title_label = QLabel('<span style="color: blue; font-size: 35px; font-weight: bold;">SGU</span> <span style="color: gray; font-size: 18px;">Music</span>')
        title_label.setStyleSheet("font-weight: bold;")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setContentsMargins(0,0,0,20)
        layout.addWidget(title_label)

        # Nút Quản lý bài hát
        self.btn_manage_songs = QPushButton("Quản lý bài hát")
        self.btn_manage_songs.setStyleSheet("font-weight: bold; color: gray; font-size: 16px; text-align: left; padding: 5px;")
        self.btn_manage_songs.setFixedHeight(45)
        self.btn_manage_songs.clicked.connect(lambda: switch_callback(0))
        layout.addWidget(self.btn_manage_songs)

        # Nút Quản lý ca sĩ
        self.btn_manage_artists = QPushButton("Quản lý ca sĩ")
        self.btn_manage_artists.setStyleSheet("font-weight: bold; color: gray; font-size: 16px; text-align: left; padding: 5px;")
        self.btn_manage_artists.setFixedHeight(45)
        self.btn_manage_artists.clicked.connect(lambda: switch_callback(1))
        layout.addWidget(self.btn_manage_artists)

        # Nút Tạo danh sách phát
        self.btn_create_playlist = QPushButton("Tạo danh sách phát")
        self.btn_create_playlist.setStyleSheet("font-weight: bold; color: gray; font-size: 16px; text-align: left; padding: 5px;")
        self.btn_create_playlist.setFixedHeight(45)
        self.btn_create_playlist.clicked.connect(lambda: switch_callback(2))
        layout.addWidget(self.btn_create_playlist)


        frame.setLayout(layout)  # Gán layout cho QFrame

        main_layout = QVBoxLayout(self)
        main_layout.addWidget(frame)
        main_layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(main_layout)
