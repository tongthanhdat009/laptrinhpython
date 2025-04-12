import sys
import os

from datetime import datetime, date
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt

from admin.GUIChiTietDanhSachPhatHeThong import GUIChiTietDanhSachPhatHeThong
from admin.GUIThemDanhSachPhatHeThong import GUIThemDanhSachPhatHeThong
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from BLL.BLLQuanLyDanhSachPhatHeThong import BLLQuanLyDanhSachPhatHeThong

class GUIQuanLyDanhSachPhatHeThong(QWidget):
    def __init__(self):
        super().__init__()
        self.bll = BLLQuanLyDanhSachPhatHeThong()
        self.setFixedSize(1250, 650)
        
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        
        # Tiêu đề
        title_layout = QHBoxLayout()
        title_widget = QWidget()
        title_widget.setContentsMargins(0, 0, 0, 0)
        title_widget.setStyleSheet("background-color: #ffffff;")
        title_widget.setLayout(title_layout)
        
        title_label = QLabel("Danh Sách Phát:")
        title_label.setFont(QFont("Arial", 26, QFont.Weight.Bold))
        title_label.setStyleSheet("color: #000; background-color: transparent;")
        
        title_layout.addWidget(title_label)
        
        # Bảng hiển thị danh sách
        table_widget = QWidget()
        table_widget.setStyleSheet("background-color: #ffffff;")
        table_layout = QVBoxLayout(table_widget)
        table_layout.setContentsMargins(0, 0, 0, 0)
        
        self.table = QTableWidget()
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(["ID", "Ảnh", "Tiêu Đề Danh Sách", "Mô Tả", "Ngày Tạo", "Chi Tiết Danh Sách","Xoá Danh Sách"])
        self.table.setStyleSheet("""
            background-color: #ffffff;
            gridline-color: transparent;
            border: none;
            font-size: 18px;
            font-family: Arial;
            color: #000;
        """)
        from PyQt6.QtWidgets import QHeaderView

        self.table.setColumnWidth(0, 60)   # ID (cố định)
        self.table.setColumnWidth(1, 120)  # Ảnh (cố định)
        self.table.setColumnWidth(4, 150)  # Ngày Tạo (cố định)
        self.table.setColumnWidth(6, 140)  # Xóa Danh Sách (cố định)

        # Các cột còn lại sẽ mở rộng để lấp đầy khoảng trống
        self.table.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)  # Tiêu Đề Danh Sách
        self.table.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeMode.Stretch)  # Mô Tả
        self.table.horizontalHeader().setSectionResizeMode(5, QHeaderView.ResizeMode.Stretch)  # Chi Tiết Danh Sách

        self.table.verticalHeader().setVisible(False)
        self.table.verticalHeader().setDefaultSectionSize(80)
        
        # Input tìm kiếm tên bài hát
        self.search_title = QLineEdit()
        self.search_title.setPlaceholderText("Tên danh sách phát...")
        self.search_title.setStyleSheet("""
            font-size: 14px;
            padding: 5px;
            color: black;  /* Màu chữ khi người dùng nhập */
            QLineEdit::placeholder {
                color: gray;  /* Màu của placeholder */
                font-size: 14px;
            }
        """)
        
        search_button = QPushButton("🔍Tìm kiếm")
        search_button.setStyleSheet("""
            QPushButton {
                background-color: #2196F3; 
                color: white; 
                padding: 10px; 
                font-size: 16px; 
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #1976D2;
            }
        """)
        search_button.clicked.connect(self.BamTimKiem)
        
        self.btn_them = QPushButton("➕Thêm")
        self.btn_them.setStyleSheet("""
            QPushButton {
                background-color: black; 
                color: white; 
                padding: 10px; 
                font-size: 16px; 
                border-radius: 5px;
                border: 2px solid transparent;
            }
            QPushButton:hover {
                background-color: #333333;
                border: 2px solid white;
            }
        """)       
        self.btn_them.clicked.connect(self.BamNutThem)
        
        self.refresh_button = QPushButton("🔄Refresh")
        self.refresh_button.setStyleSheet("""
            QPushButton {
                background-color: #2196F3; 
                color: white; 
                padding: 10px; 
                font-size: 16px; 
                border-radius: 5px;
            }
            QPushButton:hover {
                background-color: #1976D2;
            }
        """)
        self.refresh_button.clicked.connect(self.refresh)
        
        self.NoiDungBang()
        
        table_layout.addWidget(self.table)
        title_layout.addWidget(self.search_title)  
        title_layout.addWidget(search_button)  
        title_layout.addWidget(self.btn_them)
        title_layout.addWidget(self.refresh_button)
        
        main_layout.addWidget(title_widget)
        main_layout.addWidget(table_widget)
        main_layout.setSpacing(0)
        
        self.setLayout(main_layout)

    def NoiDungBang(self):
        danh_sach = self.bll.lay_danh_sach_phat_he_thong()
        self.table.setRowCount(len(danh_sach))  

        for row_idx, ds_phat in enumerate(danh_sach):
            self._tao_cot_thong_tin(row_idx, ds_phat)
            self._tao_cot_anh(row_idx, ds_phat.Anh)
            self._tao_nut_chi_tiet(row_idx, ds_phat.MaDanhSachPhatHeThong)
            self._tao_nut_xoa(row_idx, ds_phat.MaDanhSachPhatHeThong)

    def _tao_cot_thong_tin(self, row_idx, ds_phat):
        # Hàm trợ giúp để tạo item căn giữa
        def center_item(text):
            item = QTableWidgetItem(str(text))
            item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            return item
        
        # Thiết lập các cột thông tin
        self.table.setItem(row_idx, 0, center_item(ds_phat.MaDanhSachPhatHeThong))
        self.table.setItem(row_idx, 2, center_item(ds_phat.TieuDe))
        
        # Mô tả có thể để mặc định hoặc căn giữa tùy bạn
        item_mo_ta = QTableWidgetItem(ds_phat.MoTa)
        self.table.setItem(row_idx, 3, item_mo_ta)
        
        # Định dạng ngày tạo
        ngay_tao = ds_phat.NgayTao.strftime('%Y-%m-%d') if isinstance(ds_phat.NgayTao, (datetime, date)) else str(ds_phat.NgayTao)
        self.table.setItem(row_idx, 4, center_item(ngay_tao))

    def _tao_cot_anh(self, row_idx, duong_dan_anh):
        label = QLabel()
        label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        if not duong_dan_anh:
            self._them_anh_mac_dinh(label)
        else:
            self._load_anh_tu_duong_dan(label, duong_dan_anh)
        
        self.table.setCellWidget(row_idx, 1, label)

    def _them_anh_mac_dinh(self, label):
        default_image = r"assets\DanhSachPhatHeThong\0.png"
        print(f"Using default image: {default_image}")
        pixmap = QPixmap(default_image)
        
        if pixmap.isNull():
            print(f"Failed to load default image")
            label.setText("No Image")
        else:
            pixmap = pixmap.scaled(100, 100, Qt.AspectRatioMode.KeepAspectRatio)
            label.setPixmap(pixmap)

    def _load_anh_tu_duong_dan(self, label, duong_dan):
        image_path = duong_dan.replace("/", "\\")
        print(f"Loading image from: {image_path}")
        
        pixmap = QPixmap(r"{}".format(image_path))
        print(image_path)
        if pixmap.isNull():
            print(f"Failed to load image from: {image_path}")
            import os
            abs_path = os.path.abspath(image_path.strip())
            print(f"Trying absolute path: {abs_path}")
            pixmap = QPixmap(abs_path)
            
            if pixmap.isNull():
                # Sử dụng ảnh mặc định khi không tải được
                self._them_anh_mac_dinh(label)
            else:
                pixmap = pixmap.scaled(100, 100, Qt.AspectRatioMode.KeepAspectRatio)
                label.setPixmap(pixmap)
        else:
            pixmap = pixmap.scaled(100, 100, Qt.AspectRatioMode.KeepAspectRatio)
            label.setPixmap(pixmap)

    def _tao_nut_chi_tiet(self, row_idx, ma_danh_sach):
        btn_chi_tiet = QPushButton("Chi Tiết")
        btn_chi_tiet.setStyleSheet("background-color: #4CAF50; color: white; padding: 5px;")
        btn_chi_tiet.clicked.connect(lambda _, id=ma_danh_sach: self.XemChiTiet(id))
        self.table.setCellWidget(row_idx, 5, btn_chi_tiet)

    def _tao_nut_xoa(self, row_idx, ma_danh_sach):
        btn_xoa = QPushButton("Xóa")
        btn_xoa.setStyleSheet("background-color: #FF5722; color: white; padding: 5px;")
        btn_xoa.clicked.connect(lambda _, id=ma_danh_sach: self.XoaDanhSach(id))
        self.table.setCellWidget(row_idx, 6, btn_xoa)
        
    def XemChiTiet(self, ma_ds):
        print(f"Xem chi tiết danh sách: {ma_ds}")
        dialog = GUIChiTietDanhSachPhatHeThong(ma_ds)
        dialog.exec()
        
    def XoaDanhSach(self, ma_ds):
        # Tạo dialog
        dialog = QDialog(self)
        dialog.setWindowTitle("Xác nhận xóa bài hát")
        dialog.setFixedWidth(400)
        dialog.setStyleSheet("""
            QDialog {
                background-color: white;
            }
            QLabel {
                color: #333333;
            }
            QLabel#title {
                font-weight: bold;
                font-size: 16px;
                color: #d32f2f;
            }
            QPushButton {
                padding: 8px 16px;
                border: none;
                border-radius: 4px;
            }
            QPushButton#delete {
                background-color: #f44336;
                color: white;
            }
            QPushButton#delete:hover {
                background-color: #d32f2f;
            }
            QPushButton#cancel {
                background-color: #e0e0e0;
                color: #333333;
            }
            QPushButton#cancel:hover {
                background-color: #bdbdbd;
            }
        """)
        
        # Layout chính
        layout = QVBoxLayout(dialog)
        layout.setSpacing(20)
        
        # Tiêu đề
        title = QLabel("Xác nhận xóa")
        title.setObjectName("title")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title)
        
        # Nội dung
        content = QLabel(f'Bạn có chắc chắn muốn danh sách khỏi danh sách phát hệ thống không không?\n\nHành động này không thể hoàn tác.')
        content.setWordWrap(True)
        content.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(content)
        
        # Nút
        button_layout = QHBoxLayout()
        button_layout.setSpacing(10)
        
        # Nút hủy
        cancel_button = QPushButton("Hủy")
        cancel_button.setObjectName("cancel")
        cancel_button.clicked.connect(dialog.reject)
        
        # Nút xóa
        delete_button = QPushButton("Xóa")
        delete_button.setObjectName("delete")
        delete_button.clicked.connect(dialog.accept)
        
        button_layout.addWidget(cancel_button)
        button_layout.addWidget(delete_button)
        
        layout.addLayout(button_layout)
        
        # Hiển thị dialog và xử lý kết quả
        result = dialog.exec()
        
        if result == QDialog.DialogCode.Accepted:
            try:
                result = self.bll.xoa_danh_sach_phat(ma_ds)
                if result:
                    self.NoiDungBang()
                    
                    QMessageBox.information(
                        self,
                        "Xóa danh sách phát thành công",
                        f"Đã xóa danh sách phát khỏi hệ thống.",
                        QMessageBox.StandardButton.Ok
                    )
                else:
                    QMessageBox.warning(
                        self,
                        "Xóa danh sách phát thất bại",
                        f"Không thể xóa danh sách phát khỏi hệ thống. Vui lòng thử lại.",
                        QMessageBox.StandardButton.Ok
                    )
                    
            except Exception as e:
                QMessageBox.critical(
                    self,
                    "Lỗi",
                    f"Đã xảy ra lỗi khi xóa bài hát: {str(e)}",
                    QMessageBox.StandardButton.Ok
                )
                print(f"Lỗi khi xóa bài hát: {e}")
        else:
            print(f"Hủy xóa danh sách phát hệ thống ID: {ma_ds}")
    
    def BamTimKiem(self):
        ten_danh_sach = self.search_title.text()
        print(f"Tìm kiếm danh sách phát: {ten_danh_sach}")
        
        danh_sach = self.bll.lay_danh_sach_phat_he_thong()
        danh_sach = [ds for ds in danh_sach if ten_danh_sach.lower() in ds.TieuDe.lower()]
        
        self.table.setRowCount(len(danh_sach))
        
        for row_idx, ds_phat in enumerate(danh_sach):
            self._tao_cot_thong_tin(row_idx, ds_phat)
            self._tao_cot_anh(row_idx, ds_phat.Anh)
            self._tao_nut_chi_tiet(row_idx, ds_phat.MaDanhSachPhatHeThong)
            self._tao_nut_xoa(row_idx, ds_phat.MaDanhSachPhatHeThong)
    
    def refresh(self):
        self.search_title.clear()
        self.NoiDungBang()
        
    def BamNutThem(self):
        print("Bấm nút thêm danh sách phát hệ thống")
        dialog = GUIThemDanhSachPhatHeThong(self,self.bll.lay_danh_sach_phat_he_thong())
        dialog.exec()