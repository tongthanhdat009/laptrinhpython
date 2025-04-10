from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QStackedWidget, QLabel
from user.UserMenu import UserMenu
from user.UserHeader import UserHeader
from DTO.DTONguoiDung import DTONguoiDung
from .GUITrangChu import GUITrangChu  # Import các trang giao diện
from .GUIBXHBaiHat import GUIBXHBaiHat
from .GUILichSuNghe import GUILichSuNghe
from .GUIBaiHatYeuThich import GUIBaiHatYeuThich
from .GUIDanhSachPhat import GUIDanhSachPhat

class UserContent(QWidget):
    def __init__(self, user: DTONguoiDung, switch_content):
        super().__init__()
        self.setFixedSize(1500, 650)
        self.setStyleSheet("background-color: #ffffff; margin: 0; padding: 0;")  # Đặt màu nền trắng và không có margin, padding

        layout = QHBoxLayout()  # Sử dụng QHBoxLayout để chia màn hình thành 2 phần
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)  # Đặt khoảng cách giữa các phần tử là 0

        # Truyền callback switch_content_user vào UserMenu
        self.menu = UserMenu(self.switch_content_user)
        layout.addWidget(self.menu, 1)  # Phần menu chiếm 1 phần không gian

        content_layout = QVBoxLayout()
        content_layout.setContentsMargins(0, 0, 0, 0)
        content_layout.setSpacing(0)  # Đặt khoảng cách giữa các phần tử là 0

        # Truyền callback switch_content vào UserHeader để xử lý việc chuyển trang
        header = UserHeader(user, switch_content)  
        content_layout.addWidget(header)  # Thêm header vào layout

        # Tạo QStackedWidget để chứa các trang
        self.stacked_widget = QStackedWidget()
        
        # Tạo các trang và thêm vào stacked_widget
        self.gui_trangchu = GUITrangChu()  # Giả sử bạn đã có class GUITrangChu
        self.stacked_widget.addWidget(self.gui_trangchu)

        self.gui_bxh_baihat = GUIBXHBaiHat()  
        self.stacked_widget.addWidget(self.gui_bxh_baihat)

        self.gui_lichsu_nghe = GUILichSuNghe()  
        self.stacked_widget.addWidget(self.gui_lichsu_nghe)

        self.gui_baihat_yeuthich = GUIBaiHatYeuThich()  
        self.stacked_widget.addWidget(self.gui_baihat_yeuthich)

        self.gui_danhsach_phat = GUIDanhSachPhat()  
        self.stacked_widget.addWidget(self.gui_danhsach_phat)

        # Thêm stacked_widget vào layout
        content_layout.addWidget(self.stacked_widget)

        layout.addLayout(content_layout, 4)  # Phần nội dung chiếm phần không gian còn lại

        self.setLayout(layout)

        self.switch_content = switch_content  # Lưu callback để gọi khi chuyển đổi nội dung

    def switch_content_user(self, page):
        # Chuyển sang trang tương ứng trong stacked_widget
        if page == "GUITrangChu":
            self.stacked_widget.setCurrentWidget(self.gui_trangchu)
        elif page == "GUIBXHBaiHat":
            self.stacked_widget.setCurrentWidget(self.gui_bxh_baihat)
        elif page == "GUILichSuNghe":
            self.stacked_widget.setCurrentWidget(self.gui_lichsu_nghe)
        elif page == "GUIBaiHatYeuThich":
            self.stacked_widget.setCurrentWidget(self.gui_baihat_yeuthich)
        elif page == "GUIDanhSachPhat":
            self.stacked_widget.setCurrentWidget(self.gui_danhsach_phat)
        else:
            # Nếu không tìm thấy trang phù hợp, chuyển về một trang mặc định hoặc hiển thị thông báo
            self.stacked_widget.setCurrentWidget(self.gui_trangchu)
