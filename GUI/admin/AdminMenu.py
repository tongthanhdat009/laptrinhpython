from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QFrame
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QIcon

class AdminMenu(QWidget):
    def __init__(self, switch_content_admin):
        super().__init__()
        self.setFixedSize(250, 650)

        # Dùng QFrame để giữ màu nền
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
        title_label.setContentsMargins(0, 0, 0, 20)
        layout.addWidget(title_label)

        # Nút Quản lý bài hát
        self.btn_manage_songs = QPushButton("Quản lý bài hát")
        self.btn_manage_songs.setStyleSheet("font-weight: bold; color: gray; font-size: 16px; text-align: left; padding: 5px;")
        self.btn_manage_songs.setFixedHeight(45)
        self.btn_manage_songs.clicked.connect(lambda: switch_content_admin("GUIQuanLyBaiHat"))
        layout.addWidget(self.btn_manage_songs)

        # Nút Quản lý ca sĩ
        self.btn_manage_artists = QPushButton("Quản lý ca sĩ")
        self.btn_manage_artists.setStyleSheet("font-weight: bold; color: gray; font-size: 16px; text-align: left; padding: 5px;")
        self.btn_manage_artists.setFixedHeight(45)
        self.btn_manage_artists.clicked.connect(lambda: switch_content_admin("GUIQuanLyCaSi"))
        layout.addWidget(self.btn_manage_artists)

        # Nút Quản lý danh sách phát
        self.btn_manage_playlists = QPushButton("Quản lý danh sách phát")
        self.btn_manage_playlists.setStyleSheet("font-weight: bold; color: gray; font-size: 16px; text-align: left; padding: 5px;")
        self.btn_manage_playlists.setFixedHeight(45)
        self.btn_manage_playlists.clicked.connect(lambda: switch_content_admin("GUIQuanLyDanhSachPhatHeThong"))
        layout.addWidget(self.btn_manage_playlists)

        # Nút Quản lý người dùng
        self.btn_manage_users = QPushButton("Quản lý người dùng")
        self.btn_manage_users.setStyleSheet("font-weight: bold; color: gray; font-size: 16px; text-align: left; padding: 5px;")
        self.btn_manage_users.setFixedHeight(45)
        self.btn_manage_users.clicked.connect(lambda: switch_content_admin("GUIQuanLyNguoiDung"))
        layout.addWidget(self.btn_manage_users)


        layout.addStretch()  
        # Nút quay về trang chủ với icon và chữ
        self.btn_back_arrow = QPushButton(" Quay về trang chủ")
        self.btn_back_arrow.setIcon(QIcon("assets/icon/back.png"))  # Sử dụng đúng đường dẫn tới icon mũi tên qua trái
        self.btn_back_arrow.setIconSize(QSize(20, 20))  # Kích thước của icon
        self.btn_back_arrow.setStyleSheet("""
            QPushButton {
                background-color: #007bff;  /* Màu xanh */
                color: white;  /* Màu chữ trắng */
                font-size: 16px;  /* Kích thước chữ */
                font-weight: bold;  /* Chữ đậm */
                text-align: left;  /* Căn chữ sang trái */
                border: none;
                border-radius: 5px;
                padding: 8px 15px;  /* Khoảng cách giữa nội dung và viền */
            }
            QPushButton:hover {
                background-color: #0056b3;  /* Màu xanh đậm hơn khi hover */
            }
        """)
        self.btn_back_arrow.clicked.connect(lambda: switch_content_admin("User"))
        layout.addWidget(self.btn_back_arrow)

        frame.setLayout(layout)  # Gán layout cho QFrame

        main_layout = QVBoxLayout(self)
        main_layout.addWidget(frame)
        main_layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(main_layout)