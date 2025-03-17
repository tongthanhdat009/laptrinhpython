from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPalette, QColor

class UserContent(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1250, 650)

        # Đảm bảo màu nền được áp dụng đúng
        self.setAutoFillBackground(True)
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor("#FFFFFF"))
        self.setPalette(palette)


        
