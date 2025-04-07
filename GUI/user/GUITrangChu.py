from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout
from PyQt6.QtCore import Qt

class GUITrangChu(QWidget):
    def __init__(self):
        super().__init__()

        # Đặt kích thước cửa sổ
        self.setFixedSize(1200, 580)
        # Tạo layout dọc (Vertical Layout)
        layout = QVBoxLayout()

        # Tạo một label cho trang chủ
        title_label = QLabel("Chào mừng đến với Trang Chủ")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("font-size: 30px; font-weight: bold; color: #000; padding: 20px;")
        
        # Thêm label vào layout
        layout.addWidget(title_label)

        # Cài đặt layout cho QWidget
        self.setLayout(layout)
