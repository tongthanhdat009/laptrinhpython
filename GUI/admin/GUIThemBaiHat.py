import sys
import os
from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QLabel, QLineEdit, QComboBox, QPushButton, QFileDialog, 
    QHBoxLayout, QWidget, QScrollArea, QCompleter, QDateEdit, QMessageBox
)
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtCore import Qt, QDate
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from DTO.DTOBaiHat import DTOBaiHat
from BLL.BLLQuanLy import BLLQuanLy
class GUIThemBaiHat(QDialog):
    def __init__(self):
        super().__init__()
        self.duong_dan_anh = ""
        self.bll = BLLQuanLy()
        self.setWindowTitle("Thêm Bài Hát")
        self.setFixedSize(600, 750)
        self.setStyleSheet("background-color: #ffffff; color: #000000;")

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(10, 10, 10, 10)

        # Ảnh bìa
        image_layout = QHBoxLayout()
        self.label_anh = QLabel()
        self.label_anh.setFixedSize(120, 120)
        self.label_anh.setStyleSheet("border: 2px solid #000; background-color: #d9d9d9;")
        self.pixmap_anh = QPixmap("assets/AnhBaiHat/0.png")  # Ảnh mặc định
        self.label_anh.setPixmap(self.pixmap_anh.scaled(120, 120, Qt.AspectRatioMode.KeepAspectRatio))
        self.btn_chon_anh = QPushButton("Chọn Ảnh")
        self.btn_chon_anh.clicked.connect(self.chon_anh)
        image_layout.addWidget(self.label_anh)
        image_layout.addWidget(self.btn_chon_anh)
        main_layout.addLayout(image_layout)

        # Tên bài hát
        label_ten_bai_hat = QLabel("Tên Bài Hát:")
        label_ten_bai_hat.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        self.input_ten_bai_hat = QLineEdit()
        self.input_ten_bai_hat.setPlaceholderText("Nhập tên bài hát")
        self.input_ten_bai_hat.setStyleSheet("border: 1px solid #000; padding: 5px;")
        main_layout.addWidget(label_ten_bai_hat)
        main_layout.addWidget(self.input_ten_bai_hat)

        # Ngày phát hành
        label_ngay_phat_hanh = QLabel("Ngày Phát Hành:")
        label_ngay_phat_hanh.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        self.date_ngay_phat_hanh = QDateEdit()
        self.date_ngay_phat_hanh.setCalendarPopup(True)
        self.date_ngay_phat_hanh.setDate(QDate.currentDate())
        self.date_ngay_phat_hanh.setStyleSheet("border: 1px solid #000; padding: 5px;")
        main_layout.addWidget(label_ngay_phat_hanh)
        main_layout.addWidget(self.date_ngay_phat_hanh)

        # Xuất xứ
        label_xuat_xu = QLabel("Xuất Xứ:")
        label_xuat_xu.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        self.combo_xuat_xu = QComboBox()
        self.combo_xuat_xu.addItems(self.bll.layTenXuatXu())
        self.combo_xuat_xu.setStyleSheet("border: 1px solid #000; padding: 5px;")
        main_layout.addWidget(label_xuat_xu)
        main_layout.addWidget(self.combo_xuat_xu)

        # Thể loại
        label_the_loai = QLabel("Thể Loại:")
        label_the_loai.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        self.combo_the_loai = QComboBox()
        self.combo_the_loai.addItems(self.bll.layTenTheLoai())
        self.combo_the_loai.setStyleSheet("border: 1px solid #000; padding: 5px;")
        main_layout.addWidget(label_the_loai)
        main_layout.addWidget(self.combo_the_loai)

        # File nhạc
        label_file_nhac = QLabel("File Nhạc:")
        label_file_nhac.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        file_layout = QHBoxLayout()
        self.input_file_nhac = QLineEdit()
        self.input_file_nhac.setPlaceholderText("Chọn file nhạc")
        self.input_file_nhac.setStyleSheet("border: 1px solid #000; padding: 5px;")
        self.btn_chon_file_nhac = QPushButton("Chọn File")
        self.btn_chon_file_nhac.clicked.connect(self.chon_file_nhac)
        file_layout.addWidget(self.input_file_nhac)
        file_layout.addWidget(self.btn_chon_file_nhac)
        main_layout.addWidget(label_file_nhac)
        main_layout.addLayout(file_layout)

        # Ca sĩ
        label_ca_si = QLabel("Ca Sĩ:")
        label_ca_si.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        main_layout.addWidget(label_ca_si)
        
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.ca_si_container = QWidget()
        self.ca_si_layout = QVBoxLayout(self.ca_si_container)
        self.scroll_area.setWidget(self.ca_si_container)
        main_layout.addWidget(self.scroll_area)
        
        self.btn_them_ca_si = QPushButton("+ Thêm Ca Sĩ")
        self.btn_them_ca_si.clicked.connect(self.them_ca_si)
        main_layout.addWidget(self.btn_them_ca_si)

        # Nút thêm bài hát
        self.btn_them = QPushButton("Thêm Bài Hát")
        self.btn_them.setStyleSheet("background-color: #4CAF50; color: white;")
        self.btn_them.clicked.connect(self.them_bai_hat)
        main_layout.addWidget(self.btn_them)

        self.setLayout(main_layout)

    def chon_anh(self):
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("Images (*.png *.jpg *.bmp)")
        if file_dialog.exec():
            selected_files = file_dialog.selectedFiles()
            self.duong_dan_anh = selected_files[0]  # Lưu đường dẫn ảnh
            self.label_anh.setPixmap(QPixmap(self.duong_dan_anh).scaled(120, 120, Qt.AspectRatioMode.KeepAspectRatio))


    def chon_file_nhac(self):
        file_dialog = QFileDialog(self)
        file_dialog.setNameFilter("Audio Files (*.mp3 *.wav *.flac)")
        if file_dialog.exec():
            selected_files = file_dialog.selectedFiles()
            self.input_file_nhac.setText(selected_files[0])

    def them_ca_si(self):
        ca_si_layout = QHBoxLayout()

        input_ca_si = QComboBox()
        input_ca_si.setEditable(True)

        # Danh sách ca sĩ có sẵn
        ca_si_list = self.bll.layToanBoTenCaSi()
        input_ca_si.addItems(ca_si_list)

        # Sử dụng QCompleter để gợi ý
        completer = QCompleter(ca_si_list)
        completer.setCompletionMode(QCompleter.CompletionMode.PopupCompletion)
        completer.setFilterMode(Qt.MatchFlag.MatchContains)
        completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        input_ca_si.setCompleter(completer)

        # Kiểm tra khi rời khỏi ô nhập
        class CustomComboBox(QComboBox):
            def focusOutEvent(self, event):
                super().focusOutEvent(event)
                text = self.currentText()
                if text not in ca_si_list:
                    self.setCurrentText("")  # Xóa nội dung nếu không hợp lệ

        input_ca_si = CustomComboBox()
        input_ca_si.setEditable(True)
        input_ca_si.addItems(ca_si_list)
        input_ca_si.setCompleter(completer)

        input_ca_si.setStyleSheet("border: 1px solid #000; padding: 5px;")

        btn_xoa = QPushButton("X")
        btn_xoa.setFixedSize(30, 25)

        ca_si_layout.addWidget(input_ca_si)
        ca_si_layout.addWidget(btn_xoa)

        container = QWidget()
        container.setLayout(ca_si_layout)
        self.ca_si_layout.addWidget(container)

        btn_xoa.clicked.connect(lambda: self.xoa_ca_si(container))



    def xoa_ca_si(self, container):
        self.ca_si_layout.removeWidget(container)
        container.deleteLater()
    
    def them_bai_hat(self):
        ten_bai_hat = self.input_ten_bai_hat.text()
        ngay_phat_hanh = self.date_ngay_phat_hanh.date().toString("yyyy-MM-dd")  # Lấy ngày phát hành
        xuat_xu = self.combo_xuat_xu.currentText()
        the_loai = self.combo_the_loai.currentText()
        file_nhac = self.input_file_nhac.text()
        anh_bia = self.duong_dan_anh
        
        # Lấy danh sách ca sĩ từ các ComboBox
        ca_si = []
        for i in range(self.ca_si_layout.count()):
            widget = self.ca_si_layout.itemAt(i).widget()
            if widget:
                combo_box = widget.layout().itemAt(0).widget()
                ca_si.append(combo_box.currentText())

        # Cần truyền mã xuất xứ và thể loại (có thể dùng chỉ mục của combobox)
        ma_xuat_xu = self.combo_xuat_xu.currentIndex() + 1
        ma_the_loai = self.combo_the_loai.currentIndex() + 1

        # Tạo đối tượng DTOBaiHat
        bai_hat = DTOBaiHat(
            MaBaiHat=0,  # Tạm thời đặt 0, sẽ được cập nhật sau
            NgayPhatHanh=ngay_phat_hanh,
            TieuDe=ten_bai_hat,
            Anh=anh_bia,  # Cần chuyển thành đường dẫn nếu lưu vào DB
            MaXuatXu=ma_xuat_xu,
            TenXuatXu=xuat_xu,
            MaTheLoai=ma_the_loai,
            TenTheLoai=the_loai,
            FileNhac=file_nhac,
            CaSi=ca_si
        )
        self.show_info_message("Thông báo", self.bll.themBaiHat(bai_hat))
    def show_info_message(self, title, message):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Information)
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.exec()

