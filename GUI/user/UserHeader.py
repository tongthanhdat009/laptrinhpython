import sys
import os
from PyQt6.QtWidgets import QWidget, QLabel, QHBoxLayout, QLineEdit, QPushButton
from PyQt6.QtCore import Qt, QSize, pyqtSignal
from PyQt6.QtGui import QPixmap, QIcon

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from DTO.DTONguoiDung import DTONguoiDung

class UserHeader(QWidget):
    search_signal = pyqtSignal(str)
    
    def __init__(self, user: DTONguoiDung, callback_search, switch_callback):
        super().__init__()
        self.setFixedHeight(70)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground)
        self.setStyleSheet("""
            background-color: #ffffff;
            border: none;
            margin: 0;
        """)
        self.search_text = ""
        
        layout = QHBoxLayout(self)

        self.search_bar = QLineEdit(self)
        self.search_bar.setPlaceholderText("🔍 Tìm kiếm...")
        self.search_bar.setStyleSheet("""
            QLineEdit {
                padding: 10px;
                font-size: 14px;
                background-color: #f0f0f0;
                border: 1px solid #ccc;
                border-radius: 10px;
                color: #333;
                margin-left: 100px;
            }
            QLineEdit:focus {
                border: 2px solid #1db954;
                background-color: white;
            }
        """)
        self.search_bar.setFixedWidth(600)

        layout.addWidget(self.search_bar)

        user_layout = QHBoxLayout()

        if user.ma_quyen == "admin":
            admin_button = QPushButton(self)
            admin_button.setObjectName("adminButton")
            admin_button.setIcon(QIcon("assets/icon/admin.png"))
            admin_button.setIconSize(QSize(40, 40))
            admin_button.setFixedSize(60, 60)
            admin_button.setStyleSheet("""
                QPushButton#adminButton {
                    background-color: transparent;
                    border: 2px solid #ddd;
                    border-radius: 30px;
                    padding: 0;
                }
                QPushButton#adminButton:hover {
                    background-color: #f0f0f0;
                    border-color: #bbb;
                }
            """)
            admin_button.setToolTip("Quản trị viên")
            admin_button.clicked.connect(lambda: switch_callback("Admin"))
            user_layout.addWidget(admin_button)

        avatar_label = QLabel(self)
        avatar_label.setFixedSize(60, 60)
        avatar_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        avatar_label.setStyleSheet("""
            border-radius: 30px;
            border: 2px solid #ddd;
            background-color: #ffffff;
        """)

        pixmap = QPixmap(user.anh)
        if not pixmap.isNull():
            pixmap = pixmap.scaled(55, 55, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            avatar_label.setPixmap(pixmap)

        user_layout.addWidget(avatar_label)

        name_label = QLabel(user.ten_nguoi_dung, self)
        name_label.setStyleSheet("""
            font-size: 14px;
            font-weight: bold;
            color: black;
            margin-left: 10px;
        """)
        user_layout.addWidget(name_label)

        user_layout.addStretch()
        user_layout.setContentsMargins(0, 0, 20, 0)

        layout.addStretch()
        layout.addLayout(user_layout)

        self.search_bar.returnPressed.connect(lambda: callback_search(self.search_bar.text().strip()))
        self.setLayout(layout)