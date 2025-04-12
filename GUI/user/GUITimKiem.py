import sys
import os
from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QLabel, QScrollArea, 
                            QHBoxLayout, QPushButton, QTabWidget, QGridLayout,
                            QLineEdit, QComboBox, QListWidget, QListWidgetItem,
                            QFrame, QSplitter, QApplication)
from PyQt6.QtCore import Qt, pyqtSlot, QSize  # Thêm QSize để dùng với setSizeHint
from PyQt6.QtGui import QIcon, QPixmap, QColor  # Thêm QColor cho hình ảnh mặc định

# Thêm đường dẫn cha vào sys.path để import các module
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

# Import các lớp BLL cần thiết
from BLL.BLLQuanLy import BLLQuanLy
from BLL.BLLQuanLyDanhSachPhatHeThong import BLLQuanLyDanhSachPhatHeThong

class GUITimKiem(QWidget):
    def __init__(self, search_content=""):
        super().__init__()
        print(search_content)
        # Khởi tạo các đối tượng quản lý dữ liệu
        self.BLLQuanLy = BLLQuanLy()
        self.BLLQuanLyDanhSachPhatHeThong = BLLQuanLyDanhSachPhatHeThong()
        self.search_content = search_content
        
        # Lấy dữ liệu ban đầu
        self.danh_sach_bai_hat = self.BLLQuanLy.layDanhSachBaiHat()
        self.danh_sach_ca_si = self.BLLQuanLy.layDanhSachCaSi()
        self.danh_sach_phat_he_thong = self.BLLQuanLyDanhSachPhatHeThong.lay_danh_sach_phat_he_thong()
        
        self.current_search_results = []
        self.setupUI()
        
    def setupUI(self):
        # Layout chính
        main_layout = QVBoxLayout()
        
        # Thiết lập style chung cho ứng dụng
        self.setStyleSheet("""
            QWidget {
                font-size: 16px;
                background-color: #f5f5f5;
            }
            QLabel {
                font-size: 16px;
            }
            QPushButton {
                font-size: 16px;
            }
            QComboBox {
                font-size: 16px;
                padding: 5px;
                border-radius: 5px;
            }
            QLineEdit {
                font-size: 16px;
            }
            QListWidget {
                font-size: 16px;
            }
        """)
        
        # Tiêu đề trang
        title_label = QLabel("Chào mừng đến với trang tìm kiếm")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("font-size: 30px; font-weight: bold; color: #1db954; padding: 20px;")
        main_layout.addWidget(title_label)
        
        # Phần tìm kiếm
        search_section = self.create_search_section()
        main_layout.addLayout(search_section)
        
        # Tabs kết quả tìm kiếm
        self.results_tab = QTabWidget()
        self.results_tab.setStyleSheet("""
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
        """)
        self.setup_results_tabs()
        main_layout.addWidget(self.results_tab)
        
        self.setLayout(main_layout)
        
        # Thực hiện tìm kiếm nếu có nội dung tìm kiếm ban đầu
        if hasattr(self, 'pending_search') and self.pending_search:
            self.perform_search()
    
    def create_search_section(self):
        # Tạo phần tìm kiếm gồm ô nhập và nút tìm kiếm
        search_layout = QVBoxLayout()
        
        # Khu vực nhập tìm kiếm
        search_input_layout = QHBoxLayout()
        
        # Thanh tìm kiếm
        self.search_input = QLineEdit()
        self.search_input.setPlaceholderText("Nhập từ khóa tìm kiếm...")
        self.search_input.setStyleSheet("""
            QLineEdit {
                border-radius: 20px;
                padding: 10px 15px;
                font-size: 16px;
                border: 1px solid #ccc;
                background-color: white;
            }
            QLineEdit:focus {
                border: 2px solid #1db954;
            }
        """)
        # Kết nối sự kiện thay đổi text với hàm tìm kiếm
        self.search_input.textChanged.connect(self.on_search_input_changed)
        search_input_layout.addWidget(self.search_input)
        
       # Set text cho search input nếu có
        if self.search_content:
            self.search_input.setText(self.search_content)
            self.pending_search = True
        else:
            self.pending_search = False
        
        # Nút tìm kiếm
        search_button = QPushButton("Tìm kiếm")
        search_button.setStyleSheet("""
            QPushButton {
                background-color: #1db954;
                color: white;
                border-radius: 20px;
                padding: 10px 20px;
                font-size: 16px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #1ed760;
            }
            QPushButton:pressed {
                background-color: #1aa34a;
            }
        """)
        search_button.clicked.connect(self.perform_search)
        search_input_layout.addWidget(search_button)
        
        search_layout.addLayout(search_input_layout)
        
        # Các tùy chọn bộ lọc và sắp xếp
        filter_layout = QHBoxLayout()
        
        # Bộ lọc theo loại kết quả
        filter_label = QLabel("Lọc theo:")
        filter_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        filter_layout.addWidget(filter_label)
        
        self.filter_combo = QComboBox()
        self.filter_combo.addItems(["Tất cả", "Bài hát", "Ca sĩ", "Playlist"])
        self.filter_combo.setStyleSheet("""
            QComboBox {
                border: 1px solid #ccc;
                border-radius: 5px;
                padding: 5px;
                font-size: 16px;
                background-color: white;
            }
            QComboBox::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 15px;
                border-left-width: 1px;
                border-left-color: #ccc;
                border-left-style: solid;
                border-top-right-radius: 5px;
                border-bottom-right-radius: 5px;
            }
        """)
        self.filter_combo.currentIndexChanged.connect(self.on_filter_changed)
        filter_layout.addWidget(self.filter_combo)
        
        # Tùy chọn sắp xếp
        sort_label = QLabel("Sắp xếp:")
        sort_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        filter_layout.addWidget(sort_label)
        
        self.sort_combo = QComboBox()
        self.sort_combo.addItems(["Mới nhất", "Phổ biến", "A-Z"])
        self.sort_combo.setStyleSheet("""
            QComboBox {
                border: 1px solid #ccc;
                border-radius: 5px;
                padding: 5px;
                font-size: 16px;
                background-color: white;
            }
            QComboBox::drop-down {
                subcontrol-origin: padding;
                subcontrol-position: top right;
                width: 15px;
                border-left-width: 1px;
                border-left-color: #ccc;
                border-left-style: solid;
                border-top-right-radius: 5px;
                border-bottom-right-radius: 5px;
            }
        """)
        self.sort_combo.currentIndexChanged.connect(self.on_sort_changed)
        filter_layout.addWidget(self.sort_combo)
        
        filter_layout.addStretch()
        
        search_layout.addLayout(filter_layout)
        
        # Thêm đường phân cách ngang
        separator = QFrame()
        separator.setFrameShape(QFrame.Shape.HLine)
        separator.setFrameShadow(QFrame.Shadow.Sunken)
        separator.setStyleSheet("background-color: #ccc;")
        search_layout.addWidget(separator)
        
        return search_layout
    
    def setup_results_tabs(self):
        # Thiết lập các tab để hiển thị kết quả tìm kiếm
        
        # Tab bài hát
        self.songs_tab = QWidget()
        songs_layout = QVBoxLayout()
        self.songs_list = QListWidget()
        self.songs_list.setStyleSheet("""
            QListWidget {
                border: none;
                background-color: white;
                font-size: 16px;
                border-radius: 5px;
            }
            QListWidget::item {
                padding: 10px;
                border-bottom: 1px solid #eee;
                min-height: 80px;
            }
            QListWidget::item:selected {
                background-color: #e8f5e9;
                color: #1db954;
                font-weight: bold;
            }
            QListWidget::item:hover {
                background-color: #f5f5f5;
            }
        """)
        songs_layout.addWidget(self.songs_list)
        self.songs_tab.setLayout(songs_layout)
        
        # Tab ca sĩ
        self.artists_tab = QWidget()
        artists_layout = QVBoxLayout()
        self.artists_list = QListWidget()
        self.artists_list.setStyleSheet("""
            QListWidget {
                border: none;
                background-color: white;
                font-size: 16px;
                border-radius: 5px;
            }
            QListWidget::item {
                padding: 10px;
                border-bottom: 1px solid #eee;
                min-height: 80px;
            }
            QListWidget::item:selected {
                background-color: #e8f5e9;
                color: #1db954;
                font-weight: bold;
            }
            QListWidget::item:hover {
                background-color: #f5f5f5;
            }
        """)
        artists_layout.addWidget(self.artists_list)
        self.artists_tab.setLayout(artists_layout)
        
        # Tab playlist
        self.playlists_tab = QWidget()
        playlists_layout = QVBoxLayout()
        self.playlists_list = QListWidget()
        self.playlists_list.setStyleSheet("""
            QListWidget {
                border: none;
                background-color: white;
                font-size: 16px;
                border-radius: 5px;
            }
            QListWidget::item {
                padding: 10px;
                border-bottom: 1px solid #eee;
                min-height: 80px;
            }
            QListWidget::item:selected {
                background-color: #e8f5e9;
                color: #1db954;
                font-weight: bold;
            }
            QListWidget::item:hover {
                background-color: #f5f5f5;
            }
        """)
        playlists_layout.addWidget(self.playlists_list)
        self.playlists_tab.setLayout(playlists_layout)
        
        # Thêm các tab vào tab widget
        self.results_tab.addTab(self.songs_tab, "Bài hát")
        self.results_tab.addTab(self.artists_tab, "Ca sĩ")
        self.results_tab.addTab(self.playlists_tab, "Playlist")
        
        # Khởi tạo dữ liệu ban đầu
        self.populate_initial_data()
    
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
    
    def get_playlist_image_path(self, playlist):
        """Lấy đường dẫn ảnh danh sách phát từ thuộc tính của đối tượng"""
        try:
            # Tạo đường dẫn tuyệt đối từ đường dẫn tương đối - di chuyển lên đầu hàm
            base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
            
            anh_path = playlist.Anh
            
            if anh_path:
                # Xử lý đường dẫn để loại bỏ dấu / ở đầu nếu có
                if anh_path.startswith('/'):
                    anh_path = anh_path[1:]
                    
                # Tạo đường dẫn tuyệt đối từ gốc dự án
                full_path = os.path.join(base_dir, anh_path)
                
                if os.path.exists(full_path):
                    return full_path
            
            # Thử tìm trong thư mục assets của dự án
            default_img = os.path.join(base_dir, "assets", "DanhSachPhatHeThong", f"{playlist.MaDanhSachPhat}.png")
            if os.path.exists(default_img):
                return default_img
            
            # Nếu có AnhDanhSachPhat và không có getAnh
            if hasattr(playlist, 'AnhDanhSachPhat') and playlist.AnhDanhSachPhat:
                anh_path = playlist.AnhDanhSachPhat
                
                if anh_path.startswith('/'):
                    anh_path = anh_path[1:]
                
                full_path = os.path.join(base_dir, anh_path)
                if os.path.exists(full_path):
                    return full_path
                
            # Đường dẫn dự phòng
            return os.path.join(base_dir, "assets", "DanhSachPhatHeThong", "0.png")
            
        except Exception as e:
            print(f"Lỗi khi lấy ảnh danh sách phát: {e}")
            # Trả về đường dẫn ảnh mặc định
            base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
            return os.path.join(base_dir, "assets", "DanhSachPhatHeThong", "0.png")
    
    def get_song_image_path(self, bai_hat):
        """Lấy đường dẫn ảnh bài hát từ thuộc tính của đối tượng"""
        try:
            # Tạo đường dẫn tuyệt đối từ đường dẫn tương đối - di chuyển lên đầu hàm
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
    
    def _them_anh_mac_dinh(self, label, width=100, height=100):
        """Thêm ảnh mặc định khi không tìm thấy ảnh"""
        # Tạo một pixmap trống với kích thước cho trước
        pixmap = QPixmap(width, height)
        pixmap.fill(QColor('#cccccc'))  # Màu xám nhạt
        label.setPixmap(pixmap)
        
    def _load_anh_tu_duong_dan(self, label, duong_dan, width=100, height=100):
        """
        Tải và hiển thị ảnh từ đường dẫn
        
        Args:
            label: QLabel để hiển thị ảnh
            duong_dan: đường dẫn tới file ảnh
            width, height: kích thước ảnh mong muốn
        """
        if not duong_dan:
            self._them_anh_mac_dinh(label, width, height)
            return
            
        # Chuẩn hóa đường dẫn cho Windows
        image_path = duong_dan.replace("/", "\\")
        
        # Thử tạo pixmap từ đường dẫn
        pixmap = QPixmap(r"{}".format(image_path))
        
        if pixmap.isNull():
            print(f"Failed to load image from: {image_path}")
            import os
            # Thử với đường dẫn tuyệt đối
            abs_path = os.path.abspath(image_path.strip())
            print(f"Trying absolute path: {abs_path}")
            pixmap = QPixmap(abs_path)
            
            if pixmap.isNull():
                # Sử dụng ảnh mặc định khi không tải được
                self._them_anh_mac_dinh(label, width, height)
            else:
                # Scale ảnh để hiển thị
                pixmap = pixmap.scaled(width, height, Qt.AspectRatioMode.KeepAspectRatio)
                label.setPixmap(pixmap)
        else:
            # Scale ảnh để hiển thị
            pixmap = pixmap.scaled(width, height, Qt.AspectRatioMode.KeepAspectRatio)
            label.setPixmap(pixmap)

    def create_item_widget(self, title, subtitle="", image_path=None, item_type=None, item_data=None):
        # Tạo widget hiển thị cho một mục trong danh sách kết quả (gồm hình ảnh và thông tin)
        widget = QWidget()
        layout = QHBoxLayout(widget)
        layout.setContentsMargins(5, 5, 5, 5)
        
        # Tạo label cho hình ảnh
        image_label = QLabel()
        image_label.setFixedSize(70, 70)
        
        # Tải và hiển thị hình ảnh bằng phương thức mới
        if image_path:
            self._load_anh_tu_duong_dan(image_label, image_path, 70, 70)
        else:
            # Sử dụng placeholder
            self._them_anh_mac_dinh(image_label, 70, 70)
            
        layout.addWidget(image_label)
        
        # Nội dung văn bản và nút phát
        content_layout = QVBoxLayout()
        
        # Phần tiêu đề và phụ đề
        text_layout = QHBoxLayout()
        title_and_subtitle = QVBoxLayout()
        
        title_label = QLabel(title)
        title_label.setStyleSheet("font-size: 16px; font-weight: bold;")
        title_and_subtitle.addWidget(title_label)
        
        if subtitle:
            subtitle_label = QLabel(subtitle)
            subtitle_label.setStyleSheet("font-size: 14px; color: #666;")
            title_and_subtitle.addWidget(subtitle_label)
        
        text_layout.addLayout(title_and_subtitle, 1)
        
        # Thêm nút phát nhạc cho bài hát và playlist với biểu tượng thay vì chữ
        if item_type in ["song", "playlist"]:
            playButton = QPushButton()
            
            # Tạo đường dẫn đến biểu tượng play
            base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
            icon_path = os.path.join(base_dir, "assets", "icon", "play-button.png")
            
            # Thiết lập biểu tượng cho nút
            if os.path.exists(icon_path):
                icon = QIcon(icon_path)
                playButton.setIcon(icon)
                playButton.setIconSize(QSize(20, 20))
            else:
                # Fallback to text if icon not found
                playButton.setText("▶")
            
            playButton.setStyleSheet("""
                QPushButton {
                    background-color: #1DB954;
                    color: white;
                    border-radius: 15px;
                    padding: 5px;
                    font-weight: bold;
                    min-width: 30px;
                    min-height: 30px;
                }
                QPushButton:hover {
                    background-color: #1ED760;
                }
            """)
            playButton.setCursor(Qt.CursorShape.PointingHandCursor)
            playButton.setToolTip("Phát")
            playButton.setFixedSize(QSize(35, 35))
            
            # Kết nối nút với hàm xử lý sự kiện
            if item_type == "song":
                playButton.clicked.connect(lambda checked=False, s=item_data: self.play_song(s))
            else:  # playlist
                playButton.clicked.connect(lambda checked=False, p=item_data: self.play_playlist(p))
                
            text_layout.addWidget(playButton)
        
        # Thêm nút xem thông tin cho ca sĩ
        elif item_type == "artist":
            infoButton = QPushButton()
            
            # Tạo đường dẫn đến biểu tượng info
            base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
            icon_path = os.path.join(base_dir, "assets", "icon", "info-circle.png")
            
            # Thiết lập biểu tượng cho nút
            if os.path.exists(icon_path):
                icon = QIcon(icon_path)
                infoButton.setIcon(icon)
                infoButton.setIconSize(QSize(20, 20))
            else:
                # Fallback to text if icon not found
                infoButton.setText("i")
            
            infoButton.setStyleSheet("""
                QPushButton {
                    background-color: #4384e0;
                    color: white;
                    border-radius: 15px;
                    padding: 5px;
                    font-weight: bold;
                    min-width: 30px;
                    min-height: 30px;
                }
                QPushButton:hover {
                    background-color: #5599ff;
                }
            """)
            infoButton.setCursor(Qt.CursorShape.PointingHandCursor)
            infoButton.setToolTip("Xem thông tin")
            infoButton.setFixedSize(QSize(35, 35))
            
            # Kết nối nút với hàm xử lý sự kiện
            infoButton.clicked.connect(lambda checked=False, a=item_data: self.view_artist_info(a))
            
            text_layout.addWidget(infoButton)
        
        content_layout.addLayout(text_layout)
        content_layout.addStretch()
        layout.addLayout(content_layout, 1)
        
        return widget

    def view_artist_info(self, artist):
        """Xử lý khi người dùng nhấn nút xem thông tin ca sĩ"""
        try:
            # Import giao diện thông tin ca sĩ
            from GUI.user.GUIXemThongTinCaSi import GUIXemThongTinCaSi
            
            # Hiển thị dialog thông tin ca sĩ
            dialog = GUIXemThongTinCaSi(parent=self, ca_si=artist, danh_sach_bai_hat=self.danh_sach_bai_hat)
            dialog.setWindowModality(Qt.WindowModality.ApplicationModal)
            dialog.exec()
        except Exception as e:
            print(f"Lỗi khi hiển thị thông tin ca sĩ: {e}")
        

    def play_song(self, song):
        """Xử lý khi người dùng nhấn nút phát bài hát"""
        print(f"Đang phát bài hát: {song.getTieuDe()}")
        # TODO: Thêm code để phát nhạc thực tế ở đây
        # Ví dụ: gọi đến BLL để xử lý việc phát nhạc
    
    def play_playlist(self, playlist):
        """Xử lý khi người dùng nhấn nút phát playlist"""
        print(f"Đang phát playlist: {playlist.TieuDe}")
        # TODO: Thêm code để phát playlist thực tế ở đây

    def populate_initial_data(self):
        # Khởi tạo dữ liệu ban đầu cho các danh sách
        
        # Đổ dữ liệu bài hát
        self.songs_list.clear()
        for bai_hat in self.danh_sach_bai_hat:
            # Xử lý tên ca sĩ (có thể là list hoặc string)
            artist_text = ", ".join(bai_hat.getCaSi()) if isinstance(bai_hat.getCaSi(), list) else bai_hat.getCaSi()
            image_path = self.get_song_image_path(bai_hat)  # Truyền đối tượng bài hát
            
            item = QListWidgetItem()
            # Thiết lập kích thước cố định cho mỗi item - Sử dụng QSize để tránh lỗi
            item.setSizeHint(QSize(self.songs_list.width(), 80))
            item.setData(Qt.ItemDataRole.UserRole, bai_hat)
            
            widget = self.create_item_widget(
                bai_hat.getTieuDe(),
                f"Ca sĩ: {artist_text}",
                image_path,
                "song",    # Thêm loại item
                bai_hat    # Truyền đối tượng để xử lý khi click
            )
            
            self.songs_list.addItem(item)
            self.songs_list.setItemWidget(item, widget)
        
        # Đổ dữ liệu ca sĩ
        self.artists_list.clear()
        for ca_si in self.danh_sach_ca_si:
            image_path = self.get_artist_image_path(ca_si)  # Truyền đối tượng ca sĩ
            
            item = QListWidgetItem()
            item.setSizeHint(QSize(self.artists_list.width(), 80))
            item.setData(Qt.ItemDataRole.UserRole, ca_si)
            
            widget = self.create_item_widget(
                ca_si.getNgheDanh(),
                "Ca sĩ",
                image_path,
                "artist",    # Thêm loại item
                ca_si        # Truyền đối tượng để xử lý khi click
            )
            
            self.artists_list.addItem(item)
            self.artists_list.setItemWidget(item, widget)
        
        # Đổ dữ liệu playlist
        self.playlists_list.clear()
        for playlist in self.danh_sach_phat_he_thong:
            image_path = self.get_playlist_image_path(playlist)  # Truyền đối tượng playlist
            
            item = QListWidgetItem()
            item.setSizeHint(QSize(self.playlists_list.width(), 80))
            item.setData(Qt.ItemDataRole.UserRole, playlist)
            
            widget = self.create_item_widget(
                playlist.TieuDe,
                f"{len(playlist.BaiHat)} bài hát" if hasattr(playlist, 'BaiHat') else "",
                image_path,
                "playlist",    # Thêm loại item
                playlist       # Truyền đối tượng để xử lý khi click
            )
            
            self.playlists_list.addItem(item)
            self.playlists_list.setItemWidget(item, widget)
    
    @pyqtSlot(str)
    def on_search_input_changed(self, text):
        # Xử lý sự kiện khi người dùng nhập vào ô tìm kiếm
        if len(text) >= 2:  # Chỉ tìm kiếm khi có ít nhất 2 ký tự
            self.perform_search()
    
    @pyqtSlot(int)
    def on_filter_changed(self, index):
        # Xử lý khi thay đổi bộ lọc
        self.perform_search()
    
    @pyqtSlot(int)
    def on_sort_changed(self, index):
        # Xử lý khi thay đổi cách sắp xếp
        self.perform_search()
    
    def perform_search(self):
        # Hàm thực hiện tìm kiếm dựa trên các điều kiện đã chọn
        search_text = self.search_input.text().lower()
        
        # Kiểm tra xem các thành phần UI đã được khởi tạo chưa
        if not hasattr(self, 'songs_list') or not hasattr(self, 'artists_list') or not hasattr(self, 'playlists_list'):
            # Các thành phần UI chưa được khởi tạo, lưu lại yêu cầu tìm kiếm để thực hiện sau
            self.pending_search = True
            return
            
        # Các thành phần UI đã sẵn sàng, tiến hành tìm kiếm
        filter_option = self.filter_combo.currentText() if hasattr(self, 'filter_combo') else "Tất cả"
        
        # Tìm kiếm bài hát
        if filter_option in ["Tất cả", "Bài hát"]:
            self.songs_list.clear()
            # Lọc bài hát phù hợp với từ khóa tìm kiếm (tên hoặc ca sĩ)
            filtered_songs = [song for song in self.danh_sach_bai_hat 
                            if search_text in song.getTieuDe().lower() or 
                            any(search_text in ca_si.lower() for ca_si in song.getCaSi() if isinstance(ca_si, str))]
            
            # Áp dụng sắp xếp
            sort_option = self.sort_combo.currentText()
            if sort_option == "A-Z":
                filtered_songs.sort(key=lambda x: x.getTieuDe())
            # Có thể thêm các tùy chọn sắp xếp khác nếu cần
            
            # Hiển thị kết quả tìm kiếm bài hát
            for song in filtered_songs:
                artist_text = ", ".join(song.getCaSi()) if isinstance(song.getCaSi(), list) else song.getCaSi()
                image_path = self.get_song_image_path(song)  # Truyền đối tượng bài hát
                
                item = QListWidgetItem()
                item.setSizeHint(QSize(self.songs_list.width(), 80))
                item.setData(Qt.ItemDataRole.UserRole, song)
                
                widget = self.create_item_widget(
                    song.getTieuDe(),
                    f"Ca sĩ: {artist_text}",
                    image_path,
                    "song",    # Thêm loại item
                    song       # Truyền đối tượng để xử lý khi click
                )
                
                self.songs_list.addItem(item)
                self.songs_list.setItemWidget(item, widget)
        
        # Tìm kiếm ca sĩ
        if filter_option in ["Tất cả", "Ca sĩ"]:
            self.artists_list.clear()
            # Lọc ca sĩ phù hợp với từ khóa tìm kiếm
            filtered_artists = [artist for artist in self.danh_sach_ca_si 
                               if search_text in artist.getNgheDanh().lower()]
            
            # Áp dụng sắp xếp
            sort_option = self.sort_combo.currentText()
            if sort_option == "A-Z":
                filtered_artists.sort(key=lambda x: x.getNgheDanh())
            
            # Hiển thị kết quả tìm kiếm ca sĩ
            for artist in filtered_artists:
                image_path = self.get_artist_image_path(artist)  # Truyền đối tượng ca sĩ
                
                item = QListWidgetItem()
                item.setSizeHint(QSize(self.artists_list.width(), 80))
                item.setData(Qt.ItemDataRole.UserRole, artist)
                
                widget = self.create_item_widget(
                    artist.getNgheDanh(),
                    "Ca sĩ",
                    image_path,
                    "artist",    # Thêm loại item
                    artist       # Truyền đối tượng để xử lý khi click
                )
                
                self.artists_list.addItem(item)
                self.artists_list.setItemWidget(item, widget)
        
        # Tìm kiếm playlist
        if filter_option in ["Tất cả", "Playlist"]:
            self.playlists_list.clear()
            # Lọc playlist phù hợp với từ khóa tìm kiếm
            filtered_playlists = [playlist for playlist in self.danh_sach_phat_he_thong 
                                 if search_text in playlist.TieuDe.lower()]
            
            # Áp dụng sắp xếp
            sort_option = self.sort_combo.currentText()
            if sort_option == "A-Z":
                filtered_playlists.sort(key=lambda x: x.TieuDe)
            
            # Hiển thị kết quả tìm kiếm playlist
            for playlist in filtered_playlists:
                image_path = self.get_playlist_image_path(playlist)  # Truyền đối tượng playlist
                
                item = QListWidgetItem()
                item.setSizeHint(QSize(self.playlists_list.width(), 80))
                item.setData(Qt.ItemDataRole.UserRole, playlist)
                
                widget = self.create_item_widget(
                    playlist.TieuDe,
                    f"{len(playlist.BaiHat)} bài hát" if hasattr(playlist, 'BaiHat') else "",
                    image_path,
                    "playlist",    # Thêm loại item
                    playlist       # Truyền đối tượng để xử lý khi click
                )
                
                self.playlists_list.addItem(item)
                self.playlists_list.setItemWidget(item, widget)
        
        # Chuyển đến tab thích hợp dựa trên bộ lọc đã chọn
        if filter_option == "Bài hát":
            self.results_tab.setCurrentIndex(0)
        elif filter_option == "Ca sĩ":
            self.results_tab.setCurrentIndex(1)
        elif filter_option == "Playlist":
            self.results_tab.setCurrentIndex(2)
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = GUITimKiem()
    window.setWindowTitle("Tìm Kiếm")
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec())