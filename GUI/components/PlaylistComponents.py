from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QFrame
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QIcon, QColor
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from BLL.BLLQuanLyDanhSachPhatHeThong import BLLQuanLyDanhSachPhatHeThong

class BaiHatItem(QWidget):
    def __init__(self, baiHat, index):
        super().__init__()
        self.baiHat = baiHat
        self.index = index
        self.setupUI()
        
    def setupUI(self):
        layout = QHBoxLayout()
        layout.setContentsMargins(5, 5, 5, 5)
        
        # Số thứ tự
        indexLabel = QLabel(str(self.index))
        indexLabel.setFixedWidth(30)
        indexLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        indexLabel.setStyleSheet("font-size: 14px; color: #888;")
        
        # Ảnh bài hát
        anhLabel = QLabel()
        try:
            if hasattr(self.baiHat, 'getAnh') and callable(getattr(self.baiHat, 'getAnh')):
                anh_path = self.baiHat.getAnh()
                
                # Tạo đường dẫn tuyệt đối từ đường dẫn tương đối
                base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
                
                if anh_path:
                    # Xử lý đường dẫn để loại bỏ dấu / ở đầu nếu có
                    if anh_path.startswith('/'):
                        anh_path = anh_path[1:]
                        
                    # Tạo đường dẫn tuyệt đối từ gốc dự án
                    full_path = os.path.join(base_dir, anh_path)
                    
                    if os.path.exists(full_path):
                        pixmap = QPixmap(full_path)
                    else:
                        # Thử tìm trong thư mục assets của dự án
                        default_img = os.path.join(base_dir, "assets", "AnhBaiHat", "0.png")
                        if os.path.exists(default_img):
                            pixmap = QPixmap(default_img)
                        else:
                            # Tạo pixmap trống
                            pixmap = QPixmap(50, 50)
                            pixmap.fill(QColor('#cccccc'))
                else:
                    pixmap = QPixmap(50, 50)
                    pixmap.fill(QColor('#cccccc'))
            else:
                pixmap = QPixmap(50, 50)
                pixmap.fill(QColor('#cccccc'))
        except Exception as e:
            print(f"Lỗi khi lấy ảnh bài hát: {e}")
            pixmap = QPixmap(50, 50)
            pixmap.fill(QColor('#cccccc'))
        
        pixmap = pixmap.scaled(50, 50, Qt.AspectRatioMode.KeepAspectRatio)
        anhLabel.setPixmap(pixmap)
        anhLabel.setFixedSize(50, 50)
        
        # Thông tin bài hát
        infoLayout = QVBoxLayout()
        
        # Tên bài hát
        try:
            if hasattr(self.baiHat, 'getTieuDe') and callable(getattr(self.baiHat, 'getTieuDe')):
                ten_bai_hat = self.baiHat.getTieuDe()
            elif hasattr(self.baiHat, '_TenBaiHat'):
                ten_bai_hat = self.baiHat._TenBaiHat
            else:
                ten_bai_hat = "Unknown"
        except Exception as e:
            print(f"Lỗi khi lấy tên bài hát: {e}")
            ten_bai_hat = "Unknown"
        
        tenBaiHat = QLabel(ten_bai_hat)
        tenBaiHat.setStyleSheet("font-weight: bold; font-size: 14px;")
        
        # Ca sĩ
        try:
            if hasattr(self.baiHat, 'getCaSi') and callable(getattr(self.baiHat, 'getCaSi')):
                ca_si_data = self.baiHat.getCaSi()
                
                # Xử lý khác nhau dựa trên kiểu dữ liệu
                if ca_si_data is None:
                    ca_si_text = "Unknown Artist"
                elif isinstance(ca_si_data, list):
                    # Nếu là list, kết hợp các phần tử
                    if ca_si_data:  # Đảm bảo list không rỗng
                        # Xử lý trường hợp danh sách từ điển có chứa TenCaSi
                        if all(isinstance(cs, dict) and 'TenCaSi' in cs for cs in ca_si_data):
                            ca_si_text = ', '.join([cs['TenCaSi'] for cs in ca_si_data])
                        else:
                            ca_si_text = ', '.join([str(cs) for cs in ca_si_data if cs])
                    else:
                        ca_si_text = "Unknown Artist"
                elif isinstance(ca_si_data, str):
                    # Nếu là string, sử dụng trực tiếp
                    ca_si_text = ca_si_data
                else:
                    # Các trường hợp khác, chuyển đổi thành string
                    ca_si_text = str(ca_si_data)
            elif hasattr(self.baiHat, '_CaSi'):
                ca_si_text = self.baiHat._CaSi
            else:
                ca_si_text = "Unknown Artist"
        except Exception as e:
            print(f"Lỗi khi lấy tên ca sĩ: {e}")
            ca_si_text = "Unknown Artist"
            
        caSi = QLabel(ca_si_text)
        caSi.setStyleSheet("font-size: 12px; color: #555;")
        
        infoLayout.addWidget(tenBaiHat)
        infoLayout.addWidget(caSi)
        infoLayout.setSpacing(2)
        
        # Play button
        playButton = QPushButton()
        playButton.setIcon(QIcon("assets/icon/play-button.png"))
        playButton.setFixedSize(36, 36)
        playButton.setStyleSheet("""
            QPushButton {
                background-color: #1DB954;
                border-radius: 18px;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #1ED760;
            }
        """)
        playButton.setCursor(Qt.CursorShape.PointingHandCursor)
        playButton.clicked.connect(self.playButtonClicked)        
        
        # Thêm các thành phần vào layout
        layout.addWidget(indexLabel)
        layout.addWidget(anhLabel)
        layout.addLayout(infoLayout, 1)
        layout.addWidget(playButton)
        
        self.setLayout(layout)
        
        # Style cho item 
        self.setStyleSheet("""
            QWidget {
                background-color: transparent;
            }
            QWidget:hover {
                background-color: rgba(0, 0, 0, 0.05);
                border-radius: 5px;
            }
        """)
    def playButtonClicked(self):
        try:
            if hasattr(self.baiHat, 'getFileNhac') and callable(getattr(self.baiHat, 'getFileNhac')):
                file_path = self.baiHat.getFileNhac()
                print(f"Đường dẫn file nhạc: {file_path}")
        except Exception as e:
            print(f"Lỗi khi lấy file: {e}")
            ca_si_text = "Unknown Artist"
            
