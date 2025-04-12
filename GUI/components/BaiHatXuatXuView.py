from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QScrollArea, QFrame, QPushButton
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QColor, QPalette
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from datetime import datetime

class BaiHatItem(QWidget):
    def __init__(self, bai_hat_data):
        super().__init__()
        self.bai_hat_data = bai_hat_data
        self.setupUI()
        
    def setupUI(self):
        # Layout chính
        mainLayout = QHBoxLayout()
        mainLayout.setContentsMargins(10, 10, 10, 10)
        
        # Ảnh bài hát
        anhLabel = QLabel()
        try:
            anh_path = self.bai_hat_data.get('AnhBaiHat', '')
            # print(f"Debug - Đường dẫn ảnh: {anh_path}")
            # Tạo đường dẫn tuyệt đối từ đường dẫn tương đối
            base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
            # print(f"Debug - Thư mục gốc: {base_dir}")
            
            if anh_path:
                # Xử lý đường dẫn để loại bỏ dấu / ở đầu nếu có
                if anh_path.startswith('/'):
                    anh_path = anh_path[1:]
                
                # In ra đường dẫn sau khi xử lý để debug
                # print(f"Debug - Đường dẫn ảnh sau khi xử lý: {anh_path}")
                
                # Tạo đường dẫn tuyệt đối từ gốc dự án
                full_path = os.path.join(base_dir, anh_path)
                # print(f"Debug - Đường dẫn đầy đủ: {full_path}")
                
                if os.path.exists(full_path):
                    pixmap = QPixmap(full_path)
                    # print(f"Debug - Đã tìm thấy ảnh tại: {full_path}")
                else:
                    # Thử tìm trong thư mục assets của dự án
                    default_img = os.path.join(base_dir, "assets", "AnhBaiHat", "0.png")
                    # print(f"Debug - Không tìm thấy ảnh tại {full_path}")
                    # print(f"Debug - Thử tìm ảnh mặc định tại: {default_img}")
                    
                    if os.path.exists(default_img):
                        pixmap = QPixmap(default_img)
                        # print(f"Debug - Đã tìm thấy ảnh mặc định")
                    else:
                        # print(f"Debug - Không tìm thấy ảnh mặc định, tạo ảnh trống")
                        pixmap = QPixmap(70, 70)
                        pixmap.fill(QColor('#cccccc'))
            else:
                # Nếu không có đường dẫn ảnh
                default_img = os.path.join(base_dir, "assets", "AnhBaiHat", "0.png")
                # print(f"Debug - Không có đường dẫn ảnh, sử dụng ảnh mặc định: {default_img}")
                
                if os.path.exists(default_img):
                    pixmap = QPixmap(default_img)
                    # print(f"Debug - Đã tìm thấy ảnh mặc định")
                else:
                    # print(f"Debug - Không tìm thấy ảnh mặc định, tạo ảnh trống")
                    pixmap = QPixmap(70, 70)
                    pixmap.fill(QColor('#cccccc'))
                    
        except Exception as e:
            print(f"Lỗi khi lấy ảnh bài hát: {e}")
            import traceback
            traceback.print_exc()
            pixmap = QPixmap(70, 70)
            pixmap.fill(QColor('#cccccc'))
        
        pixmap = pixmap.scaled(70, 70, Qt.AspectRatioMode.KeepAspectRatio)
        anhLabel.setPixmap(pixmap)
        anhLabel.setFixedSize(70, 70)
        
        # Thông tin bài hát
        infoLayout = QVBoxLayout()
        
        # Tiêu đề
        tieu_de = self.bai_hat_data.get('TieuDe', 'Không có tiêu đề')
        tieuDeLabel = QLabel(tieu_de)
        tieuDeLabel.setStyleSheet("font-weight: bold; font-size: 16px; color: #333;")
        
        # Ngày phát hành
        ngay_phat_hanh = self.bai_hat_data.get('NgayPhatHanh', None)
        if ngay_phat_hanh:
            if isinstance(ngay_phat_hanh, datetime):
                ngay_phat_hanh_str = ngay_phat_hanh.strftime('%d/%m/%Y')
            else:
                ngay_phat_hanh_str = str(ngay_phat_hanh)
        else:
            ngay_phat_hanh_str = 'Không rõ'
        
        ngayPhatHanhLabel = QLabel(f"Ngày phát hành: {ngay_phat_hanh_str}")
        ngayPhatHanhLabel.setStyleSheet("font-size: 12px; color: #777;")
        
        # Xuất xứ
        xuat_xu = self.bai_hat_data.get('TenXuatXu', 'Không rõ')
        xuatXuLabel = QLabel(f"Xuất xứ: {xuat_xu}")
        xuatXuLabel.setStyleSheet("font-size: 12px; color: #777;")
        
        # Thêm các thành phần vào layout thông tin
        infoLayout.addWidget(tieuDeLabel)
        infoLayout.addWidget(ngayPhatHanhLabel)
        infoLayout.addWidget(xuatXuLabel)
        infoLayout.setSpacing(2)
        
        # Thêm các thành phần vào layout chính
        mainLayout.addWidget(anhLabel)
        mainLayout.addLayout(infoLayout, 1)
        
        # Button phát nhạc
        playButton = QPushButton("Phát")
        playButton.setStyleSheet("""
            QPushButton {
                background-color: #1DB954;
                color: white;
                border-radius: 15px;
                padding: 5px 15px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #1ED760;
            }
        """)
        playButton.setCursor(Qt.CursorShape.PointingHandCursor)
        playButton.clicked.connect(self.phatBaiHat)  # Thay thế bằng hàm phát nhạc thực tế
        mainLayout.addWidget(playButton)
        
        # Thiết lập layout và style cho widget
        self.setLayout(mainLayout)
        self.setStyleSheet("""
            QWidget {
                background-color: #f9f9f9;
                border-radius: 8px;
                margin: 2px 0;
            }
            QWidget:hover {
                background-color: #f0f0f0;
            }
        """)
    
    def phatBaiHat(self):
        self.data_bai_hat = self.bai_hat_data.get('FileNhac', '')
        if self.data_bai_hat:
            # Thực hiện phát nhạc tại đây
            print(f"Đang phát bài hát: {self.data_bai_hat}")
        else:
            print("Không có dữ liệu bài hát để phát")
            
