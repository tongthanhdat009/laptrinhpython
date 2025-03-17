from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPalette, QColor

class MusicPlayerBar(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1500, 100)
        self.setStyleSheet("background-color: white;")


