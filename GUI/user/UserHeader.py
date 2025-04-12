import sys
import os
from PyQt6.QtWidgets import QWidget, QLabel, QHBoxLayout, QLineEdit, QPushButton
from PyQt6.QtCore import Qt, QSize, pyqtSignal
from PyQt6.QtGui import QPixmap, QIcon

# Thêm dòng này để sửa lỗi không tìm thấy DTO
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))
from DTO.DTONguoiDung import DTONguoiDung  # Import từ DTO
from GUI.user.GUITimKiem import GUITimKiem  # Import GUITimKiem
class UserHeader(QWidget):
    search_signal = pyqtSignal(str)  # Tạo tín hiệu để truyền chuỗi tìm kiếm
    
    def __init__(self, user: DTONguoiDung, switch_callback):
        super().__init__()
        self.setFixedHeight(70)  # Đặt chiều cao header là 70px
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground)  # Buộc sử dụng màu nền từ stylesheet
        self.setStyleSheet("""
            background-color: #ffffff;  /* Explicitly set white background */
            border: none;  /* No border */
            margin: 0;  /* Đặt margin-bottom cho header */
        """)
        self.search_text = ""  # Lưu biến tìm kiếm để sử dụng sau này
        
        layout = QHBoxLayout(self)  # Đặt layout trực tiếp vào widget chính

        # Thanh tìm kiếm với icon trong placeholder
        self.search_bar = QLineEdit(self)
        self.search_bar.setPlaceholderText("🔍 Tìm kiếm...")  # Sử dụng biểu tượng Unicode cho icon tìm kiếm
        self.search_bar.setStyleSheet("""
            QLineEdit {
                padding: 10px;
                font-size: 14px;
                background-color: #f0f0f0;
                border: 1px solid #ccc;
                border-radius: 10px;
                color: #333;  /* Màu chữ trong thanh tìm kiếm */
                margin-left: 100px;  /* Thêm khoảng cách bên trái */
            }
            QLineEdit:focus {
                border: 2px solid #1db954;  /* Viền xanh lá khi focus */
                background-color: white;  /* Nền trắng khi focus */
            }
        """)
        self.search_bar.setFixedWidth(600)  # Đặt chiều rộng cho thanh tìm kiếm dài hơn
        
        # Kết nối sự kiện returnPressed (nhấn Enter) với hàm xử lý tìm kiếm
        self.search_bar.returnPressed.connect(self.handle_search)
        
        # Thêm thanh tìm kiếm vào layout
        layout.addWidget(self.search_bar)  # Thêm thanh tìm kiếm trực tiếp vào layout chính

        # Layout con chứa admin button, avatar, và tên người dùng
        user_layout = QHBoxLayout()

        # Kiểm tra quyền nếu là admin, hiển thị nút admin
        if user.ma_quyen == "admin":  # Giả sử 'ma_quyen' là mã quyền người dùng
            admin_button = QPushButton(self)
            admin_button.setObjectName("adminButton")  # Đặt object name để áp dụng CSS
            admin_button.setIcon(QIcon("assets/icon/admin.png"))  # Thay "path_to_admin_icon.png" bằng đường dẫn đến icon admin
            admin_button.setIconSize(QSize(40, 40))  # Đặt kích thước icon nhỏ hơn nút
            admin_button.setFixedSize(60, 60)  # Đặt kích thước nút là hình vuông (60x60)
            admin_button.setStyleSheet("""
                QPushButton#adminButton {
                    background-color: transparent;
                    border: 2px solid #ddd;  /* Viền xám nhạt */
                    border-radius: 30px;  /* Nút hình tròn (bằng 1/2 kích thước nút) */
                    padding: 0;
                }
                QPushButton#adminButton:hover {
                    background-color: #f0f0f0;  /* Hiệu ứng hover */
                    border-color: #bbb;  /* Đổi màu viền khi hover */
                }
            """)
            admin_button.setToolTip("Quản trị viên")  # Tooltip cho nút admin
            admin_button.clicked.connect(lambda: switch_callback("Admin"))  # Kết nối callback_admin với sự kiện click
            user_layout.addWidget(admin_button)  # Thêm nút admin vào layout

        # Ảnh đại diện ở góc phải
        avatar_label = QLabel(self)
        avatar_label.setFixedSize(60, 60)  # Đặt kích thước của avatar thành hình vuông 60x60
        avatar_label.setAlignment(Qt.AlignmentFlag.AlignCenter)  # Căn giữa ảnh trong QLabel
        avatar_label.setStyleSheet("""
            border-radius: 30px;  /* Avatar hình tròn */
            border: 2px solid #ddd;  /* Viền xám nhạt */
            background-color: #ffffff;  /* Đảm bảo nền trắng */
        """)

        pixmap = QPixmap(user.anh)  # Assuming 'anh' is the path to the avatar image
        if not pixmap.isNull():
            # Chỉnh lại kích thước ảnh cho vừa với khuôn hình tròn
            pixmap = pixmap.scaled(55, 55, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
            avatar_label.setPixmap(pixmap)

        user_layout.addWidget(avatar_label)

        # Thêm tên người dùng bên phải avatar và đặt màu đen
        name_label = QLabel(user.ten_nguoi_dung, self)
        name_label.setStyleSheet("""
            font-size: 14px;
            font-weight: bold;
            color: black;  /* Đặt màu chữ tên người dùng thành đen */
            margin-left: 10px;  /* Thêm khoảng cách giữa tên và ảnh đại diện */
        """)

        user_layout.addWidget(name_label)  # Thêm tên người dùng vào layout

        # Dồn layout con này về bên phải và tạo khoảng cách margin-right 20px
        user_layout.addStretch()
        user_layout.setContentsMargins(0, 0, 20, 0)  # Thêm khoảng cách bên phải 20px

        layout.addStretch()  # Đẩy toàn bộ vùng tìm kiếm sang bên trái
        layout.addLayout(user_layout)  # Thêm layout con vào layout chính

        self.setLayout(layout)  # Đặt layout cho toàn bộ widget

    def handle_search(self):
        """Xử lý khi người dùng nhấn Enter trong thanh tìm kiếm"""
        self.search_text = self.search_bar.text().strip()  # Lấy văn bản từ thanh tìm kiếm
    
