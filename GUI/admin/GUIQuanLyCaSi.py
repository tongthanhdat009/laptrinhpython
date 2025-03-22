import sys
import os
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QPushButton, QFrame
from admin.GUIThemBaiHat import GUIThemBaiHat
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
# from BLL.BLLQuanLy import BLLQuanLy

class GUIQuanLyCaSi(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1250, 650)
        self.placeHolder = QLabel("Quản lý ca sĩ", self)