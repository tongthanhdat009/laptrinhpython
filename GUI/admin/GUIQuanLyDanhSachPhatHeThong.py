import sys
import os

from datetime import datetime, date
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt

from admin.GUIThemBaiHat import GUIThemBaiHat
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from DAL.DALQuanLyDanhSachPhatHeThong import DALQuanLyDanhSachPhatHeThong

class GUIQuanLyDanhSachPhatHeThong(QWidget):
    def __init__(self):
        super().__init__()
        self.bll = DALQuanLyDanhSachPhatHeThong()
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
        
        search_button = QPushButton("Tìm kiếm")
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
        # search_button.clicked.connect(self.BamTimKiem)
        
        self.btn_them = QPushButton("Thêm")
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
        # self.btn_them.clicked.connect(self.BamNutThem)
        
        self.NoiDungBang()
        
        table_layout.addWidget(self.table)
        title_layout.addWidget(self.search_title)  
        title_layout.addWidget(search_button)  
        title_layout.addWidget(self.btn_them)
        
        main_layout.addWidget(title_widget)
        main_layout.addWidget(table_widget)
        main_layout.setSpacing(0)
        
        self.setLayout(main_layout)

    def NoiDungBang(self):
        danh_sach = self.bll.lay_danh_sach_phat_he_thong()

        self.table.setRowCount(len(danh_sach))  

        for row_idx, ds_phat in enumerate(danh_sach):
            self.table.setItem(row_idx, 0, QTableWidgetItem(str(ds_phat.MaDanhSachPhat)))
            self.table.setItem(row_idx, 2, QTableWidgetItem(ds_phat.TieuDe))
            self.table.setItem(row_idx, 3, QTableWidgetItem(ds_phat.MoTa))
            ngay_tao = ds_phat.NgayTao.strftime('%Y-%m-%d') if isinstance(ds_phat.NgayTao, (datetime, date)) else str(ds_phat.NgayTao)
            self.table.setItem(row_idx, 4, QTableWidgetItem(ngay_tao))

            # Ảnh (nếu có)
            if ds_phat.Anh:  
                label = QLabel()
                image_path = ds_phat.Anh.replace("/", "\\")
                print(f"Loading image from: {image_path}")
                
                pixmap = QPixmap(r"{}".format(image_path))
                
                if pixmap.isNull():
                    print(f"Failed to load image from: {image_path}")
                    import os
                    abs_path = os.path.abspath(image_path.strip())
                    print(f"Trying absolute path: {abs_path}")
                    pixmap = QPixmap(abs_path)
                    
                    if pixmap.isNull():
                        label.setText("No Image")
                    else:
                        pixmap = pixmap.scaled(100, 100, Qt.AspectRatioMode.KeepAspectRatio)
                        label.setPixmap(pixmap)
                else:
                    pixmap = pixmap.scaled(100, 100, Qt.AspectRatioMode.KeepAspectRatio)
                    label.setPixmap(pixmap)
                
                label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                self.table.setCellWidget(row_idx, 1, label)

            # Nút "Chi Tiết Danh Sách"
            btn_chi_tiet = QPushButton("Chi Tiết")
            btn_chi_tiet.setStyleSheet("background-color: #4CAF50; color: white; padding: 5px;")
            btn_chi_tiet.clicked.connect(lambda _, id=ds_phat.MaDanhSachPhat: self.XemChiTiet(id))
            self.table.setCellWidget(row_idx, 5, btn_chi_tiet)

            # Nút "Xóa"
            btn_xoa = QPushButton("Xóa")
            btn_xoa.setStyleSheet("background-color: #FF5722; color: white; padding: 5px;")
            btn_xoa.clicked.connect(lambda _, id=ds_phat.MaDanhSachPhat: self.XoaDanhSach(id))
            self.table.setCellWidget(row_idx, 6, btn_xoa)

    # Move these methods outside the NoiDungBang method to make them class methods
    def XemChiTiet(self, ma_ds):
        print(f"Xem chi tiết danh sách: {ma_ds}")

    def XoaDanhSach(self, ma_ds):
        print(f"Xóa danh sách: {ma_ds}")