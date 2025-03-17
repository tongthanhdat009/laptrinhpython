from PyQt6.QtWidgets import QWidget, QVBoxLayout, QListWidget
from PyQt6.QtCore import Qt

class UserMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(250, 650)
        self.setStyleSheet("background-color: #f2f2f2;")

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)  # Xóa margin
        layout.setSpacing(0)  # Xóa khoảng cách giữa các widget

        # Danh sách menu nhưng ẩn chữ
        menu_list = QListWidget()
        menu_list.setStyleSheet("border: none; padding: 0px; color: transparent;")  # Ẩn chữ nhưng giữ màu nền

        layout.addWidget(menu_list)
        self.setLayout(layout)
