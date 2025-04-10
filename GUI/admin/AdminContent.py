from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QStackedWidget
from admin.AdminMenu import AdminMenu
from admin.GUIQuanLyBaiHat import GUIQuanLyBaiHat
from admin.GUIQuanLyCaSi import GUIQuanLyCaSi
from admin.GUIQuanLyDanhSachPhatHeThong import GUIQuanLyDanhSachPhatHeThong
from admin.GUIQuanLyNguoiDung import GUIQuanLyNguoiDung

class AdminContent(QWidget):
    def __init__(self, switch_content):
        super().__init__()
        self.setFixedSize(1500, 650)
        self.setStyleSheet("background-color: #ffffff; margin: 0; padding: 0;")

        # Lưu lại hàm chuyển đổi trang User từ MainLayout
        self.switch_content = switch_content

        # Layout chính
        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)

        # Thanh menu
        self.menu = AdminMenu(self.switch_content_admin)
        layout.addWidget(self.menu, 1)

        # QStackedWidget để chứa các trang khác nhau
        self.stacked_widget = QStackedWidget()

        # Thêm các trang vào stacked_widget
        self.stacked_widget.addWidget(GUIQuanLyBaiHat())  # Trang quản lý bài hát
        self.stacked_widget.addWidget(GUIQuanLyCaSi())  # Trang quản lý ca sĩ
        self.stacked_widget.addWidget(GUIQuanLyDanhSachPhatHeThong())  # Trang quản lý danh sách phát
        self.stacked_widget.addWidget(GUIQuanLyNguoiDung())  # Trang quản lý người dùng

        # Layout phần nội dung
        content_layout = QVBoxLayout()
        content_layout.addWidget(self.stacked_widget)

        layout.addLayout(content_layout, 4)  # Phần nội dung chiếm phần không gian còn lại

        self.setLayout(layout)

    def switch_content_admin(self, page: str):
        # Chuyển đổi giữa các trang quản lý bên trong Admin
        if page == "GUIQuanLyBaiHat":
            self.stacked_widget.setCurrentIndex(0)
        elif page == "GUIQuanLyCaSi":
            self.stacked_widget.setCurrentIndex(1)
        elif page == "GUIQuanLyDanhSachPhatHeThong":
            self.stacked_widget.setCurrentIndex(2)
        elif page == "GUIQuanLyNguoiDung":
            self.stacked_widget.setCurrentIndex(3)
        elif page == "User":
            # Nếu muốn quay lại trang User (UserContent)
            self.switch_content("User")
        else:
            print("Page not found!")