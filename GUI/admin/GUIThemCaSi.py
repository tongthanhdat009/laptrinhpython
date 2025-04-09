import sys
import os
import shutil
from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFileDialog,
    QHBoxLayout, QDateEdit, QMessageBox, QTextEdit
)
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtCore import Qt, QDate
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from DTO.DTOCaSi import DTOCaSi
from BLL.BLLQuanLy import BLLQuanLy

class GUIThemCaSi(QDialog):
    def __init__(self, parent=None, DSCaSi=None, maCaSi=None):
        super().__init__(parent)
        self.parent = parent
        self.DSCaSi = DSCaSi if DSCaSi else []
        self.duong_dan_anh = ""
        self.bll = BLLQuanLy()
        self.maCaSi = maCaSi
        
        # Khởi tạo hệ thống ảnh
        self.init_image_system()
        self.setWindowTitle("Chỉnh Sửa Ca Sĩ" if maCaSi else "Thêm Ca Sĩ")
        self.setFixedSize(500, 600)
        self.setStyleSheet("background-color: #ffffff; color: #000000;")

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(10, 10, 10, 10)

        # Khởi tạo tất cả thành phần UI trước
        self.setup_ui(main_layout)
        
        # Load existing singer data if in edit mode
        if self.maCaSi:
            self.load_ca_si_data()

    def init_image_system(self):
        """Khởi tạo thư mục ảnh và ảnh mặc định"""
        assets_dir = "assets/CaSi"
        os.makedirs(assets_dir, exist_ok=True)
        
        # Create default image if missing
        default_img = os.path.join(assets_dir, "0.png")
        if not os.path.exists(default_img):
            blank_img = QPixmap(120, 120)
            blank_img.fill(Qt.GlobalColor.white)
            blank_img.save(default_img)
            
    def setup_ui(self, main_layout):
        # Ảnh ca sĩ
        image_layout = QHBoxLayout()
        self.label_anh = QLabel()
        self.label_anh.setFixedSize(120, 120)
        self.label_anh.setStyleSheet("border: 2px solid #000; background-color: #d9d9d9;")
        self.pixmap_anh = QPixmap("assets/CaSi/0.png")  # Ảnh mặc định
        self.label_anh.setPixmap(self.pixmap_anh.scaled(120, 120, Qt.AspectRatioMode.KeepAspectRatio))
        self.btn_chon_anh = QPushButton("Chọn Ảnh")
        self.btn_chon_anh.clicked.connect(self.chon_anh)
        image_layout.addWidget(self.label_anh)
        image_layout.addWidget(self.btn_chon_anh)
        main_layout.addLayout(image_layout)

        # Tên ca sĩ
        label_ten_ca_si = QLabel("Tên Ca Sĩ:")
        label_ten_ca_si.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        self.input_ten_ca_si = QLineEdit()
        self.input_ten_ca_si.setPlaceholderText("Nhập tên ca sĩ")
        self.input_ten_ca_si.setStyleSheet("border: 1px solid #000; padding: 5px;")
        main_layout.addWidget(label_ten_ca_si)
        main_layout.addWidget(self.input_ten_ca_si)

        # Nghệ danh
        label_nghe_danh = QLabel("Nghệ Danh:")
        label_nghe_danh.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        self.input_nghe_danh = QLineEdit()
        self.input_nghe_danh.setPlaceholderText("Nhập nghệ danh (nếu có)")
        self.input_nghe_danh.setStyleSheet("border: 1px solid #000; padding: 5px;")
        main_layout.addWidget(label_nghe_danh)
        main_layout.addWidget(self.input_nghe_danh)

        # Ngày sinh
        label_ngay_sinh = QLabel("Ngày Sinh:")
        label_ngay_sinh.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        self.date_ngay_sinh = QDateEdit()
        self.date_ngay_sinh.setCalendarPopup(True)
        self.date_ngay_sinh.setDate(QDate.currentDate())
        self.date_ngay_sinh.setStyleSheet("border: 1px solid #000; padding: 5px;")
        main_layout.addWidget(label_ngay_sinh)
        main_layout.addWidget(self.date_ngay_sinh)

        # Mô tả
        label_mo_ta = QLabel("Mô Tả:")
        label_mo_ta.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        self.input_mo_ta = QTextEdit()
        self.input_mo_ta.setPlaceholderText("Nhập mô tả về ca sĩ")
        self.input_mo_ta.setStyleSheet("border: 1px solid #000; padding: 5px;")
        main_layout.addWidget(label_mo_ta)
        main_layout.addWidget(self.input_mo_ta)

        # Nút thêm/cập nhật ca sĩ
        self.btn_them = QPushButton("Cập Nhật Ca Sĩ" if self.maCaSi else "Thêm Ca Sĩ")
        self.btn_them.setStyleSheet("background-color: #4CAF50; color: white;")
        self.btn_them.clicked.connect(self.them_ca_si if not self.maCaSi else self.cap_nhat_ca_si)
        main_layout.addWidget(self.btn_them)

        self.setLayout(main_layout)

    def chon_anh(self):
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("Images (*.png *.jpg *.bmp)")
        if file_dialog.exec():
            selected_files = file_dialog.selectedFiles()
            self.duong_dan_anh = selected_files[0]
            self.label_anh.setPixmap(QPixmap(self.duong_dan_anh).scaled(120, 120, Qt.AspectRatioMode.KeepAspectRatio))

    def load_ca_si_data(self):
        """Tải dữ liệu ca sĩ hiện có để chỉnh sửa"""
        ca_si = next((cs for cs in self.DSCaSi if cs.getMaCaSi() == self.maCaSi), None)
        if ca_si:
            self.input_ten_ca_si.setText(ca_si.getTenCaSi())
            self.input_nghe_danh.setText(ca_si.getNgheDanh())
            ngay_sinh = ca_si.getNgaySinh()
            if isinstance(ngay_sinh, str):
                self.date_ngay_sinh.setDate(QDate.fromString(ngay_sinh, "yyyy-MM-dd"))
            elif hasattr(ngay_sinh, 'year') and hasattr(ngay_sinh, 'month') and hasattr(ngay_sinh, 'day'):
                self.date_ngay_sinh.setDate(QDate(ngay_sinh.year, ngay_sinh.month, ngay_sinh.day))
            else:
                self.date_ngay_sinh.setDate(QDate.currentDate())
            self.input_mo_ta.setPlainText(ca_si.getMoTa())
            
            # Tải ảnh ca sĩ
            anh_path = ca_si.getAnhCaSi()
            default_img = "assets/CaSi/0.png"
            
            try:
                if anh_path and os.path.exists(anh_path):
                    pixmap = QPixmap(anh_path)
                    if not pixmap.isNull():
                        self.duong_dan_anh = anh_path
                        self.label_anh.setPixmap(pixmap.scaled(
                            120, 120, Qt.AspectRatioMode.KeepAspectRatio))
                        return  
            except Exception as e:
                print(f"Error loading image: {e}")
                blank_img = QPixmap(120, 120)
                blank_img.fill(Qt.GlobalColor.white)
                self.label_anh.setPixmap(blank_img)

    def them_ca_si(self):
        ten_ca_si = self.input_ten_ca_si.text().strip()
        nghe_danh = self.input_nghe_danh.text().strip()
        ngay_sinh = self.date_ngay_sinh.date().toString("yyyy-MM-dd")
        mo_ta = self.input_mo_ta.toPlainText().strip()
        anh_ca_si = self.duong_dan_anh

        # Kiểm tra các trường bắt buộc
        if not ten_ca_si:
            self.show_info_message("Lỗi", "Vui lòng nhập tên ca sĩ")
            return
        if not anh_ca_si:
            self.show_info_message("Lỗi", "Vui lòng chọn ảnh ca sĩ")
            return

        # Tạo ID mới cho ca sĩ
        ma_ca_si = len(self.bll.layDanhSachCaSi()) + 1

        # Tạo thư mục assets nếu chưa tồn tại
        assets_dir = "assets/CaSi"
        os.makedirs(assets_dir, exist_ok=True)

        # Sao chép ảnh vào thư mục assets
        duong_dan_moi_anh = f"assets/CaSi/{ma_ca_si}.png"
        try:
            if os.path.exists(anh_ca_si):
                shutil.copy(anh_ca_si, duong_dan_moi_anh)
        except Exception as e:
            self.show_info_message("Lỗi", f"Lỗi sao chép ảnh: {str(e)}")
            return

        # Tạo đối tượng DTOCaSi
        ca_si = DTOCaSi(
            maCaSi=ma_ca_si,
            tenCaSi=ten_ca_si,
            anhCaSi=duong_dan_moi_anh,
            ngheDanh=nghe_danh,
            ngaySinh=ngay_sinh,
            moTa=mo_ta
        )

        # Thêm vào cơ sở dữ liệu
        result = self.bll.themCaSi(ca_si)
        if result == "Thành công":
            self.show_info_message("Thông báo", "Thêm ca sĩ thành công!")
            if self.parent:
                self.parent.layDSCaSi()  # Refresh parent window if exists
            self.close()
        else:
            self.show_info_message("Lỗi", result)

    def cap_nhat_ca_si(self):
        ten_ca_si = self.input_ten_ca_si.text().strip()
        nghe_danh = self.input_nghe_danh.text().strip()
        ngay_sinh = self.date_ngay_sinh.date().toString("yyyy-MM-dd")
        mo_ta = self.input_mo_ta.toPlainText().strip()
        anh_ca_si = self.duong_dan_anh

        # Kiểm tra các trường bắt buộc
        if not ten_ca_si:
            self.show_info_message("Lỗi", "Vui lòng nhập tên ca sĩ")
            return
        if not anh_ca_si:
            self.show_info_message("Lỗi", "Vui lòng chọn ảnh ca sĩ")
            return

        # Sao chép ảnh mới nếu có thay đổi
        duong_dan_moi_anh = f"assets/CaSi/{self.maCaSi}.png"
        if anh_ca_si != duong_dan_moi_anh:
            try:
                if os.path.exists(anh_ca_si):
                    shutil.copy(anh_ca_si, duong_dan_moi_anh)
            except Exception as e:
                self.show_info_message("Lỗi", f"Lỗi sao chép ảnh: {str(e)}")
                return

        # Tạo đối tượng DTOCaSi
        ca_si = DTOCaSi(
            maCaSi=self.maCaSi,
            tenCaSi=ten_ca_si,
            anhCaSi=duong_dan_moi_anh,
            ngheDanh=nghe_danh,
            ngaySinh=ngay_sinh,
            moTa=mo_ta
        )

        # Cập nhật vào cơ sở dữ liệu
        result = self.bll.capNhatCaSi(ca_si)
        if result == "Thành công":
            self.show_info_message("Thông báo", "Cập nhật ca sĩ thành công!")
            if self.parent:
                self.parent.layDSCaSi()  # Refresh parent window if exists
            self.close()
        else:
            self.show_info_message("Lỗi", result)

    def show_info_message(self, title, message):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec()
