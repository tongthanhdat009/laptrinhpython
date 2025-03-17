from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel

class MusicPlayerBar(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1500, 100)

        # Thêm viền trên màu xám
        self.setStyleSheet("""
            background-color: #ffffff;
            border-top: 1px solid #f2f2f2;
        """)

        layout = QVBoxLayout()
        layout.addWidget(QLabel("play"))
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)
