import sys
import os

from datetime import datetime, date
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt, pyqtSignal
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from BLL.BLLQuanLyDanhSachPhatHeThong import BLLQuanLyDanhSachPhatHeThong

class GUIThemBaiHatDSPHT(QDialog):
    dataChanged = pyqtSignal(bool)
    
    def __init__(self, ma_danh_sach=None, parent=None):
        super().__init__(parent)
        self.ma_danh_sach = ma_danh_sach
        self.bll = BLLQuanLyDanhSachPhatHeThong()
        self.is_data_changed = False
        self.danh_sach_bai_hat = []
        self.danh_sach_da_chon = []
        
        self.setupUI()
        
        self.loadDanhSachBaiHat()
        self.setupCombobox(self.search_type)

    def setupUI(self):
        # Thiết lập tiêu đề và kích thước
        self.setWindowTitle("Thêm bài hát vào Danh sách phát")
        self.setMinimumSize(800, 600)
        
        # Layout chính
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(20)
        
        # Tiêu đề
        title_label = QLabel("🎶Thêm bài hát vào Danh sách phát")
        title_label.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("color: #2196F3; margin-bottom: 20px;")
        main_layout.addWidget(title_label)
        
        # Widget tìm kiếm
        search_widget = QWidget()
        search_layout = QHBoxLayout(search_widget)
        search_layout.setContentsMargins(0, 0, 0, 0)
        
        search_label = QLabel("Tìm kiếm:")
        search_label.setFont(QFont("Arial", 12))
        search_layout.addWidget(search_label)
        
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Nhập tên bài hát hoặc ca sĩ...")
        self.search_input.setFont(QFont("Arial", 12))
        self.search_input.textChanged.connect(self.filterDanhSach)
        search_layout.addWidget(self.search_input, 1)  # 1 là stretch factor
        
        self.search_type = QComboBox()
        self.search_type.setFont(QFont("Arial", 12))
        self.search_type.setStyleSheet("""
            QComboBox {
                border: 1px solid #ddd;
                border-radius: 4px;
                padding: 6px;
                min-width: 120px;
            }
            QComboBox:hover {
                border: 1px solid #2196F3;
            }
            QComboBox::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: center right;
                width: 20px;
            }
            QComboBox QAbstractItemView {
                border: 1px solid #ddd;
                selection-background-color: #2196F3;
                selection-color: white;
            }
        """)
        self.search_type.currentIndexChanged.connect(self.filterDanhSach)
        search_layout.addWidget(self.search_type)
        
        main_layout.addWidget(search_widget)
        
        # Bảng danh sách bài hát
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(["ID", "Tiêu đề", "Ca sĩ", "Chọn"])
        
        # Thiết lập thuộc tính cho bảng
        self.table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.table.setAlternatingRowColors(True)
        self.table.verticalHeader().setVisible(False)
        
        # Thiết lập kích thước cột
        self.table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)  # ID
        self.table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)  # Tiêu đề
        self.table.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)  # Ca sĩ
        self.table.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeMode.ResizeToContents)  # Chọn
        
        
        
        # Thiết lập style cho bảng
        self.table.setStyleSheet("""
            QTableWidget {
                border: 1px solid #ddd;
                border-radius: 4px;
                background-color: #fff;
            }
            QTableWidget::item {
                padding: 8px;
            }
            QTableWidget::item:selected {
                background-color: #e3f2fd;
            }
            QHeaderView::section {
                background-color: #2196F3;
                color: white;
                font-weight: bold;
                padding: 8px;
                border: none;
            }
        """)
        
        main_layout.addWidget(self.table)
        
        # Hiển thị số lượng đã chọn
        self.selection_label = QLabel("Đã chọn: 0 bài hát")
        self.selection_label.setFont(QFont("Arial", 12))
        self.selection_label.setAlignment(Qt.AlignmentFlag.AlignRight)
        main_layout.addWidget(self.selection_label)
        
        # Widget chứa các nút
        button_widget = QWidget()
        button_layout = QHBoxLayout(button_widget)
        button_layout.setContentsMargins(0, 0, 0, 0)
        button_layout.setSpacing(10)
        
        # Nút chọn tất cả
        select_all_button = QPushButton("✅Chọn tất cả")
        select_all_button.setFont(QFont("Arial", 12))
        select_all_button.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #388E3C;
            }
        """)
        select_all_button.clicked.connect(self.selectAll)
        button_layout.addWidget(select_all_button)
        
        # Nút bỏ chọn tất cả
        deselect_all_button = QPushButton("❌Bỏ chọn tất cả")
        deselect_all_button.setFont(QFont("Arial", 12))
        deselect_all_button.setStyleSheet("""
            QPushButton {
                background-color: #FF9800;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #F57C00;
            }
        """)
        deselect_all_button.clicked.connect(self.deselectAll)
        button_layout.addWidget(deselect_all_button)
        
        # Nút thêm
        add_button = QPushButton("➕Thêm vào danh sách phát")
        add_button.setFont(QFont("Arial", 12, QFont.Weight.Bold))
        add_button.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #1976D2;
            }
        """)
        add_button.clicked.connect(self.addSelectedSongs)
        button_layout.addWidget(add_button)
        
        # Nút hủy
        cancel_button = QPushButton("🚫Hủy")
        cancel_button.setFont(QFont("Arial", 12))
        cancel_button.setStyleSheet("""
            QPushButton {
                background-color: #f44336;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #d32f2f;
            }
        """)
        cancel_button.clicked.connect(self.reject)
        button_layout.addWidget(cancel_button)
        
        main_layout.addWidget(button_widget)
        
        
    def loadDanhSachBaiHat(self):
        # Xóa dữ liệu cũ
        self.table.setRowCount(0)
        self.danh_sach_bai_hat = []
        self.danh_sach_da_chon = []
        
        try:
            # Lấy danh sách bài hát chưa có trong danh sách phát
            if self.ma_danh_sach:
                self.danh_sach_bai_hat = self.bll.lay_bai_hat_chua_co_trong_danh_sach(self.ma_danh_sach)
            else:
                # Nếu không có mã danh sách, lấy tất cả bài hát
                self.danh_sach_bai_hat = self.bll.lay_tat_ca_bai_hat()
            
            # Hiển thị dữ liệu lên bảng
            self.hienThiDanhSachBaiHat()
            
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Không thể tải danh sách bài hát: {str(e)}")
            # print(f"Lỗi khi tải danh sách bài hát: {e}")
    
    def hienThiDanhSachBaiHat(self, filter_text=""):
        # Xóa dữ liệu cũ
        self.table.setRowCount(0)
        # Thiết lập style cho bảng với màu nền khi chọn dòng
        self.table.setStyleSheet("""
            QTableWidget {
                border: 1px solid #ddd;
                border-radius: 4px;
                background-color: #fff;
                selection-background-color: #4CAF50;  /* Màu nền khi chọn - màu xanh lá */
                selection-color: white;               /* Màu chữ khi chọn - trắng */
            }
            QTableWidget::item:selected {
                background-color: #4CAF50;  /* Màu nền khi chọn */
                color: white;               /* Màu chữ khi chọn */
            }
            QHeaderView::section {
                background-color: #2196F3;
                color: white;
                font-weight: bold;
                padding: 8px;
                border: none;
            }
        """)
        # Lọc danh sách bài hát nếu có filter_text
        displayed_songs = []
        for bai_hat in self.danh_sach_bai_hat:
            if filter_text:
                # Lọc theo tên bài hát hoặc ca sĩ
                tieu_de = bai_hat.getTieuDe().lower()
                ca_si_text = self.getCaSiText(bai_hat).lower()
                
                if filter_text.lower() in tieu_de or filter_text.lower() in ca_si_text:
                    displayed_songs.append(bai_hat)
            else:
                displayed_songs.append(bai_hat)
        
        # Điều chỉnh số cột nếu bạn thêm cột ảnh
        self.table.setColumnCount(5)  # Tăng lên 5 cột: ID, Ảnh, Tiêu đề, Ca sĩ, Checkbox
        self.table.setHorizontalHeaderLabels(["ID", "Ảnh", "Tiêu đề", "Ca sĩ", "Chọn"])
        
        # Thiết lập lại kích thước cột
        self.table.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)  # ID
        self.table.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)  # Ảnh
        self.table.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeMode.Stretch)  # Tiêu đề
        self.table.horizontalHeader().setSectionResizeMode(3, QHeaderView.ResizeMode.Stretch)  # Ca sĩ
        self.table.horizontalHeader().setSectionResizeMode(4, QHeaderView.ResizeMode.ResizeToContents)  # Checkbox
        
        # Thiết lập chiều cao dòng để phù hợp với ảnh
        self.table.verticalHeader().setDefaultSectionSize(125)  
        
        # Thiết lập số dòng
        self.table.setRowCount(len(displayed_songs))
        
        # Hiển thị dữ liệu
        for row, bai_hat in enumerate(displayed_songs):
            # ID
            id_item = QTableWidgetItem(f"#{bai_hat.getMaBaiHat()}")
            id_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            id_item.setFont(QFont("Arial", 10, QFont.Weight.Bold))
            self.table.setItem(row, 0, id_item)
            
            # Ảnh (cột mới)
            label = QLabel()
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            
            # Tải và hiển thị ảnh
            anh_path = bai_hat.getAnh()
            if anh_path != None:
                image_path = anh_path.replace("/", "\\")
                # print(f"Đang tải ảnh từ: {image_path}")
                
                if image_path.startswith("\\") or image_path.startswith("..") or image_path.startswith(".\\") or image_path.startswith("./"):
                    current_dir = os.path.dirname(os.path.abspath(__file__))
                    project_root = os.path.dirname(os.path.dirname(current_dir))
                    
                    if image_path.startswith("\\"):
                        image_path = image_path[1:]  
                        image_path = os.path.normpath(os.path.join(project_root, image_path))
                    else:
                        image_path = os.path.normpath(os.path.join(current_dir, image_path))
                    # print(f"Đường dẫn đã xử lý: {image_path}")
                    pixmap = QPixmap(image_path)
                    label.setPixmap(pixmap.scaled(120, 120, Qt.AspectRatioMode.KeepAspectRatio))
                    if pixmap.isNull():
                        # print(f"Không thể tải ảnh từ đường dẫn: {image_path}")
                        self._them_anh_mac_dinh(label)
            else:
                self._them_anh_mac_dinh(label)
            self.table.setCellWidget(row, 1, label)
            
            # Tiêu đề
            tieu_de_item = QTableWidgetItem(bai_hat.getTieuDe())
            tieu_de_item.setFont(QFont("Arial", 11))
            self.table.setItem(row, 2, tieu_de_item)
            
            # Ca sĩ
            ca_si_text = self.getCaSiText(bai_hat)
            ca_si_item = QTableWidgetItem(ca_si_text)
            ca_si_item.setFont(QFont("Arial", 11))
            self.table.setItem(row, 3, ca_si_item)
            
            # Checkbox
            checkbox_widget = QWidget()
            checkbox_layout = QHBoxLayout(checkbox_widget)
            checkbox_layout.setContentsMargins(5, 5, 5, 5)
            checkbox_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
            
            checkbox = QCheckBox()
            # Kiểm tra xem bài hát đã được chọn chưa
            if bai_hat.getMaBaiHat() in self.danh_sach_da_chon:
                checkbox.setChecked(True)
            
            # Kết nối checkbox với handler
            checkbox.stateChanged.connect(lambda state, bh=bai_hat: self.onCheckboxChanged(state, bh))
            
            checkbox_layout.addWidget(checkbox)
            self.table.setCellWidget(row, 4, checkbox_widget)
        
        # Cập nhật số lượng bài hát
        self.updateSelectionCount()
        
    def _them_anh_mac_dinh(self, label):
        """Thêm ảnh mặc định vào label"""
        default_image = r"assets\AnhBaiHat\0.png"
        # print(f"Sử dụng ảnh mặc định: {default_image}")
        pixmap = QPixmap(default_image)
        
        if pixmap.isNull():
            # print(f"Không thể tải ảnh mặc định")
            label.setText("No Image")
        else:
            pixmap = pixmap.scaled(80, 80, Qt.AspectRatioMode.KeepAspectRatio)
            # print(pixmap.size())
            label.setPixmap(pixmap)
    
    def getCaSiText(self, bai_hat):
        """Lấy danh sách tên ca sĩ của bài hát"""
        ca_si_names = []
        if bai_hat.getCaSi():
            for ca_si in bai_hat.getCaSi():
                if isinstance(ca_si, dict) and "TenCaSi" in ca_si:
                    ca_si_names.append(ca_si["TenCaSi"])
                elif hasattr(ca_si, "TenCaSi"):
                    ca_si_names.append(ca_si.TenCaSi)
        
        return ", ".join(ca_si_names) if ca_si_names else "Không có thông tin"
    
    def updateSelectionCount(self):
        """Cập nhật số lượng bài hát đã chọn"""
        count = len(self.danh_sach_da_chon)
        self.selection_label.setText(f"Đã chọn: {count} bài hát")
    
    def onCheckboxChanged(self, state, bai_hat):
        """Xử lý khi checkbox thay đổi trạng thái"""
        ma_bai_hat = bai_hat.getMaBaiHat()
        self.danh_sach_da_chon.append(ma_bai_hat)
        
        if int(state) == 2:
            # Thêm vào danh sách đã chọn nếu chưa có
            if ma_bai_hat not in self.danh_sach_da_chon:
                self.danh_sach_da_chon.append(ma_bai_hat)
        else:
            # Xóa khỏi danh sách đã chọn nếu có
            if ma_bai_hat in self.danh_sach_da_chon:
                self.danh_sach_da_chon.remove(ma_bai_hat)
        # Cập nhật số lượng đã chọn
        self.updateSelectionCount()
    
    def filterDanhSach(self):
        """Lọc danh sách bài hát theo từ khóa tìm kiếm"""
        filter_text = self.search_input.text().strip()
        self.hienThiDanhSachBaiHat(filter_text)
    
    def selectAll(self):
        """Chọn tất cả bài hát"""
        # Lấy tất cả ID bài hát hiện có
        for bai_hat in self.danh_sach_bai_hat:
            ma_bai_hat = bai_hat.getMaBaiHat()
            if ma_bai_hat not in self.danh_sach_da_chon:
                self.danh_sach_da_chon.append(ma_bai_hat)
        # Cập nhật lại giao diện
        current_filter = self.search_input.text().strip()
        self.hienThiDanhSachBaiHat(current_filter)
    
    def deselectAll(self):
        # bỏ chọn tất cả
        # Lấy tất cả ID bài hát hiện có
        for bai_hat in self.danh_sach_bai_hat:
            ma_bai_hat = bai_hat.getMaBaiHat()
            if ma_bai_hat in self.danh_sach_da_chon:
                self.danh_sach_da_chon.remove(ma_bai_hat)
        # Cập nhật lại giao diện
        current_filter = self.search_input.text().strip()
        self.hienThiDanhSachBaiHat(current_filter)
                
    def setupCombobox(self, combobox):
        # Thêm mục mặc định - tất cả ca sĩ
        combobox.addItem("Tất cả ca sĩ")
        
        # Tạo danh sách ca sĩ không trùng lặp
        ds_ca_si = []
        for bai_hat in self.danh_sach_bai_hat:
            for ca_si in bai_hat.getCaSi():
                if ca_si["TenCaSi"] not in ds_ca_si:
                    ds_ca_si.append(ca_si["TenCaSi"])
        
        # Sắp xếp danh sách ca sĩ theo thứ tự abc
        ds_ca_si.sort()
        
        # Thêm vào combobox
        combobox.addItems(ds_ca_si)
        
        # Kết nối signal - QUAN TRỌNG: Sử dụng lambda để truyền tham chiếu hàm
        combobox.currentIndexChanged.connect(lambda: self.filterDanhSachCBB(combobox))

    def filterDanhSachCBB(self, combobox):
        # Lấy text hiện tại của combobox
        selected_text = combobox.currentText()
        
        # Nếu là "Tất cả ca sĩ" thì hiển thị toàn bộ
        if selected_text == "Tất cả ca sĩ":
            self.hienThiDanhSachBaiHat("")
        else:
            # Lọc theo ca sĩ đã chọn
            self.hienThiDanhSachBaiHat(selected_text)
        
        # Cập nhật tiêu đề
        if selected_text != "Tất cả ca sĩ":
            self.setWindowTitle(f"Thêm bài hát - Lọc theo ca sĩ: {selected_text}")

    def accept(self):
        if self.is_data_changed:
            self.dataChanged.emit(True)
        super().accept()
    
    def reject(self):
        super().reject()
        
    def addSelectedSongs(self):
        """Thêm các bài hát đã chọn vào danh sách phát"""
        if not self.ma_danh_sach:
            QMessageBox.warning(self, "Cảnh báo", "Không có thông tin danh sách phát!")
            return
        
        if not self.danh_sach_da_chon:
            QMessageBox.warning(self, "Cảnh báo", "Vui lòng chọn ít nhất một bài hát!")
            return
        
        try:
            # Gọi hàm từ BLL để thêm bài hát
            success_count, failed_count = self.bll.them_bai_hat_vao_danh_sach(self.ma_danh_sach, self.danh_sach_da_chon)
            
            # Hiển thị thông báo kết quả
            if success_count > 0:
                QMessageBox.information(
                    self,
                    "Thành công",
                    f"Đã thêm {success_count}/{len(self.danh_sach_da_chon)} bài hát vào danh sách phát."
                )
                
                # Đánh dấu dữ liệu đã thay đổi
                self.is_data_changed = True
                # Phát signal thông báo dữ liệu đã thay đổi
                self.dataChanged.emit(True)
                # Đóng dialog với kết quả là Accepted
                self.accept()
            else:
                if failed_count > 0:
                    QMessageBox.warning(
                        self,
                        "Thất bại",
                        f"Không thể thêm bài hát vào danh sách phát. {failed_count} bài hát thất bại."
                    )
                else:
                    QMessageBox.information(
                        self,
                        "Thông báo",
                        "Không có bài hát nào được thêm vào danh sách phát."
                    )
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Đã xảy ra lỗi khi thêm bài hát: {str(e)}")
            print(f"Lỗi khi thêm bài hát: {e}")
    
if __name__ == "__main__":
    import sys
    from PyQt6.QtWidgets import QApplication
    
    app = QApplication(sys.argv)
    
    # Khởi tạo cửa sổ với ID mẫu (ví dụ: 1)
    window = GUIThemBaiHatDSPHT(1)
    window.show()
    
    sys.exit(app.exec())