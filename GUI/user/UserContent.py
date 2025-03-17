from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout

class UserContent(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1250, 650)
        self.setStyleSheet("background-color: #ffffff;")
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        label = QLabel("content")
        layout.addWidget(label)
        self.setLayout(layout)
        
