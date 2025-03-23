from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QFormLayout, 
                          QLabel, QLineEdit, QTextEdit, QComboBox, QPushButton, 
                          QFileDialog, QMessageBox, QGroupBox, QWidget)
from PyQt6.QtGui import QFont, QPixmap, QTextCursor
from PyQt6.QtCore import Qt
from datetime import datetime
import os
import shutil
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from BLL.BLLQuanLyDanhSachPhatHeThong import BLLQuanLyDanhSachPhatHeThong

class GUIThemDanhSachPhatHeThong(QDialog):
    def __init__(self, parent=None, danh_sach=None):
        super().__init__(parent)
        self.danh_sach = danh_sach
        self.setWindowTitle("🎵 Thêm Danh Sách Phát Hệ Thống")
        self.setFixedSize(800, 950)  # Tăng kích thước cửa sổ
        self.image_path = None
        self.bll = BLLQuanLyDanhSachPhatHeThong()
        self.ds_tieu_de = []
        
        self.xu_ly_tieu_de()
        self.setup_ui()
        
    def setup_ui(self):
        """Thiết lập giao diện người dùng"""
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(15)
        
        # Thêm tiêu đề chính
        self.add_main_title(main_layout)
        
        # Form layout cho các trường nhập liệu
        form_layout = QFormLayout()
        form_layout.setVerticalSpacing(15)
        form_layout.setLabelAlignment(Qt.AlignmentFlag.AlignRight)
        
        # Tạo các trường
        self.create_id_field(form_layout)
        self.create_title_field(form_layout)
        self.create_desc_field(form_layout)
        self.create_status_field(form_layout)
        self.create_date_field(form_layout)
        
        # Layout cho phần chọn ảnh
        self.create_image_selection(form_layout)
        
        # Thêm form vào layout chính
        main_layout.addLayout(form_layout)
        
        # Thêm các nút
        button_layout = QHBoxLayout()
        self.create_buttons(button_layout)
        main_layout.addLayout(button_layout)
        
        self.setLayout(main_layout)
    
    def xu_ly_tieu_de(self):
        if not self.danh_sach:
            return
        try:
            for ds in self.danh_sach:
                self.ds_tieu_de.append(ds.TieuDe)
                
            print(f"Đã tải {len(self.ds_tieu_de)} tiêu đề danh sách phát")
        except Exception as e:
            print(f"Lỗi khi xử lý tiêu đề: {str(e)}")
            import traceback
            traceback.print_exc()
        
    def add_main_title(self, layout):
        """Thêm tiêu đề chính cho form"""
        # Container cho tiêu đề
        title_container = QWidget()
        title_container.setStyleSheet("background-color: #2196F3; border-radius: 8px;")
        title_layout = QVBoxLayout(title_container)
        title_layout.setContentsMargins(15, 15, 15, 15)
        
        # Tiêu đề chính
        main_title = QLabel("🎵 THÊM DANH SÁCH PHÁT MỚI")
        main_title.setFont(QFont("Arial", 18, QFont.Weight.Bold))
        main_title.setStyleSheet("color: white;")
        main_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        # Tiêu đề phụ
        sub_title = QLabel("📝 Nhập thông tin chi tiết về danh sách phát hệ thống mới")
        sub_title.setFont(QFont("Arial", 13))
        sub_title.setStyleSheet("color: rgba(255, 255, 255, 0.9);")
        sub_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        title_layout.addWidget(main_title)
        title_layout.addWidget(sub_title)
        
        # Thêm vào layout chính với margin
        layout.addWidget(title_container)
        
        # Thêm khoảng cách sau tiêu đề
        spacer = QWidget()
        spacer.setFixedHeight(10)
        layout.addWidget(spacer)
    
    def create_id_field(self, form_layout):
        """Tạo trường mã danh sách (chỉ đọc)"""
        id_label = QLabel("🆔 Mã danh sách:")
        id_label.setFont(QFont("Arial", 13))
        
        self.id_field = QLineEdit()
        self.id_field.setReadOnly(True)
        self.id_field.setStyleSheet("""
            QLineEdit {
                background-color: #f5f5f5;
                padding: 8px;
                border: 1px solid #ddd;
                border-radius: 4px;
                font-size: 13pt;
            }
        """)
        
        form_layout.addRow(id_label, self.id_field)
        
        try:
            self.id_field.setText("{}".format(self.bll.lay_id_danh_sach_phat_moi()))
        except Exception as e:
            print(f"Lỗi khi lấy ID danh sách phát mới: {str(e)}")
            self.id_field.setText("Auto")
            
    def create_title_field(self, form_layout):
        """Tạo trường tiêu đề"""
        title_label = QLabel("🏷️ Tiêu đề:")
        title_label.setFont(QFont("Arial", 13))
        
        self.title_field = QLineEdit()
        self.title_field.setPlaceholderText("Nhập tiêu đề danh sách phát")
        self.title_field.setMaxLength(255)
        self.title_field.setStyleSheet("""
            QLineEdit {
                padding: 8px;
                border: 1px solid #ddd;
                border-radius: 4px;
                font-size: 13pt;
            }
            QLineEdit:focus {
                border: 1px solid #4CAF50;
            }
        """)
        
        form_layout.addRow(title_label, self.title_field)
    
    def create_desc_field(self, form_layout):
        """Tạo trường mô tả"""
        desc_label = QLabel("📝 Mô tả:")
        desc_label.setFont(QFont("Arial", 13))
        
        self.desc_field = QTextEdit()
        self.desc_field.setPlaceholderText("Nhập mô tả cho danh sách phát")
        self.desc_field.setStyleSheet("""
            QTextEdit {
                padding: 8px;
                border: 1px solid #ddd;
                border-radius: 4px;
                font-size: 13pt;
            }
            QTextEdit:focus {
                border: 1px solid #4CAF50;
            }
        """)
        self.desc_field.setFixedHeight(100)  
        
        # Giới hạn số ký tự
        self.char_count_label = QLabel("0/255 ký tự")
        self.char_count_label.setStyleSheet("color: #888; font-size: 10pt;")
        self.desc_field.textChanged.connect(self.check_desc_length)
        
        # Container cho mô tả và đếm ký tự
        desc_container = QVBoxLayout()
        desc_container.addWidget(self.desc_field)
        desc_container.addWidget(self.char_count_label, alignment=Qt.AlignmentFlag.AlignRight)
        
        # Tạo widget container
        container_widget = QWidget()
        container_widget.setLayout(desc_container)
        
        form_layout.addRow(desc_label, container_widget)
    
    def check_desc_length(self):
        """Kiểm tra và giới hạn độ dài của trường mô tả"""
        text = self.desc_field.toPlainText()
        length = len(text)
        
        # Cập nhật nhãn đếm ký tự
        if length <= 255:
            self.char_count_label.setText(f"{length}/255 ký tự")
            self.char_count_label.setStyleSheet("color: #888; font-size: 10pt;")
        else:
            # Nếu vượt quá giới hạn, hiển thị màu đỏ
            self.char_count_label.setText(f"{length}/255 ký tự - Tối đa 255 kí tự!")
            self.char_count_label.setStyleSheet("color: red; font-size: 10pt;")
            
            # Cắt bớt văn bản xuống 255 ký tự
            truncated_text = text[:255]
            
            # Ngăn đệ quy bằng cách ngắt kết nối và kết nối lại
            self.desc_field.textChanged.disconnect(self.check_desc_length)
            self.desc_field.setPlainText(truncated_text)
            self.desc_field.textChanged.connect(self.check_desc_length)
            
            # Đặt con trỏ ở cuối văn bản
            cursor = self.desc_field.textCursor()
            cursor.movePosition(QTextCursor.MoveOperation.End)
            self.desc_field.setTextCursor(cursor)
    
    def create_status_field(self, form_layout):
        """Tạo trường trạng thái (combobox)"""
        status_label = QLabel("👁️ Trạng thái:")
        status_label.setFont(QFont("Arial", 13))
        
        self.status_field = QComboBox()
        self.status_field.addItem("Hiển thị", True)
        self.status_field.addItem("Ẩn", False)
        self.status_field.setStyleSheet("""
            QComboBox {
                padding: 8px;
                border: 1px solid #ddd;
                border-radius: 4px;
                font-size: 13pt;
                min-width: 150px;
            }
        """)
        
        form_layout.addRow(status_label, self.status_field)
    
    def create_date_field(self, form_layout):
        """Tạo trường ngày tạo (chỉ đọc)"""
        date_label = QLabel("📅 Ngày tạo:")
        date_label.setFont(QFont("Arial", 13))
        
        self.date_field = QLineEdit()
        self.date_field.setReadOnly(True)
        current_date = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        self.date_field.setText(current_date)
        self.date_field.setStyleSheet("""
            QLineEdit {
                background-color: #f5f5f5;
                padding: 8px;
                border: 1px solid #ddd;
                border-radius: 4px;
                font-size: 13pt;
            }
        """)
        
        form_layout.addRow(date_label, self.date_field)
    
    def create_image_selection(self, form_layout):
        """Tạo phần chọn ảnh"""
        image_label = QLabel("🖼️ Ảnh:")
        image_label.setFont(QFont("Arial", 13))
        
        # Container cho ảnh
        image_container = QWidget()
        container_layout = QVBoxLayout(image_container)
        container_layout.setContentsMargins(0, 0, 0, 0)
        
        # Tiêu đề phụ cho phần ảnh
        image_title = QLabel("🎨 Chọn ảnh đại diện cho danh sách phát")
        image_title.setStyleSheet("color: #555; font-size: 10pt;")
        container_layout.addWidget(image_title, alignment=Qt.AlignmentFlag.AlignCenter)
        
        # Preview ảnh
        self.image_preview = QLabel()
        self.image_preview.setFixedSize(200, 200)  # Tăng kích thước phần hiển thị ảnh
        self.image_preview.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_preview.setStyleSheet("""
            border: 2px dashed #ccc; 
            background-color: #f9f9f9;
            border-radius: 5px;
        """)
        self.image_preview.setText("Chưa có ảnh")
        
        # Nút chọn ảnh
        self.choose_image_btn = QPushButton("📷 Chọn ảnh")
        self.choose_image_btn.setStyleSheet("""
            QPushButton {
                background-color: #2196F3;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
                font-size: 13pt;
            }
            QPushButton:hover {
                background-color: #1976D2;
            }
        """)
        self.choose_image_btn.clicked.connect(self.choose_image)
        
        container_layout.addWidget(self.image_preview, alignment=Qt.AlignmentFlag.AlignCenter)
        container_layout.addWidget(self.choose_image_btn, alignment=Qt.AlignmentFlag.AlignCenter)
        
        # Ghi chú về ảnh
        image_note = QLabel("📌 Định dạng hỗ trợ: PNG, JPG, JPEG, BMP")
        image_note.setStyleSheet("color: #888; font-size: 9pt; font-style: italic;")
        container_layout.addWidget(image_note, alignment=Qt.AlignmentFlag.AlignCenter)
        
        form_layout.addRow(image_label, image_container)
    
    def choose_image(self):
        """Mở hộp thoại chọn ảnh"""
        file_dialog = QFileDialog(self)
        file_dialog.setWindowTitle("Chọn ảnh cho danh sách phát")
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        file_dialog.setNameFilter("Ảnh (*.png *.jpg *.jpeg *.bmp)")
        
        if file_dialog.exec() == QDialog.DialogCode.Accepted:
            selected_file = file_dialog.selectedFiles()[0]
            self.image_path = selected_file
            
            # Hiển thị ảnh xem trước
            pixmap = QPixmap(selected_file)
            if not pixmap.isNull():
                pixmap = pixmap.scaled(190, 190, Qt.AspectRatioMode.KeepAspectRatio)
                self.image_preview.setPixmap(pixmap)
                self.image_preview.setText("")
            else:
                QMessageBox.warning(self, "Lỗi", "Không thể tải ảnh đã chọn!")
    
    def create_buttons(self, layout):
        """Tạo các nút ở dưới cùng"""
        # Nút hủy
        self.cancel_btn = QPushButton("❌ Hủy")
        self.cancel_btn.setStyleSheet("""
            QPushButton {
                background-color: #f44336;
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 4px;
                font-size: 12pt;
            }
            QPushButton:hover {
                background-color: #d32f2f;
            }
        """)
        self.cancel_btn.clicked.connect(self.reject)
        
        # Nút lưu
        self.save_btn = QPushButton("💾 Lưu")
        self.save_btn.setStyleSheet("""
            QPushButton {
                background-color: #4CAF50;
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 4px;
                font-size: 12pt;
            }
            QPushButton:hover {
                background-color: #388E3C;
            }
        """)
        self.save_btn.clicked.connect(self.save_data)
        
        # Thêm nút vào layout
        layout.addStretch()
        layout.addWidget(self.cancel_btn)
        layout.addWidget(self.save_btn)
    
    def save_data(self):
        # Validate dữ liệu
        if not self.validate_data():
            return
        
        # Lấy dữ liệu từ form
        title = self.title_field.text().strip()
        desc = self.desc_field.toPlainText().strip()
        status = self.status_field.currentData()  # True/False
        
        # Tạo đối tượng dữ liệu - chưa có ảnh
        data = {
            "TieuDe": title,
            "MoTa": desc,
            "TrangThai": status,
            "Anh": None,
            "NgayTao": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
        
        try:
            # Thêm danh sách phát trước để lấy ID
            new_id = self.bll.them_danh_sach_phat(data)
            
            if not new_id:
                QMessageBox.warning(self, "Thất bại", "Không thể thêm danh sách phát. Vui lòng thử lại!")
                return
                
            # Xử lý và lưu ảnh với ID mới
            image_path_to_save = None
            if self.image_path:
                try:
                    image_path_to_save = self.save_image(new_id)
                    
                    # Cập nhật đường dẫn ảnh vào bản ghi đã tạo
                    if image_path_to_save:
                        update_result = self.bll.cap_nhat_anh_danh_sach_phat(new_id, image_path_to_save)
                        if not update_result:
                            print(f"Cảnh báo: Không thể cập nhật đường dẫn ảnh cho danh sách phát ID {new_id}")
                except Exception as e:
                    print(f"Lỗi khi lưu ảnh: {str(e)}")
                    # Vẫn cho phép tiếp tục nếu ảnh lỗi
            
            QMessageBox.information(self, "Thành công", f"Đã thêm danh sách phát mới với ID: {new_id}!")
            self.accept()  # Đóng dialog với kết quả Accepted
            
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Lỗi khi lưu danh sách phát: {str(e)}")
    
    def validate_data(self):
        # Kiểm tra tiêu đề
        title = self.title_field.text().strip()
        if not title:
            QMessageBox.warning(self, "Thiếu thông tin", "Vui lòng nhập tiêu đề cho danh sách phát!")
            self.title_field.setFocus()
            return False
        
        # Kiểm tra trùng tiêu đề - cách kiểm tra tiêu đề có trong danh sách hay không
        if title in self.ds_tieu_de:
            QMessageBox.warning(self, "Dữ liệu không hợp lệ", 
                            f"Tiêu đề '{title}' đã tồn tại!\nVui lòng chọn tiêu đề khác.")
            self.title_field.setFocus()
            return False
        
        # Kiểm tra độ dài mô tả
        desc_length = len(self.desc_field.toPlainText().strip())
        if desc_length > 255:
            QMessageBox.warning(self, "Dữ liệu không hợp lệ", "Mô tả không được vượt quá 255 ký tự!")
            self.desc_field.setFocus()
            return False
        
        return True
    
    def save_image(self, list_id=None):
        if not self.image_path:
            return None
        
        # Kiểm tra định dạng file
        valid_extensions = ['.png', '.jpg', '.jpeg', '.bmp']
        file_extension = os.path.splitext(self.image_path)[1].lower()
        
        if file_extension not in valid_extensions:
            raise ValueError(f"Định dạng file không được hỗ trợ. Chỉ chấp nhận: {', '.join(valid_extensions)}")
        
        # Sử dụng ID được truyền vào hoặc lấy từ field
        if list_id is None:
            try:
                list_id = self.id_field.text().strip()
                if not list_id or list_id == "Auto" or list_id == "Tự động":
                    # Sử dụng timestamp nếu không có ID
                    list_id = f"temp_{int(datetime.now().timestamp())}"
            except:
                list_id = f"temp_{int(datetime.now().timestamp())}"
        
        # Thư mục lưu ảnh
        destination_folder = "assets/DanhSachPhatHeThong"
        
        # Tạo thư mục nếu chưa tồn tại
        os.makedirs(destination_folder, exist_ok=True)
        
        # Tạo tên file mới dựa trên ID danh sách
        new_filename = f"{list_id}{file_extension}"
        
        # Đường dẫn đầy đủ cho file mới
        destination_path = os.path.join(destination_folder, new_filename)
        
        # Kiểm tra xem file đã tồn tại chưa
        if os.path.exists(destination_path):
            # Nếu đã tồn tại, xóa file cũ
            try:
                os.remove(destination_path)
                print(f"Đã xóa file ảnh cũ: {destination_path}")
            except Exception as e:
                print(f"Không thể xóa file ảnh cũ: {e}")
        
        # Copy file ảnh mới
        shutil.copy2(self.image_path, destination_path)
        print(f"Đã lưu ảnh với tên: {new_filename}")
        
        # Trả về đường dẫn tương đối để lưu vào DB
        return destination_path.replace("\\", "/")
    
if __name__ == "__main__":
    import sys
    from PyQt6.QtWidgets import QApplication
    
    app = QApplication(sys.argv)
    
    window = GUIThemDanhSachPhatHeThong()
    window.show()
    
    sys.exit(app.exec())