from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout
from user.UserMenu import UserMenu
from user.UserContent import UserContent
from user.MusicPlayerBar import MusicPlayerBar
from admin.AdminMenu import AdminMenu
from admin.GUIQuanLyBaiHat import GUIQuanLyBaiHat
from admin.GUIQuanLyDanhSachPhatHeThong import GUIQuanLyDanhSachPhatHeThong
from admin.GUIQuanLyCaSi import GUIQuanLyCaSi
from admin.GUIQuanLyNguoiDung import GUIQuanLyNguoiDung
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
        self.menu = AdminMenu(self.switch_content)
        center_layout.addWidget(self.menu)
        
        # Nội dung bên phải
        self.content = UserContent()
        self.content = GUIQuanLyBaiHat()
        
        center_layout.addWidget(self.content)
        
        player_widget = MusicPlayerBar()

        main_layout.addLayout(center_layout)
        main_layout.addWidget(player_widget)
        
        self.setLayout(main_layout)

    def switch_content(self, page):
        pages = {
            "GUIQuanLyBaiHat": GUIQuanLyBaiHat,
            "GUIQuanLyCaSi": GUIQuanLyCaSi,
            "GUIQuanLyDanhSachPhatHeThong": GUIQuanLyDanhSachPhatHeThong,
            "GUIQuanLyNguoiDung": GUIQuanLyNguoiDung,
        }

        new_content = pages.get(page, None)  # Lấy class từ dictionary, nếu không có thì None

        if new_content:  # Chỉ thay thế nếu tìm thấy trang hợp lệ
            new_content = new_content()
            self.layout().replaceWidget(self.content, new_content)
            self.content.deleteLater()
            self.content = new_content


# Chạy ứng dụng
if __name__ == "__main__":
    app = QApplication([])
    window = MainLayout()
    window.show()
    app.exec()