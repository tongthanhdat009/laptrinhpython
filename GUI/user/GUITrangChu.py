from PyQt6.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QListWidget, QListWidgetItem, QScrollArea, QPushButton, QFrame, QGridLayout
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QPixmap, QIcon, QColor, QPalette
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from BLL.BLLQuanLyDanhSachPhatHeThong import BLLQuanLyDanhSachPhatHeThong
from datetime import date
from GUI.components.PlaylistComponents import BaiHatItem, DanhSachPhatSection
from GUI.components.BaiHatXuatXuView import BaiHatXuatXuView
from BLL.BLLQuanLyDanhSachPhatHeThong import BLLQuanLyDanhSachPhatHeThong
from BLL.BLLTrangChu import BLLTrangChu

class GUITrangChu(QWidget):
    def __init__(self, load_songs):
        super().__init__()
        self.bllDSPHT = BLLQuanLyDanhSachPhatHeThong()
        self.bll = BLLTrangChu()
        self.load_songs = load_songs  # Lưu hàm phát nhạc vào biến instance
        self.setupUI()
        
    def setupUI(self):
        # Đặt kích thước cửa sổ
        self.setMinimumSize(1200, 500)
        
        # Tạo một palette với màu nền
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(245, 245, 250))
        self.setPalette(palette)
        
        # Tạo layout dọc (Vertical Layout)
        mainLayout = QVBoxLayout()
        mainLayout.setContentsMargins(20, 20, 20, 20)

        # Tạo scroll area để cuộn khi có nhiều danh sách phát
        scrollArea = QScrollArea()
        scrollArea.setWidgetResizable(True)
        scrollArea.setFrameShape(QFrame.Shape.NoFrame)
        scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        scrollArea.setStyleSheet("background-color: transparent;")
        
        # Widget chứa nội dung trong scroll area
        scrollContent = QWidget()
        scrollContent.setStyleSheet("background-color: transparent;")
        scrollLayout = QVBoxLayout(scrollContent)
        
        # Load danh sách phát
        self.loadDanhSachPhatGoiY(scrollLayout)
        self.loadDanhSachPhat(scrollLayout)
        self.loadDanhSachPhatTheoXuatXu(scrollLayout)
        
        scrollArea.setWidget(scrollContent)
        mainLayout.addWidget(scrollArea)

        # Cài đặt layout cho QWidget
        self.setLayout(mainLayout)

    def loadDanhSachPhatGoiY(self, layout):
        # Tạo tiêu đề phần xuất xứ
        titleLabel = QLabel("Gợi ý cho bạn")
        titleLabel.setStyleSheet("font-size: 24px; font-weight: bold; color: #333; margin-top: 30px;")
        layout.addWidget(titleLabel)

    def loadDanhSachPhatTheoXuatXu(self, layout):
        xuat_xu_list = ["Việt Nam", "Hàn Quốc", "US-UK"]
        xuat_xu_ids = {
            "Việt Nam": 1,
            "Hàn Quốc": 2,
            "US-UK": 3
        }  
        
        try:
            # Tạo tiêu đề phần xuất xứ
            titleLabel = QLabel("Khám phá âm nhạc theo xuất xứ")
            titleLabel.setStyleSheet("font-size: 24px; font-weight: bold; color: #333; margin-top: 30px;")
            layout.addWidget(titleLabel)
            
            displayed_count = 0
            for ten_xuat_xu in xuat_xu_list:
                if ten_xuat_xu in xuat_xu_ids:
                    ma_xuat_xu = xuat_xu_ids[ten_xuat_xu]
                    
                    # Lấy dữ liệu bài hát theo xuất xứ
                    danh_sach_bai_hat = self.bll.layBaiHatVoiXuatXu(ma_xuat_xu)
                    
                    if danh_sach_bai_hat and len(danh_sach_bai_hat) > 0:
                        # Thêm component hiển thị danh sách bài hát theo xuất xứ
                        section = BaiHatXuatXuView(ten_xuat_xu, danh_sach_bai_hat,self.load_songs)
                        layout.addWidget(section)
                        displayed_count += 1
            
            # Hiển thị thông báo nếu không có xuất xứ nào được hiển thị
            if displayed_count == 0:
                emptyLabel = QLabel("Không có dữ liệu bài hát nào từ các xuất xứ cần hiển thị")
                emptyLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
                emptyLabel.setStyleSheet("font-size: 18px; color: #999; padding: 50px;")
                layout.addWidget(emptyLabel)
                
        except Exception as e:
            print(f"Lỗi khi tải danh sách xuất xứ: {e}")
            import traceback
            traceback.print_exc()
            errorLabel = QLabel(f"Lỗi khi tải danh sách theo xuất xứ: {e}")
            errorLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
            errorLabel.setStyleSheet("font-size: 18px; color: red; padding: 50px;")
            layout.addWidget(errorLabel)
        
        # Thêm khoảng cách ở cuối section
        layout.addSpacing(30)
            
            
            
    def loadDanhSachPhat(self, layout):
        # Tạo tiêu đề phần xuất xứ
        titleLabel = QLabel("Danh sách mới")
        titleLabel.setStyleSheet("font-size: 24px; font-weight: bold; color: #333; margin-top: 30px;")
        layout.addWidget(titleLabel)
        try:
            danhSachPhat = self.bllDSPHT.lay_danh_sach_phat_he_thong()
            
            if not danhSachPhat:
                emptyLabel = QLabel("Không có danh sách phát nào")
                emptyLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
                emptyLabel.setStyleSheet("font-size: 18px; color: #999; padding: 50px;")
                layout.addWidget(emptyLabel)
                layout.addStretch()
                return
            
            # Đếm số danh sách phát hiển thị (có TrangThai = 1)
            visible_playlists = [playlist for playlist in danhSachPhat if playlist.TrangThai == 1]
            
            if not visible_playlists:
                emptyLabel = QLabel("Không có danh sách phát nào được hiển thị")
                emptyLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
                emptyLabel.setStyleSheet("font-size: 18px; color: #999; padding: 50px;")
                layout.addWidget(emptyLabel)
                layout.addStretch()
                return
            
            # Sắp xếp danh sách phát theo ngày tạo từ mới nhất đến cũ nhất
            visible_playlists.sort(key=lambda x: x.NgayTao, reverse=True)
            
            # Thêm từng danh sách phát có TrangThai = 1 vào layout
            for playlist in visible_playlists:
                section = DanhSachPhatSection(playlist, self.load_songs)
                layout.addWidget(section)
                    
            layout.addStretch()
                
        except Exception as e:
            print(f"Lỗi khi tải danh sách phát: {e}")
            errorLabel = QLabel(f"Lỗi khi tải danh sách phát: {e}")
            errorLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
            errorLabel.setStyleSheet("font-size: 18px; color: red; padding: 50px;")
            layout.addWidget(errorLabel)
            layout.addStretch()

if __name__ == "__main__":
    import sys
    from PyQt6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = GUITrangChu()
    window.show()
    sys.exit(app.exec())