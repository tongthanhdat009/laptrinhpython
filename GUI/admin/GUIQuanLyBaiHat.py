from PyQt6.QtWidgets import QWidget, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QHBoxLayout
from BLL.BLLQuanLy import BLLQuanLy
class GUIQuanLyBaiHat(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1250, 650)
        self.setStyleSheet("background-color: #ffffff;")

        layout = QVBoxLayout()
        layout.setContentsMargins(10, 10, 10, 10)

        # Bảng danh sách bài hát
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["Mã Bài Hát", "Tiêu Đề", "Thể Loại", "Xuất Xứ", "Ca Sĩ"])
        layout.addWidget(self.table)

        # Layout chứa các nút chức năng
        btn_layout = QHBoxLayout()
        
        self.btn_them = QPushButton("Thêm")
        self.btn_them.setStyleSheet("background-color: #4CAF50; color: white; padding: 8px; font-size: 14px;")
        btn_layout.addWidget(self.btn_them)

        self.btn_xoa = QPushButton("Xóa")
        self.btn_xoa.setStyleSheet("background-color: #FF0000; color: white; padding: 8px; font-size: 14px;")
        btn_layout.addWidget(self.btn_xoa)

        layout.addLayout(btn_layout)
        self.setLayout(layout)

        # Load dữ liệu vào bảng
        self.layDSNhac()
    
    def layDSNhac(self):
        bll = BLLQuanLy()
        self.DSNhac = bll.layDanhSachBaiHat()

        self.table.setRowCount(len(self.DSNhac))

        for row, baiHat in enumerate(self.DSNhac):
            self.table.setItem(row, 0, QTableWidgetItem(str(baiHat.getMaBaiHat())))
            self.table.setItem(row, 1, QTableWidgetItem(baiHat.getTieuDe()))
            self.table.setItem(row, 2, QTableWidgetItem(baiHat.getTenTheLoai()))
            self.table.setItem(row, 3, QTableWidgetItem(baiHat.getTenXuatXu()))
            self.table.setItem(row, 4, QTableWidgetItem(", ".join(baiHat.getCaSi())))  # Hiển thị danh sách ca sĩ

a = GUIQuanLyBaiHat()