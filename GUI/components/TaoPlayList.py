import os
from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QHBoxLayout, QSpacerItem, QSizePolicy, QFileDialog
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap
import shutil

class TaoPlayList(QDialog):
    def __init__(self, bllphatnhac, idnguoidung, cap_nhat_danh_sach):
        super().__init__()
        self.cap_nhat_danh_sach = cap_nhat_danh_sach
        self.image_path = "assets/DanhSachPhat/0.png"
        self.bllphatnhac = bllphatnhac
        self.idnguoidung = idnguoidung
        self.setFixedSize(300, 320)  # Kích thước cửa sổ đủ lớn để chứa ảnh bìa
        self.setWindowTitle("Tạo danh sách phát")
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground)

        self.setStyleSheet("""
            QDialog {
                background-color: #ffffff;
                color: black;
            }
            QLabel#titleLabel {
                font-size: 18px;
                font-weight: bold;
                qproperty-alignment: AlignCenter;
                color: black;
            }
            QLineEdit {
                padding: 6px;
                font-size: 14px;
                border: 1px solid #ccc;
                border-radius: 5px;
                background-color: white;
                color: black;
            }
            QPushButton {
                padding: 6px;
                font-size: 14px;
                border: none;
                border-radius: 5px;
            }
            QPushButton#btnClose {
                background-color: transparent;
                font-weight: bold;
                font-size: 16px;
                color: black;
                padding: 2px 6px 0px 6px;
            }
            QPushButton#btnClose:hover {
                background-color: #e0e0e0;
            }
            QPushButton#btnCreate {
                background-color: #0078d7;
                color: white;
            }
            QPushButton#btnCreate:hover {
                background-color: #005ea6;
            }
            QPushButton#btnChooseImage {
                background-color: #f0f0f0;
                color: black;
            }
            QPushButton#btnChooseImage:hover {
                background-color: #e0e0e0;
            }
        """)

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(10, 10, 10, 10)
        main_layout.setSpacing(10)

        # Header: Nút X ở góc phải
        header_layout = QHBoxLayout()
        header_layout.setContentsMargins(0, 0, 0, 0)
        header_layout.setSpacing(0)

        spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        header_layout.addItem(spacer)

        btn_close = QPushButton("✖")
        btn_close.setObjectName("btnClose")
        btn_close.clicked.connect(self.close)
        header_layout.addWidget(btn_close)

        main_layout.addLayout(header_layout)

        # Tiêu đề "Tạo danh sách phát"
        title = QLabel("Tạo danh sách phát")
        title.setObjectName("titleLabel")
        main_layout.addWidget(title)

        # Ô nhập tên danh sách phát
        self.input_ten = QLineEdit()
        self.input_ten.setPlaceholderText("Nhập tên danh sách phát...")
        main_layout.addWidget(self.input_ten)

        # Nút chọn ảnh bìa
        self.btn_choose_image = QPushButton("Chọn ảnh bìa")
        self.btn_choose_image.setObjectName("btnChooseImage")
        self.btn_choose_image.clicked.connect(self.choose_image)
        main_layout.addWidget(self.btn_choose_image)

        # Label hiển thị ảnh bìa
        self.image_label = QLabel()
        self.image_label.setFixedSize(120, 120)  # Tăng kích thước hiển thị ảnh lên 120x120
        self.load_default_image()  # Tải và hiển thị ảnh mặc định ngay từ đầu
        main_layout.addWidget(self.image_label)

        # Nút tạo mới nằm ở cuối cùng
        self.btn_tao_moi = QPushButton("Tạo mới")
        self.btn_tao_moi.setObjectName("btnCreate")
        self.btn_tao_moi.clicked.connect(self.create_playlist)
        main_layout.addWidget(self.btn_tao_moi)

        self.setLayout(main_layout)

    def load_default_image(self):
        pixmap = QPixmap(self.image_path)
        if pixmap.isNull():
            # Nếu không thể tải ảnh mặc định, tạo một pixmap màu trắng
            pixmap = QPixmap(120, 120)
            pixmap.fill(Qt.GlobalColor.white)
        # Scale ảnh để nó vừa với QLabel mà không cắt bớt nội dung
        self.image_label.setPixmap(pixmap.scaled(120, 120, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))

    def choose_image(self):
        """Chọn ảnh từ file và cập nhật ảnh bìa hiển thị"""
        file_dialog = QFileDialog(self, "Chọn ảnh bìa")
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFiles)
        file_dialog.setNameFilter("Images (*.png *.jpg *.bmp *.jpeg)")
        if file_dialog.exec():
            selected_files = file_dialog.selectedFiles()
            if selected_files:
                self.image_path = selected_files[0]
                pixmap = QPixmap(self.image_path)
                if not pixmap.isNull():
                    self.image_label.setPixmap(pixmap.scaled(120, 120, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation))

    def create_playlist(self):
        ma = self.bllphatnhac.layMaDanhSachPhat()
        tieu_de = self.input_ten.text()
        target_path = os.path.join("assets", "DanhSachPhat", f"{ma}.png").replace("\\", "/")

        if self.image_path != "assets/DanhSachPhat/0.png":
            try:
                shutil.copy(self.image_path, target_path)
                print(f"Đã sao chép ảnh tới {target_path}")
            except Exception as e:
                print("Lỗi khi sao chép ảnh:", e)
            self.image_path = target_path
        else:
            self.image_path = "assets/DanhSachPhat/0.png"

        self.bllphatnhac.taoDanhSachPhat(tieu_de, "", self.idnguoidung, self.image_path)
        self.cap_nhat_danh_sach()
        self.accept()

