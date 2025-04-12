from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, 
                          QHBoxLayout, QApplication, QScrollArea, QWidget, QListWidget, 
                          QListWidgetItem, QFrame, QGridLayout, QSizePolicy, QTabWidget)
from PyQt6.QtGui import QPixmap, QFont, QIcon, QColor
from PyQt6.QtCore import Qt, QSize
import os
import sys
import datetime  # Thêm import cho datetime

# Thêm đường dẫn cha vào sys.path để import các module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

class GUIXemThongTinCaSi(QDialog):
    def __init__(self, parent=None, ca_si=None, danh_sach_bai_hat=None):
        super().__init__(parent)
        self.ca_si = ca_si
        self.danh_sach_bai_hat = danh_sach_bai_hat if danh_sach_bai_hat else []
        
        # Thiết lập cửa sổ
        self.setWindowTitle(f"Thông Tin Ca Sĩ - {ca_si.getNgheDanh() if ca_si else ''}")
        self.setMinimumSize(700, 600)
        
        # Thiết lập style chung
        self.setStyleSheet("""
            QDialog {
                background-color: #f5f5f5;
                font-size: 16px;
            }
            QLabel {
                font-size: 16px;
            }
            QTabWidget::pane {
                border: 1px solid #ccc;
                border-radius: 5px;
                padding: 5px;
                background: white;
            }
            QTabBar::tab {
                font-size: 16px;
                background: #e0e0e0;
                border: 1px solid #c0c0c0;
                border-bottom: none;
                border-top-left-radius: 6px;
                border-top-right-radius: 6px;
                padding: 8px 15px;
                margin-right: 2px;
            }
            QTabBar::tab:selected {
                background: #1db954;
                color: white;
                font-weight: bold;
            }
            QTabBar::tab:hover:!selected {
                background: #d0d0d0;
            }
            QListWidget {
                font-size: 16px;
                border: none;
                background-color: white;
            }
            QListWidget::item {
                border-bottom: 1px solid #eee;
                min-height: 80px; /* Tăng chiều cao tối thiểu của hàng */
            }
            QListWidget::item:selected {
                background-color: #e8f5e9;
                color: #1db954;
            }
            QListWidget::item:hover {
                background-color: #f5f5f5;
            }
        """)
        
        self.initUI()
    
    def initUI(self):
        # Layout chính
        main_layout = QVBoxLayout()
        main_layout.setSpacing(15)
        
        # ===== PHẦN THÔNG TIN CHÍNH =====
        info_layout = QHBoxLayout()
        
        # Ảnh ca sĩ
        self.artist_image_container = QLabel()
        self.artist_image_container.setFixedSize(200, 200)
        self.artist_image_container.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.artist_image_container.setStyleSheet("""
            background-color: white;
            border: 2px solid #ddd;
        """)
        
        # Nạp ảnh ca sĩ nếu có
        if self.ca_si:
            image_path = self.get_artist_image_path(self.ca_si)
            if image_path and os.path.exists(image_path):
                pixmap = QPixmap(image_path)
                pixmap = pixmap.scaled(190, 190, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
                self.artist_image_container.setPixmap(pixmap)
            else:
                self.artist_image_container.setText("Không có ảnh")
        
        info_layout.addWidget(self.artist_image_container)
        
        # Thông tin chi tiết
        detail_layout = QVBoxLayout()
        
        # Nghệ danh (tên hiển thị)
        nghe_danh = ""
        if self.ca_si and hasattr(self.ca_si, 'getNgheDanh') and callable(getattr(self.ca_si, 'getNgheDanh')):
            nghe_danh = self.ca_si.getNgheDanh()
            
        self.label_nghe_danh = QLabel(nghe_danh)
        self.label_nghe_danh.setStyleSheet("font-size: 28px; font-weight: bold; color: #333;")
        detail_layout.addWidget(self.label_nghe_danh)
        
        # Tên thật
        ten_that_layout = QHBoxLayout()
        ten_that_title = QLabel("Tên thật:")
        ten_that_title.setStyleSheet("font-weight: bold; color: #666;")
        ten_that_title.setFixedWidth(100)
        
        ten_that = ""
        if self.ca_si and hasattr(self.ca_si, 'getTenCaSi') and callable(getattr(self.ca_si, 'getTenCaSi')):
            ten_that = self.ca_si.getTenCaSi()
        elif self.ca_si and hasattr(self.ca_si, 'getTen') and callable(getattr(self.ca_si, 'getTen')):
            ten_that = self.ca_si.getTen()
            
        self.label_ten_that = QLabel(ten_that)
        ten_that_layout.addWidget(ten_that_title)
        ten_that_layout.addWidget(self.label_ten_that)
        detail_layout.addLayout(ten_that_layout)
        
        # Mã ca sĩ
        ma_ca_si_layout = QHBoxLayout()
        ma_ca_si_title = QLabel("Mã ca sĩ:")
        ma_ca_si_title.setStyleSheet("font-weight: bold; color: #666;")
        ma_ca_si_title.setFixedWidth(100)
        
        ma_ca_si = ""
        if self.ca_si and hasattr(self.ca_si, 'getMaCaSi') and callable(getattr(self.ca_si, 'getMaCaSi')):
            ma_ca_si = str(self.ca_si.getMaCaSi())
            
        self.label_ma_ca_si = QLabel(ma_ca_si)
        ma_ca_si_layout.addWidget(ma_ca_si_title)
        ma_ca_si_layout.addWidget(self.label_ma_ca_si)
        detail_layout.addLayout(ma_ca_si_layout)
        
        # Ngày sinh
        ngay_sinh_layout = QHBoxLayout()
        ngay_sinh_title = QLabel("Ngày sinh:")
        ngay_sinh_title.setStyleSheet("font-weight: bold; color: #666;")
        ngay_sinh_title.setFixedWidth(100)
        
        # Xử lý ngày sinh, có thể là datetime.date hoặc chuỗi
        ngay_sinh_text = ""
        if self.ca_si and hasattr(self.ca_si, 'getNgaySinh') and callable(getattr(self.ca_si, 'getNgaySinh')):
            ngay_sinh = self.ca_si.getNgaySinh()
            if isinstance(ngay_sinh, datetime.date):
                ngay_sinh_text = ngay_sinh.strftime("%d/%m/%Y")
            elif ngay_sinh:
                ngay_sinh_text = str(ngay_sinh)
                
        self.label_ngay_sinh = QLabel(ngay_sinh_text)
        ngay_sinh_layout.addWidget(ngay_sinh_title)
        ngay_sinh_layout.addWidget(self.label_ngay_sinh)
        detail_layout.addLayout(ngay_sinh_layout)
        
        # Số lượng bài hát
        so_luong_layout = QHBoxLayout()
        so_luong_title = QLabel("Số bài hát:")
        so_luong_title.setStyleSheet("font-weight: bold; color: #666;")
        so_luong_title.setFixedWidth(100)
        
        so_bai_hat = 0
        if self.ca_si and self.danh_sach_bai_hat and hasattr(self.ca_si, 'getMaCaSi') and callable(getattr(self.ca_si, 'getMaCaSi')):
            ma_ca_si = self.ca_si.getMaCaSi()
            ma_ca_si_str = str(ma_ca_si)  # Chuyển mã ca sĩ sang chuỗi để so sánh
            
            # Cũng lấy nghệ danh để so sánh thêm
            nghe_danh = ""
            if hasattr(self.ca_si, 'getNgheDanh') and callable(getattr(self.ca_si, 'getNgheDanh')):
                nghe_danh = self.ca_si.getNgheDanh()
            
            for bai_hat in self.danh_sach_bai_hat:
                if hasattr(bai_hat, 'getCaSi') and callable(getattr(bai_hat, 'getCaSi')):
                    ca_si_bai_hat = bai_hat.getCaSi()
                    
                    # Nếu ca_si_bai_hat là một danh sách
                    if isinstance(ca_si_bai_hat, list):
                        tim_thay = False
                        
                        for ca_si_item in ca_si_bai_hat:
                            # Xử lý trường hợp '1-Sơn Tùng M-TP'
                            if isinstance(ca_si_item, str) and "-" in ca_si_item:
                                parts = ca_si_item.split("-", 1)
                                if len(parts) >= 2:
                                    item_ma = parts[0].strip()
                                    item_ten = parts[1].strip()
                                    
                                    # So sánh theo mã hoặc tên
                                    if item_ma == ma_ca_si_str or (nghe_danh and item_ten == nghe_danh):
                                        tim_thay = True
                                        break
                            # Trường hợp so sánh trực tiếp
                            elif ca_si_item == ma_ca_si or ca_si_item == nghe_danh:
                                tim_thay = True
                                break
                        
                        if tim_thay:
                            so_bai_hat += 1
                    
                    # Nếu ca_si_bai_hat là một chuỗi đơn
                    elif isinstance(ca_si_bai_hat, str):
                        # Xử lý trường hợp '1-Sơn Tùng M-TP'
                        if "-" in ca_si_bai_hat:
                            parts = ca_si_bai_hat.split("-", 1)
                            if len(parts) >= 2:
                                item_ma = parts[0].strip()
                                item_ten = parts[1].strip()
                                
                                # So sánh theo mã hoặc tên
                                if item_ma == ma_ca_si_str or (nghe_danh and item_ten == nghe_danh):
                                    so_bai_hat += 1
                        # Trường hợp so sánh trực tiếp
                        elif ca_si_bai_hat == ma_ca_si or ca_si_bai_hat == nghe_danh:
                            so_bai_hat += 1
        
        self.label_so_bai_hat = QLabel(str(so_bai_hat))
        so_luong_layout.addWidget(so_luong_title)
        so_luong_layout.addWidget(self.label_so_bai_hat)
        detail_layout.addLayout(so_luong_layout)
        
        # Mô tả
        mo_ta_layout = QVBoxLayout()
        mo_ta_title = QLabel("Tiểu sử:")
        mo_ta_title.setStyleSheet("font-weight: bold; color: #666;")
        mo_ta_layout.addWidget(mo_ta_title)
        
        mo_ta_text = ""
        if hasattr(self.ca_si, 'getMoTa') and callable(getattr(self.ca_si, 'getMoTa')):
            mo_ta_text = self.ca_si.getMoTa()
        elif hasattr(self.ca_si, 'getTieuSu') and callable(getattr(self.ca_si, 'getTieuSu')):
            mo_ta_text = self.ca_si.getTieuSu()
        elif hasattr(self.ca_si, 'TieuSu'):
            mo_ta_text = self.ca_si.TieuSu
            
        self.label_mo_ta = QLabel(mo_ta_text if mo_ta_text else "Chưa có thông tin")
        self.label_mo_ta.setWordWrap(True)
        self.label_mo_ta.setStyleSheet("line-height: 1.4;")
        mo_ta_layout.addWidget(self.label_mo_ta)
        
        detail_layout.addLayout(mo_ta_layout)
        detail_layout.addStretch()
        
        info_layout.addLayout(detail_layout, 1)  # 1 là stretch factor
        
        main_layout.addLayout(info_layout)
        
        # Phân cách
        separator = QFrame()
        separator.setFrameShape(QFrame.Shape.HLine)
        separator.setFrameShadow(QFrame.Shadow.Sunken)
        separator.setStyleSheet("background-color: #ccc;")
        main_layout.addWidget(separator)
        
        # ===== PHẦN TAB THÔNG TIN =====
        tabs = QTabWidget()
        
        # Tab Bài hát
        songs_tab = QWidget()
        songs_layout = QVBoxLayout(songs_tab)
        
        # Tiêu đề danh sách bài hát
        songs_title = QLabel("Bài hát của ca sĩ")
        songs_title.setStyleSheet("font-size: 18px; font-weight: bold; color: #333; margin-bottom: 10px;")
        songs_layout.addWidget(songs_title)
        
        # Danh sách bài hát
        self.songs_list = QListWidget()
        
        # Lọc danh sách bài hát của ca sĩ này
        if self.ca_si and self.danh_sach_bai_hat and hasattr(self.ca_si, 'getMaCaSi') and callable(getattr(self.ca_si, 'getMaCaSi')):
            ma_ca_si = self.ca_si.getMaCaSi()
            ma_ca_si_str = str(ma_ca_si)  # Chuyển mã ca sĩ sang chuỗi để so sánh
            
            # Lấy nghệ danh để so sánh thêm
            nghe_danh = ""
            if hasattr(self.ca_si, 'getNgheDanh') and callable(getattr(self.ca_si, 'getNgheDanh')):
                nghe_danh = self.ca_si.getNgheDanh()
            
            # Lọc bài hát theo mã ca sĩ
            bai_hat_ca_si = []
            for bai_hat in self.danh_sach_bai_hat:
                added = False
                
                # Kiểm tra theo getMaCaSi
                if not added and hasattr(bai_hat, 'getMaCaSi') and callable(getattr(bai_hat, 'getMaCaSi')):
                    ma_ca_si_bai_hat = bai_hat.getMaCaSi()
                    
                    if isinstance(ma_ca_si_bai_hat, list) and ma_ca_si in ma_ca_si_bai_hat:
                        bai_hat_ca_si.append(bai_hat)
                        added = True
                    elif ma_ca_si == ma_ca_si_bai_hat:
                        bai_hat_ca_si.append(bai_hat)
                        added = True
                
                # Kiểm tra theo getCaSi nếu chưa thêm
                if not added and hasattr(bai_hat, 'getCaSi') and callable(getattr(bai_hat, 'getCaSi')):
                    ca_si_bai_hat = bai_hat.getCaSi()
                    
                    # Nếu ca_si_bai_hat là một danh sách
                    if isinstance(ca_si_bai_hat, list):
                        for ca_si_item in ca_si_bai_hat:
                            # Xử lý trường hợp '1-Sơn Tùng M-TP'
                            if isinstance(ca_si_item, str) and "-" in ca_si_item:
                                parts = ca_si_item.split("-", 1)
                                if len(parts) >= 2:
                                    item_ma = parts[0].strip()
                                    item_ten = parts[1].strip()
                                    
                                    # So sánh theo mã hoặc tên
                                    if item_ma == ma_ca_si_str or (nghe_danh and item_ten == nghe_danh):
                                        bai_hat_ca_si.append(bai_hat)
                                        added = True
                                        break
                            # Trường hợp so sánh trực tiếp
                            elif ca_si_item == ma_ca_si or (nghe_danh and ca_si_item == nghe_danh):
                                bai_hat_ca_si.append(bai_hat)
                                added = True
                                break
                        
                    # Nếu ca_si_bai_hat là một chuỗi đơn
                    elif isinstance(ca_si_bai_hat, str):
                        # Xử lý trường hợp '1-Sơn Tùng M-TP'
                        if "-" in ca_si_bai_hat:
                            parts = ca_si_bai_hat.split("-", 1)
                            if len(parts) >= 2:
                                item_ma = parts[0].strip()
                                item_ten = parts[1].strip()
                                
                                # So sánh theo mã hoặc tên
                                if item_ma == ma_ca_si_str or (nghe_danh and item_ten == nghe_danh):
                                    bai_hat_ca_si.append(bai_hat)
                                    added = True
                        # Trường hợp so sánh trực tiếp
                        elif ca_si_bai_hat == ma_ca_si or (nghe_danh and ca_si_bai_hat == nghe_danh):
                            bai_hat_ca_si.append(bai_hat)
                            added = True
            
            # Hiển thị danh sách bài hát
            for bai_hat in bai_hat_ca_si:
                song_item = QListWidgetItem()
                
                # Tạo layout cho mỗi item
                item_widget = QWidget()
                item_layout = QHBoxLayout(item_widget)
                item_layout.setContentsMargins(5, 5, 5, 5)
                
                # Lấy đường dẫn ảnh bài hát
                image_path = self.get_song_image_path(bai_hat)
                
                # Tạo và hiển thị ảnh bài hát
                song_image = QLabel()
                song_image.setFixedSize(100, 100)
                if image_path and os.path.exists(image_path):
                    pixmap = QPixmap(image_path)
                    pixmap = pixmap.scaled(100, 100, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
                    song_image.setPixmap(pixmap)
                    song_image.setStyleSheet("border-radius: 4px;")
                else:
                    # Tạo placeholder nếu không có ảnh
                    song_image.setStyleSheet("background-color: #e0e0e0; border-radius: 4px;")
                
                item_layout.addWidget(song_image)
                
                # Thông tin bài hát
                song_info_layout = QVBoxLayout()
                
                # Tiêu đề bài hát
                tieu_de = ""
                if hasattr(bai_hat, 'getTieuDe') and callable(getattr(bai_hat, 'getTieuDe')):
                    tieu_de = bai_hat.getTieuDe()
                    
                song_title = QLabel(tieu_de)
                song_title.setStyleSheet("font-weight: bold; font-size: 16px;")
                song_info_layout.addWidget(song_title)
                
                # Thêm thông tin thời lượng nếu có
                if hasattr(bai_hat, 'getThoiLuong') and callable(getattr(bai_hat, 'getThoiLuong')):
                    thoi_luong = bai_hat.getThoiLuong()
                    duration_label = QLabel(f"Thời lượng: {thoi_luong}")
                    duration_label.setStyleSheet("color: #666; font-size: 14px;")
                    song_info_layout.addWidget(duration_label)
                
                item_layout.addLayout(song_info_layout, 1)  # 1 là stretch factor
                
                # Nút phát
                play_button = QPushButton()
                play_button.setIcon(QIcon(os.path.join(os.path.dirname(__file__), "../../assets/icon/play-button.png")))
                play_button.setIconSize(QSize(20, 20))
                play_button.setFixedSize(35, 35)
                play_button.setStyleSheet("""
                    QPushButton {
                        background-color: #1DB954;
                        color: white;
                        border-radius: 15px;
                        padding: 5px;
                    }
                    QPushButton:hover {
                        background-color: #1ED760;
                    }
                """)
                play_button.setCursor(Qt.CursorShape.PointingHandCursor)
                play_button.clicked.connect(lambda checked=False, s=bai_hat: self.play_song(s))
                
                item_layout.addWidget(play_button)
                
                # Thiết lập kích thước cho item và widget
                song_item.setSizeHint(item_widget.sizeHint())
                self.songs_list.addItem(song_item)
                self.songs_list.setItemWidget(song_item, item_widget)
        
        songs_layout.addWidget(self.songs_list)
        tabs.addTab(songs_tab, "Bài Hát")
        
        # # Tab thông tin thêm (có thể mở rộng sau)
        # more_info_tab = QWidget()
        # more_layout = QVBoxLayout(more_info_tab)
        
        # # Thêm một số thông tin khác nếu có
        # more_title = QLabel("Thông tin thêm")
        # more_title.setStyleSheet("font-size: 18px; font-weight: bold; color: #333;")
        # more_layout.addWidget(more_title)
        
        # more_content = QLabel("Thông tin chi tiết thêm về ca sĩ sẽ được cập nhật sau.")
        # more_content.setWordWrap(True)
        # more_layout.addWidget(more_content)
        # more_layout.addStretch()
        
        # tabs.addTab(more_info_tab, "Thông Tin Thêm")
        
        main_layout.addWidget(tabs)
        
        # ===== PHẦN NÚT ĐIỀU KHIỂN =====
        button_layout = QHBoxLayout()
        
        close_button = QPushButton("Đóng")
        close_button.setStyleSheet("""
            QPushButton {
                background-color: #f44336;
                color: white;
                font-weight: bold;
                padding: 8px 15px;
                border-radius: 5px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #ff5722;
            }
        """)
        close_button.clicked.connect(self.close)
        
        button_layout.addStretch()
        button_layout.addWidget(close_button)
        
        main_layout.addLayout(button_layout)
        
        self.setLayout(main_layout)
    
    def play_song(self, song):
        """Xử lý khi người dùng nhấn nút phát bài hát"""
        print(f"Đang phát bài hát: {song.getTieuDe()}")
        # TODO: Thêm code để phát nhạc thực tế ở đây
    
    def get_artist_image_path(self, ca_si):
        """Lấy đường dẫn ảnh ca sĩ từ thuộc tính của đối tượng"""
        try:
            # Tạo đường dẫn tuyệt đối từ đường dẫn tương đối
            base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
            
            # Kiểm tra xem đối tượng có phương thức getAnh không
            if hasattr(ca_si, 'getAnhCaSi') and callable(getattr(ca_si, 'getAnhCaSi')):
                anh_path = ca_si.getAnhCaSi()
                
                if anh_path:
                    # Xử lý đường dẫn để loại bỏ dấu / ở đầu nếu có
                    if anh_path.startswith('/'):
                        anh_path = anh_path[1:]
                        
                    # Tạo đường dẫn tuyệt đối từ gốc dự án
                    full_path = os.path.join(base_dir, anh_path)
                    
                    if os.path.exists(full_path):
                        return full_path
                
                # Thử tìm trong thư mục assets của dự án
                default_img = os.path.join(base_dir, "assets", "CaSi", f"{ca_si.getMaCaSi()}.png")
                if os.path.exists(default_img):
                    return default_img
            
            # Nếu có AnhCaSi và không có getAnh
            if hasattr(ca_si, 'AnhCaSi') and ca_si.AnhCaSi:
                anh_path = ca_si.AnhCaSi
                
                if anh_path.startswith('/'):
                    anh_path = anh_path[1:]
                
                full_path = os.path.join(base_dir, anh_path)
                if os.path.exists(full_path):
                    return full_path
                
            # Đường dẫn dự phòng
            return os.path.join(base_dir, "assets", "CaSi", "0.png")
            
        except Exception as e:
            print(f"Lỗi khi lấy ảnh ca sĩ: {e}")
            # Trả về đường dẫn ảnh mặc định
            base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
            return os.path.join(base_dir, "assets", "CaSi", "0.png")
        
    def get_song_image_path(self, bai_hat):
        """Lấy đường dẫn ảnh bài hát từ thuộc tính của đối tượng"""
        try:
            # Tạo đường dẫn tuyệt đối từ đường dẫn tương đối
            base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
            
            # Kiểm tra xem đối tượng có phương thức getAnh không
            if hasattr(bai_hat, 'getAnh') and callable(getattr(bai_hat, 'getAnh')):
                anh_path = bai_hat.getAnh()
                
                if anh_path:
                    # Xử lý đường dẫn để loại bỏ dấu / ở đầu nếu có
                    if anh_path.startswith('/'):
                        anh_path = anh_path[1:]
                        
                    # Tạo đường dẫn tuyệt đối từ gốc dự án
                    full_path = os.path.join(base_dir, anh_path)
                    
                    if os.path.exists(full_path):
                        return full_path
                
                # Thử tìm trong thư mục assets của dự án
                if hasattr(bai_hat, 'getMaBaiHat') and callable(getattr(bai_hat, 'getMaBaiHat')):
                    default_img = os.path.join(base_dir, "assets", "AnhBaiHat", f"{bai_hat.getMaBaiHat()}.png")
                    if os.path.exists(default_img):
                        return default_img
            
            # Nếu có AnhBaiHat và không có getAnh
            if hasattr(bai_hat, 'AnhBaiHat') and bai_hat.AnhBaiHat:
                anh_path = bai_hat.AnhBaiHat
                
                if anh_path.startswith('/'):
                    anh_path = anh_path[1:]
                
                full_path = os.path.join(base_dir, anh_path)
                if os.path.exists(full_path):
                    return full_path
                
            # Đường dẫn dự phòng
            return os.path.join(base_dir, "assets", "AnhBaiHat", "0.png")
            
        except Exception as e:
            print(f"Lỗi khi lấy ảnh bài hát: {e}")
            # Trả về đường dẫn ảnh mặc định
            base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
            return os.path.join(base_dir, "assets", "AnhBaiHat", "0.png")

# Sửa lại hàm main để có thể thử nghiệm độc lập
if __name__ == "__main__":
    import sys
    from BLL.BLLQuanLy import BLLQuanLy
    
    app = QApplication(sys.argv)
    bll = BLLQuanLy()
    danh_sach_ca_si = bll.layDanhSachCaSi()
    danh_sach_bai_hat = bll.layDanhSachBaiHat()
    
    if danh_sach_ca_si:
        window = GUIXemThongTinCaSi(ca_si=danh_sach_ca_si[0], danh_sach_bai_hat=danh_sach_bai_hat)
        window.show()
    else:
        print("Không tìm thấy ca sĩ nào trong dữ liệu")
    
    sys.exit(app.exec())