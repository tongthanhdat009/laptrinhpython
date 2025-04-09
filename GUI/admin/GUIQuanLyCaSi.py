import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem,
    QHBoxLayout, QLabel, QLineEdit, QMessageBox, QDialog
)
from GUI.admin.GUIThemCaSi import GUIThemCaSi
from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtCore import Qt
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from BLL.BLLQuanLy import BLLQuanLy

class GUIQuanLyCaSi(QWidget):
    def __init__(self):
        super().__init__()
        self.bll = BLLQuanLy()
        self.DSCaSi = self.bll.layDanhSachCaSi()
        self.DSCaSiXuat = self.DSCaSi
        self.setFixedSize(1250, 650)

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)

        title_layout = QHBoxLayout()
        title_widget = QWidget()
        title_widget.setContentsMargins(0, 0, 0, 0)
        title_widget.setStyleSheet("background-color: #ffffff;")
        title_widget.setLayout(title_layout)

        title_label = QLabel("Danh Sách Ca Sĩ")
        title_label.setFont(QFont("Arial", 26, QFont.Weight.Bold))
        title_label.setStyleSheet("color: #000; background-color: transparent;")

        self.btn_them = QPushButton("Thêm")
        self.btn_them.setStyleSheet("background-color: black; color: white; padding: 10px; font-size: 16px; border-radius: 5px;")
        self.btn_them.clicked.connect(self.BamNutThem)

        # Input tìm kiếm tên ca sĩ
        self.search_name = QLineEdit()
        self.search_name.setPlaceholderText("Tên ca sĩ...")
        self.search_name.setStyleSheet("""
            font-size: 14px;
            padding: 5px;
            color: black;
            QLineEdit::placeholder {
                color: gray;
                font-size: 14px;
            }
        """)

        search_button = QPushButton("Tìm kiếm")
        search_button.setStyleSheet("background-color: #2196F3; color: white; padding: 10px; font-size: 16px; border-radius: 5px;")
        search_button.clicked.connect(self.BamTimKiem)
        
        title_layout.addWidget(title_label)
        title_layout.addWidget(self.search_name)
        title_layout.addWidget(search_button)
        title_layout.addWidget(self.btn_them)

        main_layout.addWidget(title_widget)

        # Tạo QWidget chứa bảng danh sách ca sĩ
        table_widget = QWidget()
        table_widget.setStyleSheet("background-color: #ffffff;")
        table_layout = QVBoxLayout(table_widget)
        table_layout.setContentsMargins(0, 0, 0, 0)
        
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["ID", "Ảnh", "Tên Ca Sĩ", ""])
        self.table.cellDoubleClicked.connect(self.sua_ca_si)
        self.table.setStyleSheet("""
            background-color: #ffffff;
            gridline-color: transparent;
            border: none;
            font-size: 18px;
            font-family: Arial;
            color: #000;
        """)
        self.table.setColumnWidth(0, 80)   # ID
        self.table.setColumnWidth(1, 100)  # Ảnh
        self.table.setColumnWidth(2, 800)  # Tên Ca Sĩ
        self.table.setColumnWidth(3, 100)  # Nút Xóa

        self.table.verticalHeader().setVisible(False)
        self.table.verticalHeader().setDefaultSectionSize(80)

        table_layout.addWidget(self.table)
        main_layout.addWidget(table_widget)

        main_layout.setSpacing(0)
        self.setLayout(main_layout)
        self.layDSCaSi()

    def layDSCaSi(self):
        self.table.setRowCount(len(self.DSCaSiXuat))

        for row, ca_si in enumerate(self.DSCaSiXuat):
            # ID
            item_id = QTableWidgetItem(f"#{ca_si.getMaCaSi()}")
            item_id.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            item_id.setFont(QFont("Arial Black", 20, QFont.Weight.Bold))
            self.table.setItem(row, 0, item_id)

            # Ảnh đại diện
            label_image = QLabel()
            # Thử các định dạng ảnh khác nhau
            extensions = ['.png', '.jpg', '.jpeg']
            duong_dan_anh = None
            for ext in extensions:
                path = f"assets/CaSi/{ca_si.getMaCaSi()}{ext}"
                if os.path.exists(path):
                    duong_dan_anh = path
                    break
            
            if not duong_dan_anh:
                print(f"⚠️ Không tìm thấy ảnh cho ca sĩ {ca_si.getMaCaSi()}")
            duong_dan_anh = "assets/CaSi/0.png"  # Ảnh mặc định
            pixmap = QPixmap(duong_dan_anh)
            if not pixmap.isNull():
                pixmap = pixmap.scaled(80, 80, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
                label_image.setPixmap(pixmap)
            else:
                print(f"⚠️ Không thể load ảnh: {duong_dan_anh}")
            label_image.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.table.setCellWidget(row, 1, label_image)

            # Tên Ca Sĩ
            item_name = QTableWidgetItem(ca_si.getTenCaSi())
            item_name.setFont(QFont("Arial", 20))
            self.table.setItem(row, 2, item_name)

            # Nút Xóa
            btn_xoa = QPushButton("Xóa")
            btn_xoa.setStyleSheet("background-color: #FF0000; color: white; padding: 5px; font-size: 14px; border-radius: 3px;")
            self.table.setCellWidget(row, 3, btn_xoa)
            btn_xoa.clicked.connect(lambda checked, ma=ca_si.getMaCaSi(): self.on_xoa_clicked(ma))

    def on_xoa_clicked(self, ma_ca_si):
        reply = QMessageBox.question(
            self, "Xác nhận xóa", 
            f"Bạn có chắc chắn muốn xóa ca sĩ có mã {ma_ca_si} không?", 
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, 
            QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            result = self.bll.xoaCaSi(ma_ca_si)
            if result == "Thành công":
                QMessageBox.information(self, "Thông báo", "Xóa ca sĩ thành công!")
                self.DSCaSiXuat = self.bll.layDanhSachCaSi()
                self.layDSCaSi()
            else:
                QMessageBox.critical(self, "Lỗi", "Xóa ca sĩ thất bại!")

    def timKiemCaSi(self, ten_ca_si: str):
        filtered_ca_si = [ca_si for ca_si in self.DSCaSi if ten_ca_si.lower() in ca_si.getTenCaSi().lower()]
        self.DSCaSiXuat = filtered_ca_si
        self.layDSCaSi()

    def BamTimKiem(self):
        ten_ca_si = self.search_name.text()
        self.timKiemCaSi(ten_ca_si)

    def BamNutThem(self):
        # Open the Add Singer dialog
        them_ca_si_dialog = GUIThemCaSi(self, self.DSCaSi)
        if them_ca_si_dialog.exec() == QDialog.DialogCode.Accepted:
            # Refresh singer list after adding
            self.DSCaSi = self.bll.layDanhSachCaSi()
            self.DSCaSiXuat = self.DSCaSi
            self.layDSCaSi()

    def sua_ca_si(self, row, column):
        # Lấy mã ca sĩ từ cột đầu tiên
        ma_ca_si = int(self.table.item(row, 0).text().replace("#", ""))
        
        # Mở dialog chỉnh sửa với dữ liệu ca sĩ
        sua_ca_si_dialog = GUIThemCaSi(self, self.DSCaSi, ma_ca_si)
        if sua_ca_si_dialog.exec() == QDialog.DialogCode.Accepted:
            # Làm mới danh sách sau khi chỉnh sửa
            self.DSCaSi = self.bll.layDanhSachCaSi()
            self.DSCaSiXuat = self.DSCaSi
            self.layDSCaSi()