class DanhSachPhatSection(QWidget):
    def __init__(self, danhSachPhat):
        super().__init__()
        self.danhSachPhat = danhSachPhat
        self.danhSachBaiHat = []
        self.bll = BLLQuanLyDanhSachPhatHeThong()
        self.isShowingAllSongs = False  # Flag để theo dõi trạng thái hiển thị
        self.setupUI()

    def lay_danh_sach_bai_hat(self):
        try:
            # Lấy toàn bộ danh sách bài hát (không giới hạn số lượng)
            self.danhSachBaiHat = self.bll.lay_danh_sach_bai_hat_theo_ma_danh_sach(self.danhSachPhat._MaDanhSachPhatHeThong)
            print(f"Tổng số bài hát trong danh sách: {len(self.danhSachBaiHat)}")
        except Exception as e:
            print(f"Lỗi khi lấy danh sách bài hát: {e}")
            
    def setupUI(self):
        # Layout chính
        mainLayout = QVBoxLayout()
        mainLayout.setContentsMargins(0, 0, 0, 20)
        
        # Header section với thông tin danh sách phát
        headerLayout = QHBoxLayout()
        
        # Widget hiển thị ảnh
        anhLabel = QLabel()
        if self.danhSachPhat._Anh and os.path.exists(self.danhSachPhat._Anh):
            pixmap = QPixmap(self.danhSachPhat._Anh)
        else:
            # Sử dụng ảnh mặc định nếu không tìm thấy
            base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
            default_img = os.path.join(base_dir, "assets", "AnhBaiHat", "0.png")
            if os.path.exists(default_img):
                pixmap = QPixmap(default_img)
            else:
                pixmap = QPixmap(120, 120)
                pixmap.fill(QColor('#cccccc'))
        
        pixmap = pixmap.scaled(120, 120, Qt.AspectRatioMode.KeepAspectRatio)
        anhLabel.setPixmap(pixmap)
        anhLabel.setFixedSize(120, 120)
        
        # Thông tin danh sách phát
        infoLayout = QVBoxLayout()
        
        # Tiêu đề
        tieuDeLabel = QLabel(self.danhSachPhat._TieuDe)
        tieuDeLabel.setStyleSheet("font-weight: bold; font-size: 24px; color: #333;")
        
        # Mô tả
        moTaLabel = QLabel(self.danhSachPhat._MoTa)
        moTaLabel.setStyleSheet("font-size: 14px; color: #555;")
        moTaLabel.setWordWrap(True)
        
        # Ngày tạo
        ngayTaoLabel = QLabel(f"Ngày tạo: {self.danhSachPhat._NgayTao.strftime('%d/%m/%Y')}")
        ngayTaoLabel.setStyleSheet("font-size: 12px; color: #888;")
        
        # Button phát tất cả
        playAllButton = QPushButton("Phát tất cả")
        playAllButton.setIcon(QIcon("../../assets/images/play_all.png"))
        playAllButton.setCursor(Qt.CursorShape.PointingHandCursor)
        playAllButton.setStyleSheet("""
            QPushButton {
                background-color: #1DB954;
                color: white;
                border-radius: 20px;
                padding: 8px 15px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #1ED760;
            }
        """)
        playAllButton.clicked.connect(self.playAllButtonClicked)
        
        # Thêm các thành phần vào layout thông tin
        infoLayout.addWidget(tieuDeLabel)
        infoLayout.addWidget(moTaLabel)
        infoLayout.addWidget(ngayTaoLabel)
        infoLayout.addWidget(playAllButton)
        infoLayout.addStretch()
        
        # Thêm các thành phần vào header layout
        headerLayout.addWidget(anhLabel)
        headerLayout.addLayout(infoLayout, 1)
        headerLayout.addStretch()
        
        # Thêm header vào layout chính
        mainLayout.addLayout(headerLayout)
        
        # Danh sách bài hát
        songsLabel = QLabel("Danh sách bài hát")
        songsLabel.setStyleSheet("font-size: 16px; font-weight: bold; margin-top: 10px;")
        mainLayout.addWidget(songsLabel)
        
        # Khung chứa danh sách bài hát
        songListFrame = QFrame()
        songListFrame.setFrameShape(QFrame.Shape.StyledPanel)
        songListFrame.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 10px;
                border: 1px solid #ddd;
            }
        """)
        
        self.songListLayout = QVBoxLayout(songListFrame)  # Lưu reference để có thể cập nhật
        
        # Lấy toàn bộ danh sách bài hát
        self.lay_danh_sach_bai_hat()
        
        # Hiển thị danh sách bài hát
        self.displaySongs()
        
        mainLayout.addWidget(songListFrame)
        
        # Thêm đường ngăn cách
        separator = QFrame()
        separator.setFrameShape(QFrame.Shape.HLine)
        separator.setStyleSheet("background-color: #ddd;")
        mainLayout.addWidget(separator)
        
        self.setLayout(mainLayout)

    def playAllButtonClicked(self):
        try:
            # Lấy danh sách bài hát từ danh sách phát
            if hasattr(self.danhSachPhat, '_MaDanhSachPhatHeThong'):
                ma_danh_sach = self.danhSachPhat._MaDanhSachPhatHeThong
                print(f"Đang phát tất cả bài hát trong danh sách: {ma_danh_sach}")
                lay_danh_sach_bai_hat = self.bll.lay_danh_sach_bai_hat_theo_ma_danh_sach(ma_danh_sach)
                print(f"Tổng số bài hát trong danh sách: {len(lay_danh_sach_bai_hat)}")
                # Thực hiện phát nhạc tại đây
            else:
                print("Không có mã danh sách phát để phát nhạc")
        except Exception as e:
            print(f"Lỗi khi phát tất cả bài hát: {e}")

    def displaySongs(self):
        # Xóa tất cả widgets hiện có trong layout
        while self.songListLayout.count():
            item = self.songListLayout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()

        if self.danhSachBaiHat:
            # Xác định số lượng bài hát hiển thị dựa trên trạng thái
            if self.isShowingAllSongs:
                displayCount = len(self.danhSachBaiHat)
            else:
                displayCount = min(5, len(self.danhSachBaiHat))
                
            # Hiển thị bài hát
            for i in range(displayCount):
                try:
                    songItem = BaiHatItem(self.danhSachBaiHat[i], i+1)
                    self.songListLayout.addWidget(songItem)
                except Exception as e:
                    print(f"Lỗi khi thêm bài hát: {e}")
                    
            # Thêm nút "Xem thêm" hoặc "Thu gọn" tùy thuộc vào trạng thái
            if len(self.danhSachBaiHat) > 5:
                if self.isShowingAllSongs:
                    seeButton = QPushButton("Thu gọn")
                else:
                    seeButton = QPushButton(f"Xem thêm {len(self.danhSachBaiHat) - 5} bài hát")
                
                seeButton.setStyleSheet("""
                    QPushButton {
                        background-color: transparent;
                        color: #1DB954;
                        font-weight: bold;
                        padding: 8px;
                        text-align: center;
                        border: none;
                    }
                    QPushButton:hover {
                        color: #1ED760;
                        text-decoration: underline;
                    }
                """)
                seeButton.clicked.connect(self.toggleSongDisplay)
                self.songListLayout.addWidget(seeButton)
        else:
            emptyLabel = QLabel("Không có bài hát nào trong danh sách này")
            emptyLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
            emptyLabel.setStyleSheet("font-size: 14px; color: #999; padding: 20px;")
            self.songListLayout.addWidget(emptyLabel)
    
    def toggleSongDisplay(self):
        # Đảo ngược trạng thái hiển thị
        self.isShowingAllSongs = not self.isShowingAllSongs
        # Hiển thị lại danh sách
        self.displaySongs()