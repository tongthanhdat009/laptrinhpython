from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QStackedWidget, QLabel
from user.UserMenu import UserMenu
from user.UserHeader import UserHeader
from DTO.DTONguoiDung import DTONguoiDung
from .GUITrangChu import GUITrangChu  
from .GUIBXHBaiHat import GUIBXHBaiHat
from .GUILichSuNghe import GUILichSuNghe
from .GUIBaiHatYeuThich import GUIBaiHatYeuThich
from .GUIDanhSachPhat import GUIDanhSachPhat
from .GUITimKiem import GUITimKiem
class UserContent(QWidget):
    def __init__(self, user: DTONguoiDung, switch_content):
        super().__init__()
        self.setFixedSize(1500, 650)
        self.setStyleSheet("background-color: #ffffff; margin: 0; padding: 0;")  
        layout = QHBoxLayout()  
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0) 

        self.menu = UserMenu(self.switch_content_user)
        layout.addWidget(self.menu, 1)

        content_layout = QVBoxLayout()
        content_layout.setContentsMargins(0, 0, 0, 0)
        content_layout.setSpacing(0) 

        self.header = UserHeader(user,self.switch_content_search ,switch_content)  
        content_layout.addWidget(self.header) 

        self.stacked_widget = QStackedWidget()
        

        self.gui_trangchu = GUITrangChu() 
        self.stacked_widget.addWidget(self.gui_trangchu)

        self.gui_bxh_baihat = GUIBXHBaiHat()  
        self.stacked_widget.addWidget(self.gui_bxh_baihat)

        self.gui_lichsu_nghe = GUILichSuNghe()  
        self.stacked_widget.addWidget(self.gui_lichsu_nghe)

        self.gui_baihat_yeuthich = GUIBaiHatYeuThich()  
        self.stacked_widget.addWidget(self.gui_baihat_yeuthich)

        self.gui_danhsach_phat = GUIDanhSachPhat()  
        self.stacked_widget.addWidget(self.gui_danhsach_phat)
        
        self.gui_timkiem = GUITimKiem()  
        self.stacked_widget.addWidget(self.gui_timkiem)


        content_layout.addWidget(self.stacked_widget)

        layout.addLayout(content_layout, 4)   

        self.setLayout(layout)

        self.switch_content = switch_content  

    def switch_content_search(self, search_text):
        # Xóa widget tìm kiếm cũ nếu có
        old_widget = self.stacked_widget.widget(5)  # Vị trí 5 là widget tìm kiếm
        if old_widget:
            self.stacked_widget.removeWidget(old_widget)
        
        # Tạo widget tìm kiếm mới và thêm vào stack
        self.gui_timkiem = GUITimKiem(search_text)
        self.stacked_widget.insertWidget(5, self.gui_timkiem)
        self.stacked_widget.setCurrentWidget(self.gui_timkiem)

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
