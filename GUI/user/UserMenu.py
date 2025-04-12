from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QFrame
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QPixmap

class UserMenu(QWidget):
    def __init__(self, switch_callback):
        super().__init__()
        self.setFixedSize(250, 650)
        
        # **Dùng QFrame để giữ màu nền**
        frame = QFrame(self)
        frame.setStyleSheet("background-color: #f2f2f2;")
        frame.setFixedSize(250, 650)

        layout = QVBoxLayout(frame)
        layout.setContentsMargins(10, 10, 10, 10)
        layout.setAlignment(Qt.AlignmentFlag.AlignTop)

        # Tiêu đề "SGU Music"
        title_label = QLabel('<span style="color: blue; font-size: 35px; font-weight: bold;">SGU</span> <span style="color: gray; font-size: 18px;">Music</span>')
        title_label.setStyleSheet("font-weight: bold;")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setContentsMargins(0, 0, 0, 20)
        layout.addWidget(title_label)

        def create_button(text, icon_path, page_name):
            button = QPushButton(text)
            button.setIcon(QIcon(QPixmap(icon_path).scaled(32, 32, Qt.AspectRatioMode.KeepAspectRatio)))
            button.setStyleSheet("font-weight: bold; color: gray; font-size: 16px; text-align: left; padding: 5px;")
            button.setFixedHeight(45)

            # Kết nối sự kiện hover vào nút
            def on_enter():
                button.setStyleSheet("font-weight: bold; color: blue; font-size: 16px; text-align: left; padding: 5px;")
                button.setIcon(QIcon())  # Ẩn icon khi hover

            def on_leave():
                button.setStyleSheet("font-weight: bold; color: gray; font-size: 16px; text-align: left; padding: 5px;")
                button.setIcon(QIcon(QPixmap(icon_path).scaled(32, 32, Qt.AspectRatioMode.KeepAspectRatio)))

            button.enterEvent = lambda event: on_enter()
            button.leaveEvent = lambda event: on_leave()

            # Kết nối sự kiện clicked với callback truyền vào
            button.clicked.connect(lambda: switch_callback(page_name))

            return button

        # Tạo các nút với callback tương ứng
        self.btn_home = create_button("Trang Chủ", "assets/icon/home.png", "GUITrangChu")
        layout.addWidget(self.btn_home)

        self.btn_search = create_button("Tìm Kiếm", "assets/icon/search.png", "GUITimKiem")
        layout.addWidget(self.btn_search)

        self.btn_chart = create_button("BXH Bài Hát", "assets/icon/chart.png", "GUIBXHBaiHat")
        layout.addWidget(self.btn_chart)

        self.btn_history = create_button("Lịch Sử Nghe", "assets/icon/history.png", "GUILichSuNghe")
        layout.addWidget(self.btn_history)

        self.btn_favorite = create_button("Bài Hát Yêu Thích", "assets/icon/favorite.png", "GUIBaiHatYeuThich")
        layout.addWidget(self.btn_favorite)

        self.btn_playlist = create_button("Danh Sách Phát", "assets/icon/playlist.png", "GUIDanhSachPhat")
        layout.addWidget(self.btn_playlist)

        # In ra các nút đã tạo để kiểm tra
        print("Nút 'Trang Chủ' đã được tạo!")
        print("Nút 'BXH Bài Hát' đã được tạo!")
        print("Nút 'Lịch Sử Nghe' đã được tạo!")
        print("Nút 'Bài Hát Yêu Thích' đã được tạo!")
        print("Nút 'Danh Sách Phát' đã được tạo!")
    
        frame.setLayout(layout)

        main_layout = QVBoxLayout(self)
        main_layout.addWidget(frame)
        main_layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(main_layout)
