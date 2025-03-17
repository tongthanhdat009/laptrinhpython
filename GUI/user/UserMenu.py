from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel

class UserMenu(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(250, 650)
        self.setStyleSheet("background-color: #f2f2f2;")

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        # Thêm một chữ "Menu" vào UserMenu
        label = QLabel("Menu")
        layout.addWidget(label)

        self.setLayout(layout)
