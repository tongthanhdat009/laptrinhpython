import sys
import os

from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QHBoxLayout, QPushButton, 
                             QTableWidget, QTableWidgetItem, QLabel, QLineEdit,
                             QHeaderView, QFrame, QDialog, QMessageBox)
from PyQt6.QtGui import QFont, QPixmap
from PyQt6.QtCore import Qt
from datetime import datetime, date
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from BLL.BLLQuanLyDanhSachPhatHeThong import BLLQuanLyDanhSachPhatHeThong
from GUI.admin.GUIThemBaiHatDSPHT import GUIThemBaiHatDSPHT
from GUI.admin.GUIChinhSuaDanhSachPhatHeThong import GUIChinhSuaDanhSachPhatHeThong
class GUIChiTietDanhSachPhatHeThong(QDialog):
    def __init__(self, ma_danh_sach:int):
        super().__init__()
        self.ma_danh_sach = ma_danh_sach
        self.bll = BLLQuanLyDanhSachPhatHeThong()
        self.danh_sach = self.bll.lay_danh_sach_phat_he_thong_theo_ma(ma_danh_sach)
        self.danh_sach_nhac = self.bll.lay_danh_sach_bai_hat_theo_ma_danh_sach(ma_danh_sach)
        self.setWindowTitle("Chi Tiết Danh Sách Phát")
        self.setFixedSize(1000, 600)
        self.setUpUI()
        
    def setUpUI(self):
        # Layout chính
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        
        # Tiêu đề với ảnh và thông tin
        title_widget = QWidget()
        title_layout = QHBoxLayout(title_widget)
        title_layout.setContentsMargins(0, 0, 0, 20)

        # Ảnh danh sách phát (bên trái)
        self.image_label = QLabel()
        self.image_label.setFixedSize(120, 120)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Tải ảnh từ đường dẫn của danh sách
        # Sử dụng hàm trong UI
        self.image_label = QLabel()
        self.image_label.setFixedSize(120, 120)
        self.image_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        pixmap = self._load_image(self.danh_sach.Anh)
        if pixmap:
            self.image_label.setPixmap(pixmap)
        else:
            self.image_label.setText("No Image")
            self.image_label.setStyleSheet("background-color: #f0f0f0; border-radius: 10px;")

        # Container cho tiêu đề và mô tả (bên phải)
        info_container = QWidget()
        info_layout = QVBoxLayout(info_container)
        info_layout.setContentsMargins(20, 0, 0, 0)
        info_layout.setSpacing(5)

        # Tiêu đề danh sách phát
        self.title_label = QLabel(self.danh_sach.TieuDe)
        self.title_label.setFont(QFont("Arial", 24, QFont.Weight.Bold))
        self.title_label.setStyleSheet("color: #2196F3;")

        # Mô tả danh sách phát
        self.desc_label = QLabel(self.danh_sach.MoTa)
        self.desc_label.setFont(QFont("Arial", 14))
        self.desc_label.setStyleSheet("color: #757575;")
        self.desc_label.setWordWrap(True)

        # Thêm tiêu đề và mô tả vào container
        info_layout.addWidget(self.title_label)
        info_layout.addWidget(self.desc_label)
        info_layout.addStretch()

        # Thêm ảnh và thông tin vào layout tiêu đề
        title_layout.addWidget(self.image_label)
        title_layout.addWidget(info_container, 1)  # Số 1 để info_container có thể mở rộng

        # Đường kẻ phân cách dưới tiêu đề
        separator = QFrame()
        separator.setFrameShape(QFrame.Shape.HLine)
        separator.setFrameShadow(QFrame.Shadow.Sunken)
        separator.setStyleSheet("background-color: #e0e0e0; min-height: 1px;")

        # Thêm widget tiêu đề và đường kẻ vào layout chính
        main_layout.addWidget(title_widget)
        main_layout.addWidget(separator)
        
        # Layout thanh tìm kiếm và nút thêm
        search_layout = QHBoxLayout()
        
        # Thanh tìm kiếm
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Tìm kiếm bài hát...")
        self.search_input.setStyleSheet("""
            QLineEdit {
                padding: 8px;
                border: 1px solid #ccc;
                border-radius: 4px;
                font-size: 14px;
            }
        """)
        
        # Nút tìm kiếm
        search_button = QPushButton("🔍Tìm Kiếm")
        search_button.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #1976D2;
            }
        """)
        search_button.clicked.connect(self.tim_kiem_bai_hat)
        
        # Nút thêm bài hát
        add_button = QPushButton("➕Thêm Bài Hát")
        add_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #388E3C;
            }
        """)
        add_button.clicked.connect(self.them_bai_hat)
        
        # nút sửa thông tin danh sách
        edit_button = QPushButton("📝Sửa")
        edit_button.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;  
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #1976D2;  
            }
        """)     
        edit_button.clicked.connect(self.sua_danh_sach)
        
        # nút refresh
        refresh_button = QPushButton("🔄Refresh")
        refresh_button.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;  
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #1976D2;  
            }
        """)           
        
        refresh_button.clicked.connect(self.lam_moi_danh_sach)
        
        search_layout.addWidget(self.search_input, 7)
        search_layout.addWidget(search_button, 1)
        search_layout.addWidget(add_button, 2)
        search_layout.addWidget(edit_button, 1)
        search_layout.addWidget(refresh_button, 1)
        main_layout.addLayout(search_layout)
        
        # Bảng hiển thị danh sách bài hát
        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(["ID", "Ảnh", "Tên Bài Hát", "Ca Sĩ", "Xóa"])
        self.table.setStyleSheet("""
            QTableWidget {
                border: 1px solid #ddd;
                border-radius: 4px;
                background-color: white;
                gridline-color: #f0f0f0;
            }
            QHeaderView::section {
                background-color: #f5f5f5;
                padding: 8px;
                font-size: 14px;
                font-weight: bold;
                border: 1px solid #ddd;
            }
            QTableWidget::item {
                padding: 8px;
            }
        """)
        
        # Thiết lập độ rộng cột
        self.table.setColumnWidth(0, 80)  # ID
        self.table.setColumnWidth(1, 120)  # Ảnh
        self.table.setColumnWidth(4, 100)  # Xóa
        
        # Các cột còn lại mở rộng tự động
        self.table.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)  # Tên bài hát
        self.table.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeMode.Stretch)  # Ca sĩ
        
        self.table.verticalHeader().setVisible(False)
        self.table.verticalHeader().setDefaultSectionSize(125)
        
        main_layout.addWidget(self.table)
        
        # Button Layout (Đóng, Lưu thay đổi, v.v.)
        button_layout = QHBoxLayout()
        
        close_button = QPushButton("Đóng")
        close_button.setStyleSheet("""
            QPushButton {
                background-color: #f44336;
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 4px;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #d32f2f;
            }
        """)
        close_button.clicked.connect(self.close)
        
        button_layout.addStretch()
        button_layout.addWidget(close_button)
        
        main_layout.addLayout(button_layout)
        
        self.setLayout(main_layout)
        
        # Load dữ liệu
        self.load_danh_sach_bai_hat()
        
    def load_danh_sach_bai_hat(self):
        # Đặt số dòng bảng bằng 0 trước khi cập nhật
        self.table.setRowCount(0)
        
        # Nếu không có dữ liệu, dừng lại
        if not self.danh_sach_nhac:
            return
        
        # Thiết lập số dòng
        self.table.setRowCount(len(self.danh_sach_nhac))
        
        # Tải dữ liệu vào từng dòng
        for row, bai_hat in enumerate(self.danh_sach_nhac):
            # ID
            id_item = QTableWidgetItem(str(f'#{bai_hat.getMaBaiHat()}'))
            id_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            font = QFont()
            font.setPointSize(14)
            font.setBold(True)
            id_item.setFont(font)
            self.table.setItem(row, 0, id_item)
            
            # Ảnh
            label = QLabel()
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            
            # Xử lý ảnh
            anh_path = bai_hat.getAnh()
            if anh_path != None:
                image_path = anh_path.replace("/", "\\")
                print(f"Đang tải ảnh từ: {image_path}")
                
                if image_path.startswith("\\") or image_path.startswith("..") or image_path.startswith(".\\") or image_path.startswith("./"):
                    current_dir = os.path.dirname(os.path.abspath(__file__))
                    project_root = os.path.dirname(os.path.dirname(current_dir))
                    
                    if image_path.startswith("\\"):
                        image_path = image_path[1:]  
                        image_path = os.path.normpath(os.path.join(project_root, image_path))
                    else:
                        image_path = os.path.normpath(os.path.join(current_dir, image_path))
                    print(f"Đường dẫn đã xử lý: {image_path}")
                    pixmap = QPixmap(image_path)
                    label.setPixmap(pixmap.scaled(120, 120, Qt.AspectRatioMode.KeepAspectRatio))
                    if pixmap.isNull():
                        print(f"Không thể tải ảnh từ đường dẫn: {image_path}")
                        self._them_anh_mac_dinh(label)
            else:
                self._them_anh_mac_dinh(label)
                
            self.table.setCellWidget(row, 1, label)
            
            # Tên bài hát
            ten_item = QTableWidgetItem(bai_hat.getTieuDe())
            ten_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            ten_item.setFont(QFont("Arial", 10))
            self.table.setItem(row, 2, ten_item)
            
            # Ca sĩ - hợp nhất danh sách ca sĩ thành chuỗi
            ca_si_names = []
            if bai_hat.getCaSi():
                for ca_si in bai_hat.getCaSi():
                    if isinstance(ca_si, dict) and "TenCaSi" in ca_si:
                        ca_si_names.append(ca_si["TenCaSi"])
                    elif hasattr(ca_si, "TenCaSi"):
                        ca_si_names.append(ca_si.TenCaSi)
            
            ca_si_text = ", ".join(ca_si_names) if ca_si_names else "Không có thông tin"
            ca_si_item = QTableWidgetItem(ca_si_text)
            ca_si_item.setTextAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft)
            ca_si_item.setFont(QFont("Arial", 10))
            self.table.setItem(row, 3, ca_si_item)
            
            # Nút xóa
            btn_xoa = QPushButton("🗑️Xóa")
            btn_xoa.setStyleSheet("""
                QPushButton {
                    background-color: #f44336;
                    color: white;
                    border: none;
                    padding: 5px;
                    border-radius: 3px;
                }
                QPushButton:hover {
                    background-color: #d32f2f;
                }
            """)
            btn_xoa.clicked.connect(lambda _, id=bai_hat.getMaBaiHat(): self.xoa_bai_hat(id))
            self.table.setCellWidget(row, 4, btn_xoa)

    def _them_anh_mac_dinh(self, label):
        """Thêm ảnh mặc định vào label"""
        default_image = r"assets\AnhBaiHat\0.png"
        print(f"Sử dụng ảnh mặc định: {default_image}")
        pixmap = QPixmap(default_image)
        
        if pixmap.isNull():
            print(f"Không thể tải ảnh mặc định")
            label.setText("No Image")
        else:
            pixmap = pixmap.scaled(80, 80, Qt.AspectRatioMode.KeepAspectRatio)
            label.setPixmap(pixmap)
    
    def tim_kiem_bai_hat(self):
        search_text = self.search_input.text().strip().lower()
        search_type = self.search_type.currentText() if hasattr(self, 'search_type') else "Tất cả"
        
        # Đặt lại thông báo trạng thái
        if hasattr(self, 'status_label'):
            self.status_label.clear()
        
        if not search_text:
            # Nếu ô tìm kiếm trống, hiển thị lại toàn bộ danh sách
            self.load_danh_sach_bai_hat()
            if hasattr(self, 'status_label'):
                self.status_label.setText(f"Hiển thị tất cả {len(self.danh_sach_nhac)} bài hát trong danh sách")
            return
        
        # Xóa nội dung bảng hiện tại
        self.table.setRowCount(0)
        
        # Lọc danh sách bài hát theo từ khóa và loại tìm kiếm
        bai_hat_tim_thay = []
        
        for bai_hat in self.danh_sach_nhac:
            # Tìm kiếm trong tên bài hát
            ten_bai_hat = bai_hat.getTieuDe().lower()
            
            # Tìm kiếm trong tên ca sĩ
            ca_si_names = []
            if bai_hat.getCaSi():
                for ca_si in bai_hat.getCaSi():
                    if isinstance(ca_si, dict) and "TenCaSi" in ca_si:
                        ca_si_names.append(ca_si["TenCaSi"].lower())
                    elif hasattr(ca_si, "TenCaSi"):
                        ca_si_names.append(ca_si.TenCaSi.lower())
            
            ca_si_text = " ".join(ca_si_names).lower()
            
            # Kiểm tra theo loại tìm kiếm
            if search_type == "Tất cả":
                if search_text in ten_bai_hat or search_text in ca_si_text:
                    bai_hat_tim_thay.append(bai_hat)
            elif search_type == "Tên bài hát":
                if search_text in ten_bai_hat:
                    bai_hat_tim_thay.append(bai_hat)
            elif search_type == "Ca sĩ":
                if search_text in ca_si_text:
                    bai_hat_tim_thay.append(bai_hat)
        
        # Hiển thị kết quả tìm kiếm
        if bai_hat_tim_thay:
            # Thiết lập số dòng cho bảng
            self.table.setRowCount(len(bai_hat_tim_thay))
            
            # Hiển thị các bài hát đã tìm thấy
            for row, bai_hat in enumerate(bai_hat_tim_thay):
                # ID
                id_item = QTableWidgetItem(str(f'#{bai_hat.getMaBaiHat()}'))
                id_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                font = QFont()
                font.setPointSize(14)
                font.setBold(True)
                id_item.setFont(font)
                self.table.setItem(row, 0, id_item)
                
                # Ảnh
                label = QLabel()
                label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                
                # Xử lý ảnh
                anh_path = bai_hat.getAnh()
                if anh_path != None:
                    image_path = anh_path.replace("/", "\\")
                    
                    if image_path.startswith("\\") or image_path.startswith("..") or image_path.startswith(".\\") or image_path.startswith("./"):
                        current_dir = os.path.dirname(os.path.abspath(__file__))
                        project_root = os.path.dirname(os.path.dirname(current_dir))
                        
                        if image_path.startswith("\\"):
                            image_path = image_path[1:]  
                            image_path = os.path.normpath(os.path.join(project_root, image_path))
                        else:
                            image_path = os.path.normpath(os.path.join(current_dir, image_path))
                        
                        pixmap = QPixmap(image_path)
                        label.setPixmap(pixmap.scaled(120, 120, Qt.AspectRatioMode.KeepAspectRatio))
                        if pixmap.isNull():
                            self._them_anh_mac_dinh(label)
                else:
                    self._them_anh_mac_dinh(label)
                    
                self.table.setCellWidget(row, 1, label)
                
                # Tên bài hát - Đánh dấu từ khóa tìm kiếm
                ten_bai_hat = bai_hat.getTieuDe()
                ten_item = QTableWidgetItem(ten_bai_hat)
                ten_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                
                self.table.setItem(row, 2, ten_item)
                
                # Ca sĩ - hợp nhất danh sách ca sĩ thành chuỗi
                ca_si_names = []
                if bai_hat.getCaSi():
                    for ca_si in bai_hat.getCaSi():
                        if isinstance(ca_si, dict) and "TenCaSi" in ca_si:
                            ca_si_names.append(ca_si["TenCaSi"])
                        elif hasattr(ca_si, "TenCaSi"):
                            ca_si_names.append(ca_si.TenCaSi)
                
                ca_si_text = ", ".join(ca_si_names) if ca_si_names else "Không có thông tin"
                ca_si_item = QTableWidgetItem(ca_si_text)
                ca_si_item.setTextAlignment(Qt.AlignmentFlag.AlignVCenter | Qt.AlignmentFlag.AlignLeft)
                
                self.table.setItem(row, 3, ca_si_item)
                
                # Nút xóa
                btn_xoa = QPushButton("🗑️Xóa")
                btn_xoa.setStyleSheet("""
                    QPushButton {
                        background-color: #f44336;
                        color: white;
                        border: none;
                        padding: 5px;
                        border-radius: 3px;
                    }
                    QPushButton:hover {
                        background-color: #d32f2f;
                    }
                """)
                btn_xoa.clicked.connect(lambda _, id=bai_hat.getMaBaiHat(): self.xoa_bai_hat(id))
                self.table.setCellWidget(row, 4, btn_xoa)
            
            # Cập nhật thanh trạng thái
            if hasattr(self, 'status_label'):
                self.status_label.setText(f"Tìm thấy {len(bai_hat_tim_thay)}/{len(self.danh_sach_nhac)} bài hát phù hợp với từ khóa '{search_text}'")
                self.status_label.setStyleSheet("""
                    QLabel {
                        background-color: #e3f2fd;
                        color: #1976D2;
                        padding: 8px;
                        border-radius: 4px;
                        font-size: 13px;
                        border: 1px solid #bbdefb;
                    }
                """)
            else:
                # Hiển thị thông báo kết quả tìm kiếm bằng hộp thoại
                QMessageBox.information(
                    self,
                    "Kết quả tìm kiếm",
                    f"Tìm thấy {len(bai_hat_tim_thay)} bài hát phù hợp với từ khóa '{search_text}'",
                    QMessageBox.StandardButton.Ok
                )
        else:
            # Cập nhật thanh trạng thái
            if hasattr(self, 'status_label'):
                self.status_label.setText(f"Không tìm thấy bài hát nào phù hợp với từ khóa '{search_text}'")
                self.status_label.setStyleSheet("""
                    QLabel {
                        background-color: #ffebee;
                        color: #c62828;
                        padding: 8px;
                        border-radius: 4px;
                        font-size: 13px;
                        border: 1px solid #ffcdd2;
                    }
                """)
            else:
                # Hiển thị thông báo nếu không tìm thấy kết quả
                QMessageBox.information(
                    self,
                    "Kết quả tìm kiếm",
                    f"Không tìm thấy bài hát nào phù hợp với từ khóa '{search_text}'",
                    QMessageBox.StandardButton.Ok
                )
            
            # Hiển thị lại toàn bộ danh sách
            self.load_danh_sach_bai_hat()
        
    def them_bai_hat(self):
        try:
            # Tạo dialog thêm bài hát và truyền self làm parent
            dialog = GUIThemBaiHatDSPHT(ma_danh_sach=self.ma_danh_sach, parent=self)
            
            # Kết nối signal với slot để cập nhật dữ liệu
            dialog.dataChanged.connect(self.load_danh_sach_bai_hat)
            
            # Đặt vị trí trung tâm so với cửa sổ cha
            self.centerChildDialog(dialog)
            
            # Hiển thị dialog
            result = dialog.exec()
            
            # Xử lý kết quả nếu cần
            if result == QDialog.DialogCode.Accepted:
                # Nếu thêm thành công, cập nhật lại dữ liệu
                self.load_danh_sach_bai_hat()
        
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Lỗi khi mở dialog thêm bài hát: {str(e)}")
            print(f"Lỗi khi mở dialog thêm bài hát: {e}")
        
    def centerChildDialog(self, child_dialog):
        """Đặt dialog con ở giữa dialog cha"""
        # Lấy kích thước và vị trí của dialog cha
        parent_geom = self.geometry()
        parent_center = parent_geom.center()
        
        # Lấy kích thước của dialog con
        child_size = child_dialog.sizeHint()
        
        # Tính toán vị trí để dialog con ở giữa dialog cha
        child_x = parent_center.x() - child_size.width() // 2
        child_y = parent_center.y() - child_size.height() // 2
        
        # Đặt vị trí cho dialog con
        child_dialog.setGeometry(child_x, child_y, child_size.width(), child_size.height())
    
    def lam_moi_danh_sach(self):
        self.table.clearContents()
        self.table.setRowCount(0)
        self.danh_sach_nhac = self.bll.lay_danh_sach_bai_hat_theo_ma_danh_sach(self.ma_danh_sach)
        self.load_danh_sach_bai_hat()
    
    def sua_danh_sach(self):
        try:
            # Tạo dialog chỉnh sửa với mã danh sách hiện tại
            dialog = GUIChinhSuaDanhSachPhatHeThong(ma_danh_sach=self.ma_danh_sach, parent=self)
            
            # Đặt vị trí trung tâm so với cửa sổ cha
            self.centerChildDialog(dialog)
            
            # Hiển thị dialog dạng modal để chặn tương tác với cửa sổ chính
            result = dialog.exec()
            
            # Xử lý kết quả nếu cần
            if result == QDialog.DialogCode.Accepted:
                print("Đã chỉnh sửa danh sách phát thành công!")
                self.danh_sach = self.bll.lay_danh_sach_phat_he_thong_theo_ma(self.ma_danh_sach)
                self.desc_label.setText(self.danh_sach.MoTa)
                self.title_label.setText(self.danh_sach.TieuDe)
                pixmap = self._load_image(self.danh_sach.Anh)
                if pixmap:
                    self.image_label.setPixmap(pixmap)
                else:
                    self.image_label.setText("No Image")
                    self.image_label.setStyleSheet("background-color: #f0f0f0; border-radius: 10px;")
    
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Lỗi khi mở dialog chỉnh sửa: {str(e)}")
            print(f"Lỗi khi mở dialog chỉnh sửa: {e}")
            
    def xoa_bai_hat(self, id_bai_hat):
        # Xác nhận và xóa bài hát
        print(f"Xóa bài hát có ID: {id_bai_hat}")
        
        # Tìm thông tin bài hát
        ten_bai_hat = ""
        anh_bai_hat = None
        
        for bai_hat in self.danh_sach_nhac:
            if bai_hat.getMaBaiHat() == id_bai_hat:
                ten_bai_hat = bai_hat.getTieuDe()
                anh_bai_hat = bai_hat.getAnh()
                break
        
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
        content = QLabel(f'Bạn có chắc chắn muốn xóa bài hát "{ten_bai_hat}" khỏi danh sách phát không?\n\nHành động này không thể hoàn tác.')
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
            print(f"Xác nhận xóa bài hát ID: {id_bai_hat}")
            
            try:
                result = self.bll.xoa_bai_hat_khoi_danh_sach(self.ma_danh_sach, id_bai_hat)
                
                if result:
                    self.danh_sach_nhac = [bh for bh in self.danh_sach_nhac if bh.getMaBaiHat() != id_bai_hat]
                    
                    self.load_danh_sach_bai_hat()
                    
                    QMessageBox.information(
                        self,
                        "Xóa bài hát thành công",
                        f"Đã xóa bài hát khỏi danh sách phát.",
                        QMessageBox.StandardButton.Ok
                    )
                else:
                    QMessageBox.warning(
                        self,
                        "Xóa bài hát thất bại",
                        f"Không thể xóa bài hát khỏi danh sách phát. Vui lòng thử lại.",
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
            print(f"Hủy xóa bài hát ID: {id_bai_hat}")
        
    def _load_image(self, image_path, width=120, height=120):
        """Tải ảnh từ đường dẫn, trả về QPixmap đã được scale"""
        default_image_path = r"assets\DanhSachPhatHeThong\0.png"
        
        if image_path and os.path.exists(image_path.replace("/", "\\")):
            pixmap = QPixmap(image_path.replace("/", "\\"))
            if not pixmap.isNull():
                return pixmap.scaled(width, height, Qt.AspectRatioMode.KeepAspectRatio)
        
        # Nếu không có ảnh hoặc ảnh không tải được, sử dụng ảnh mặc định
        default_pixmap = QPixmap(default_image_path)
        if not default_pixmap.isNull():
            return default_pixmap.scaled(width, height, Qt.AspectRatioMode.KeepAspectRatio)
        
        return None  # Nếu cả hai đều không tải được
if __name__ == "__main__":
    import sys
    from PyQt6.QtWidgets import QApplication
    
    app = QApplication(sys.argv)
    
    # Khởi tạo cửa sổ với ID mẫu (ví dụ: 1)
    window = GUIChiTietDanhSachPhatHeThong(1)
    window.show()
    
    sys.exit(app.exec())