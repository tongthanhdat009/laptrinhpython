import sys
import os
from PyQt6.QtWidgets import (
    QWidget, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem,
    QHBoxLayout, QLabel, QLineEdit, QComboBox, QCompleter, QMessageBox
)
from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtCore import Qt
from admin.GUIThemBaiHat import GUIThemBaiHat
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from BLL.BLLQuanLy import BLLQuanLy

class GUIQuanLyBaiHat(QWidget):
    def __init__(self):
        super().__init__()
        self.bll = BLLQuanLy()
        self.DSNhac = self.bll.layDanhSachBaiHat()
        self.DSNhacXuat = self.DSNhac
        self.setFixedSize(1250, 650)

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)

        title_layout = QHBoxLayout()
        title_widget = QWidget()
        title_widget.setContentsMargins(0, 0, 0, 0)
        title_widget.setStyleSheet("background-color: #ffffff;")
        title_widget.setLayout(title_layout)

        title_label = QLabel("Danh Sách Bài Hát")
        title_label.setFont(QFont("Arial", 26, QFont.Weight.Bold))
        title_label.setStyleSheet("color: #000; background-color: transparent;")

        self.btn_them = QPushButton("Thêm")
        self.btn_them.setStyleSheet("background-color: black; color: white; padding: 10px; font-size: 16px; border-radius: 5px;")
        self.btn_them.clicked.connect(self.BamNutThem)

        # Input tìm kiếm tên bài hát
        self.search_title = QLineEdit()
        self.search_title.setPlaceholderText("Tên bài hát...")
        self.search_title.setStyleSheet("""
            font-size: 14px;
            padding: 5px;
            color: black;  /* Màu chữ khi người dùng nhập */
            QLineEdit::placeholder {
                color: gray;  /* Màu của placeholder */
                font-size: 14px;
            }
        """)

        # Tìm kiếm ca sĩ
        self.search_singer = QComboBox()
        self.search_singer.setStyleSheet("""
            font-size: 16px;  /* Chữ lớn hơn */
            padding: 5px;
            color: black;  /* Màu chữ của các item */
            QComboBox::item {
                color: black;  /* Màu chữ của các item */
                font-size: 16px;  /* Chữ lớn hơn trong các item */
            }
            QComboBox::drop-down {
                background-color: white;  /* Màu nền trắng cho drop-down */
                border: 1px solid #ccc;  /* Viền nhẹ cho drop-down */
            }
        """)
        self.search_singer.setFixedWidth(200)
        self.search_singer.setEditable(True)
        singers_list = self.bll.layToanBoTenCaSi()
        singers_list.insert(0, "Tất cả ca sĩ")

        # Thêm tất cả ca sĩ vào QComboBox
        self.search_singer.addItems(singers_list)

        # Tạo completer và gán vào QComboBox
        completer = QCompleter(singers_list)
        self.search_singer.setCompleter(completer)
        completer.setFilterMode(Qt.MatchFlag.MatchContains)
        completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        popup = completer.popup()
        popup.setStyleSheet("""
            background-color: white;  /* Màu nền trắng của completer */
            font-size: 16px;  /* Chữ lớn hơn trong completer */
            color: black;  /* Màu chữ đen */
        """)

        search_button = QPushButton("Tìm kiếm")
        search_button.setStyleSheet("background-color: #2196F3; color: white; padding: 10px; font-size: 16px; border-radius: 5px;")
        search_button.clicked.connect(self.BamTimKiem)
        title_layout.addWidget(title_label)
        title_layout.addWidget(self.search_title)  # Thêm input tìm kiếm tên bài hát
        title_layout.addWidget(self.search_singer)  # Thêm input tìm kiếm ca sĩ
        title_layout.addWidget(search_button)
        title_layout.addWidget(self.btn_them)

        main_layout.addWidget(title_widget)

        # Tạo QWidget chứa bảng danh sách bài hát
        table_widget = QWidget()
        table_widget.setStyleSheet("background-color: #ffffff;")
        table_layout = QVBoxLayout(table_widget)
        table_layout.setContentsMargins(0, 0, 0, 0)
        
        self.table = QTableWidget()
        self.table.setColumnCount(7)  # Thêm cột ảnh ở vị trí 2
        self.table.setHorizontalHeaderLabels(["ID", "Ảnh", "Tiêu Đề & Ca Sĩ", "Thể Loại", "Xuất Xứ", "Ngày Phát Hành", ""])
        self.table.setStyleSheet("""
            background-color: #ffffff;
            gridline-color: transparent;
            border: none;
            font-size: 18px;
            font-family: Arial;
            color: #000;
        """)
        self.table.setColumnWidth(0, 80)   # ID
        self.table.setColumnWidth(1, 100)   # Ảnh
        self.table.setColumnWidth(2, 500)  # Tiêu Đề & Ca Sĩ
        self.table.setColumnWidth(3, 175)  # Thể Loại
        self.table.setColumnWidth(4, 100)  # Xuất Xứ
        self.table.setColumnWidth(5, 180)  # Ngày Phát Hành
        self.table.setColumnWidth(6, 100)  # Nút Xóa

        self.table.verticalHeader().setVisible(False)
        self.table.verticalHeader().setDefaultSectionSize(80)

        # Điều chỉnh kích thước cột

        table_layout.addWidget(self.table)
        main_layout.addWidget(table_widget)

        main_layout.setSpacing(0)

        self.setLayout(main_layout)
        self.layDSNhac()

    def layDSNhac(self):
        # Lấy thư mục gốc của project
        self.table.setRowCount(len(self.DSNhacXuat))

        for row, baiHat in enumerate(self.DSNhacXuat):

            item_id = QTableWidgetItem(f"#{baiHat.getMaBaiHat()}")
            item_id.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            item_id.setFont(QFont("Arial Black", 20, QFont.Weight.Bold))  # 🔹 Chữ to, đậm
            self.table.setItem(row, 0, item_id)

            # Lấy đường dẫn ảnh từ SQL và xử lý
            duong_dan_sql = baiHat.getAnh().lstrip("\\/")  # Xóa dấu '\' hoặc '/' đầu chuỗi nếu có

            # Hiển thị ảnh trong QLabel
            label_image = QLabel()
            pixmap = QPixmap(duong_dan_sql)
            if not pixmap.isNull():
                pixmap = pixmap.scaled(80, 80, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
                label_image.setPixmap(pixmap)
            else:
                print(f"⚠️ Không thể load ảnh: {duong_dan_sql}")
            label_image.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.table.setCellWidget(row, 1, label_image)

            # Tiêu đề và ca sĩ
            danh_sach_ca_si = [ca_si.split("-", 1)[-1] for ca_si in baiHat.getCaSi()]
            ten_ca_si = ", ".join(danh_sach_ca_si)
            label_tieu_de = QLabel(baiHat.getTieuDe())
            label_tieu_de.setStyleSheet("font-size: 20px; font-weight: bold; color: black;")
            label_ca_si = QLabel(ten_ca_si)
            label_ca_si.setStyleSheet("font-size: 14px; color: gray;")  
            widget_title_casi = QWidget()
            widget_title_casi.setFixedHeight(55)
            layout_title_casi = QVBoxLayout()
            layout_title_casi.setContentsMargins(10, 0, 0, 0)  
            layout_title_casi.addWidget(label_tieu_de)
            layout_title_casi.addWidget(label_ca_si)
            widget_title_casi.setLayout(layout_title_casi)
            self.table.setCellWidget(row, 2, widget_title_casi)

            # Thể loại
            item_type = QTableWidgetItem(baiHat.getTenTheLoai())
            item_type.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.table.setItem(row, 3, item_type)

            # Xuất xứ
            item_origin = QTableWidgetItem(baiHat.getTenXuatXu())
            item_origin.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.table.setItem(row, 4, item_origin)

            # Ngày phát hành
            item_date = QTableWidgetItem(str(baiHat.getNgayPhatHanh()))
            item_date.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.table.setItem(row, 5, item_date)

            # Nút Xóa
            btn_xoa = QPushButton("Xóa")
            btn_xoa.setStyleSheet("background-color: #FF0000; color: white; padding: 5px; font-size: 14px; border-radius: 3px;")
            self.table.setCellWidget(row, 6, btn_xoa)
            btn_xoa.clicked.connect(lambda checked, ma=baiHat.getMaBaiHat(): self.on_xoa_clicked(ma))

    def on_xoa_clicked(self, ma_bai_hat):
        reply = QMessageBox.question(
            self, "Xác nhận xóa", 
            f"Bạn có chắc chắn muốn xóa bài hát có mã {ma_bai_hat} không?", 
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No, 
            QMessageBox.StandardButton.No
        )

        if reply == QMessageBox.StandardButton.Yes:
            result = self.bll.xoaBaiHat(ma_bai_hat)  
            if result == "Thành công":
                QMessageBox.information(self, "Thông báo", "Xóa bài hát thành công!")
                self.DSNhacXuat = self.bll.layDanhSachBaiHat()  # Cập nhật lại danh sách
                self.layDSNhac()  # Load lại danh sách bài hát
            else:
                QMessageBox.critical(self, "Lỗi", "Xóa bài hát thất bại!")

       
    def timKiemBaiHat(self, tenBaiHat: str, tenCaSi: str):
        # Lọc danh sách bài hát theo tên bài hát
        print(tenCaSi)
        filtered_bai_hat = [baiHat for baiHat in self.DSNhac if tenBaiHat.lower() in baiHat.getTieuDe().lower()]
        # Lọc thêm theo tên ca sĩ
        if tenCaSi != "Tất cả ca sĩ":
            filtered_bai_hat = [
                baiHat for baiHat in filtered_bai_hat
                if any(tenCaSi.lower() in ca_si.lower() for ca_si in baiHat.getCaSi())
            ]
        self.DSNhacXuat = filtered_bai_hat
        self.layDSNhac()

    def BamTimKiem(self):
        ten_bai_hat = self.search_title.text()  # Lấy tên bài hát từ input
        ten_ca_si = self.search_singer.currentText()  # Lấy tên ca sĩ từ combobox
        self.timKiemBaiHat(ten_bai_hat, ten_ca_si)  # Gọi hàm tìm kiếm

    def BamNutThem(self):
        dialog = GUIThemBaiHat(self,self.DSNhac)
        dialog.exec()