class BaiHatXuatXuView(QWidget):
    def __init__(self, ten_xuat_xu, danh_sach_bai_hat):
        super().__init__()
        self.ten_xuat_xu = ten_xuat_xu
        self.danh_sach_bai_hat = danh_sach_bai_hat
        self.setupUI()
        
    def setupUI(self):
        # Layout chính
        mainLayout = QVBoxLayout()
        
        # Tiêu đề
        titleLabel = QLabel(f"{self.ten_xuat_xu}")
        titleLabel.setStyleSheet("font-size: 20px; font-weight: bold; color: #333; margin-bottom: 15px;")
        mainLayout.addWidget(titleLabel)
        
        # Số lượng bài hát
        countLabel = QLabel(f"Tổng cộng: {len(self.danh_sach_bai_hat)} bài hát")
        countLabel.setStyleSheet("font-size: 14px; color: #666; margin-bottom: 10px;")
        mainLayout.addWidget(countLabel)
        
        # Container cho danh sách bài hát
        containerFrame = QFrame()
        containerFrame.setFrameShape(QFrame.Shape.StyledPanel)
        containerFrame.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 10px;
                border: 1px solid #ddd;
            }
        """)
        
        containerLayout = QVBoxLayout(containerFrame)
        
        # Thêm các bài hát vào container
        if self.danh_sach_bai_hat:
            for bai_hat in self.danh_sach_bai_hat:
                bai_hat_item = BaiHatItem(bai_hat)
                containerLayout.addWidget(bai_hat_item)
        else:
            emptyLabel = QLabel(f"Không có bài hát nào từ xuất xứ: {self.ten_xuat_xu}")
            emptyLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
            emptyLabel.setStyleSheet("font-size: 14px; color: #999; padding: 20px;")
            containerLayout.addWidget(emptyLabel)
        
        # Thêm container vào scroll area
        scrollArea = QScrollArea()
        scrollArea.setWidgetResizable(True)
        scrollArea.setWidget(containerFrame)
        scrollArea.setStyleSheet("""
            QScrollArea {
                border: none;
                background-color: transparent;
            }
        """)
        
        mainLayout.addWidget(scrollArea)
        self.setLayout(mainLayout)
        
        # Đặt màu nền cho widget
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(245, 245, 250))
        self.setPalette(palette)
        self.setAutoFillBackground(True)
