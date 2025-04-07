# GUILichSuNghe.py
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt

class GUILichSuNghe(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1200, 580)

        layout = QVBoxLayout()

        title_label = QLabel("Chào mừng đến với Lịch Sử Nghe Nhạc")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("font-size: 30px; font-weight: bold; color: #000; padding: 20px;")
        layout.addWidget(title_label)

        self.setLayout(layout)
