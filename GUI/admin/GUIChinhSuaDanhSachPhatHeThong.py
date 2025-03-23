import sys
import os
import shutil
from datetime import datetime, date
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt, pyqtSignal
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from BLL.BLLQuanLyDanhSachPhatHeThong import BLLQuanLyDanhSachPhatHeThong

class GUIChinhSuaDanhSachPhatHeThong(QDialog):
    dataChanged = pyqtSignal(bool)
    
    def __init__(self, ma_danh_sach=None, parent=None, callback=None):
        super().__init__(parent)
        self.ma_danh_sach = ma_danh_sach
        self.bll = BLLQuanLyDanhSachPhatHeThong()
        self.danh_sach = None
        self.new_image_path = None
        self.is_data_changed = False
        self. callback = callback
        
        # Tải thông tin danh sách phát
        self.load_danh_sach_phat()
        
        # Thiết lập UI
        self.setupUI()
        
        # Điều chỉnh cửa sổ
        self.setWindowTitle("📝 Chỉnh sửa Danh sách phát")
        self.setMinimumSize(600, 500)
        self.setModal(True)
        
        # Căn giữa trên cửa sổ cha (nếu có)
        if parent:
            self.center_on_parent()
    
    def load_danh_sach_phat(self):
        """Tải thông tin danh sách phát từ cơ sở dữ liệu"""
        try:
            if self.ma_danh_sach:
                self.danh_sach = self.bll.lay_danh_sach_phat_he_thong_theo_ma(self.ma_danh_sach)
                if not self.danh_sach:
                    raise Exception(f"Không tìm thấy danh sách phát có mã {self.ma_danh_sach}")
        except Exception as e:
            QMessageBox.critical(self, "Lỗi", f"Không thể tải thông tin danh sách phát: {str(e)}")
            print(f"Lỗi khi tải danh sách phát: {e}")
            self.reject()
    
    def setupUI(self):
        """Thiết lập giao diện người dùng"""
        # Layout chính
        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(15)
        
        # Thêm tiêu đề
        self.setup_title(main_layout)
        
        # Container cho ảnh và thông tin
        content_widget = QWidget()
        content_layout = QHBoxLayout(content_widget)
        content_layout.setContentsMargins(0, 0, 0, 0)
        content_layout.setSpacing(20)
        
        # Thiết lập panel hình ảnh (bên trái)
        image_panel = self.setup_image_panel()
        content_layout.addWidget(image_panel)
        
        # Thiết lập panel thông tin (bên phải)
        info_panel = self.setup_info_panel()
        content_layout.addWidget(info_panel, 1)  # Cho phép info_panel mở rộng
        
        main_layout.addWidget(content_widget)
        
        # Thêm đường phân cách
        self.add_separator(main_layout)
        
        # Thêm nút điều khiển
        self.setup_buttons(main_layout)
    
    def setup_title(self, parent_layout):
        """Thiết lập tiêu đề dialog"""
        title_label = QLabel("📋 Chỉnh sửa thông tin danh sách phát")
        title_label.setFont(QFont("Arial", 16, QFont.Weight.Bold))
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title_label.setStyleSheet("color: #2196F3; margin-bottom: 10px;")
        parent_layout.addWidget(title_label)
    
    def setup_image_panel(self):
        """Thiết lập panel hiển thị và quản lý ảnh"""
        image_panel = QWidget()
        image_layout = QVBoxLayout(image_panel)
        image_layout.setContentsMargins(0, 0, 0, 0)
        image_layout.setSpacing(10)
        
        # Khung ảnh
        self.image_frame = QLabel()
        self.image_frame.setFixedSize(200, 200)
        self.image_frame.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.image_frame.setStyleSheet("""
            QLabel {
                background-color: #f5f5f5;
                border: 2px dashed #bdbdbd;
                border-radius: 10px;
            }
        """)
        
        # Tải ảnh từ danh sách phát
        if self.danh_sach and hasattr(self.danh_sach, 'Anh') and self.danh_sach.Anh:
            self.load_image(self.danh_sach.Anh)
        else:
            self.image_frame.setText("Không có ảnh")
        
        image_layout.addWidget(self.image_frame, alignment=Qt.AlignmentFlag.AlignCenter)
        
        # Nút chọn ảnh
        select_image_button = self.create_button(
            "🖼️ Chọn ảnh khác", 
            "#4CAF50", "#388E3C", 
            self.select_image
        )
        image_layout.addWidget(select_image_button)
        
        # Nút xóa ảnh
        remove_image_button = self.create_button(
            "🗑️ Xóa ảnh", 
            "#F44336", "#D32F2F", 
            self.remove_image
        )
        image_layout.addWidget(remove_image_button)
        
        # Thêm stretch để các nút không bị kéo giãn
        image_layout.addStretch()
        
        return image_panel
    
    def setup_info_panel(self):
        """Thiết lập panel thông tin danh sách phát"""
        info_panel = QWidget()
        info_layout = QFormLayout(info_panel)
        info_layout.setContentsMargins(0, 0, 0, 0)
        info_layout.setSpacing(15)
        
        # Mã danh sách (chỉ đọc)
        self.id_field = self.create_read_only_field(
            self.get_danh_sach_attr("MaDanhSach") or self.get_danh_sach_attr("MaDanhSachPhat") or ""
        )
        id_label = self.create_form_label("Mã danh sách:")
        info_layout.addRow(id_label, self.id_field)
        
        # Tiêu đề
        self.title_field = self.create_edit_field(self.get_danh_sach_attr("TieuDe") or "")
        title_label = self.create_form_label("Tiêu đề:")
        info_layout.addRow(title_label, self.title_field)
        
        # Mô tả (nhiều dòng)
        self.desc_field = self.create_text_edit(self.get_danh_sach_attr("MoTa") or "")
        desc_label = self.create_form_label("Mô tả:")
        info_layout.addRow(desc_label, self.desc_field)
        
        # Ngày tạo (chỉ đọc)
        self.created_date_field = self.create_read_only_field("")
        self.set_formatted_date(self.created_date_field, self.get_danh_sach_attr("NgayTao"))
        created_date_label = self.create_form_label("Ngày tạo:")
        info_layout.addRow(created_date_label, self.created_date_field)
        
        # Trạng thái
        self.status_combo = self.create_status_combo()
        status_label = self.create_form_label("Trạng thái:")
        info_layout.addRow(status_label, self.status_combo)
        
        return info_panel
    
    def get_danh_sach_attr(self, attr_name):
        """Lấy thuộc tính từ đối tượng danh sách nếu có"""
        if self.danh_sach and hasattr(self.danh_sach, attr_name):
            return getattr(self.danh_sach, attr_name)
        return None
    
    def create_form_label(self, text):
        """Tạo nhãn cho form"""
        label = QLabel(text)
        label.setFont(QFont("Arial", 12))
        return label
    
    def create_read_only_field(self, text):
        """Tạo trường nhập liệu chỉ đọc"""
        field = QLineEdit(str(text))
        field.setReadOnly(True)
        field.setStyleSheet("""
            QLineEdit {
                padding: 8px;
                background-color: #f5f5f5;
                border: 1px solid #ddd;
                border-radius: 4px;
                font-size: 14px;
            }
        """)
        return field
    
    def create_edit_field(self, text):
        """Tạo trường nhập liệu có thể chỉnh sửa"""
        field = QLineEdit(str(text))
        field.setStyleSheet("""
            QLineEdit {
                padding: 8px;
                border: 1px solid #ddd;
                border-radius: 4px;
                font-size: 14px;
            }
            QLineEdit:focus {
                border: 1px solid #2196F3;
            }
        """)
        return field
    
    def create_text_edit(self, text):
        """Tạo trường văn bản nhiều dòng"""
        text_edit = QTextEdit(str(text))
        text_edit.setStyleSheet("""
            QTextEdit {
                padding: 8px;
                border: 1px solid #ddd;
                border-radius: 4px;
                font-size: 14px;
                min-height: 100px;
            }
            QTextEdit:focus {
                border: 1px solid #2196F3;
            }
        """)
        return text_edit
    
    def create_status_combo(self):
        """Tạo combobox trạng thái"""
        combo = QComboBox()
        combo.addItems(["Hiển thị", "Ẩn"])
        
        # Thiết lập trạng thái hiện tại
        if self.danh_sach and hasattr(self.danh_sach, 'TrangThai'):
            index = 1 if self.danh_sach.TrangThai == 0 else 0
            combo.setCurrentIndex(index)
            
        combo.setStyleSheet("""
            QComboBox {
                padding: 8px;
                border: 1px solid #ddd;
                border-radius: 4px;
                font-size: 14px;
            }
            QComboBox:focus {
                border: 1px solid #2196F3;
            }
        """)
        return combo
    
    def set_formatted_date(self, field, date_value):
        """Định dạng và thiết lập giá trị ngày tháng cho trường nhập liệu"""
        formatted_date = self.format_date(date_value)
        field.setText(formatted_date)
    
    def format_date(self, date_value):
        """Hàm trợ giúp để định dạng ngày tháng từ nhiều định dạng khác nhau"""
        if not date_value:
            return datetime.now().strftime("%d/%m/%Y")
            
        try:
            if isinstance(date_value, str):
                # Thử nhiều định dạng chuỗi khác nhau
                for fmt in ["%Y-%m-%d", "%d/%m/%Y", "%m/%d/%Y", "%Y/%m/%d"]:
                    try:
                        date_obj = datetime.strptime(date_value, fmt)
                        return date_obj.strftime("%d/%m/%Y")
                    except ValueError:
                        continue
                # Nếu không định dạng nào khớp
                return date_value
            
            elif isinstance(date_value, (datetime, date)):
                # Nếu đã là đối tượng date hoặc datetime
                return date_value.strftime("%d/%m/%Y")
            
            else:
                # Trường hợp khác
                return str(date_value)
        
        except Exception as e:
            print(f"Lỗi khi định dạng ngày: {e}")
            return str(date_value)
    
    def add_separator(self, parent_layout):
        """Thêm đường phân cách vào layout"""
        separator = QFrame()
        separator.setFrameShape(QFrame.Shape.HLine)
        separator.setFrameShadow(QFrame.Shadow.Sunken)
        separator.setStyleSheet("background-color: #e0e0e0;")
        parent_layout.addWidget(separator)
    
    def setup_buttons(self, parent_layout):
        """Thiết lập các nút thao tác"""
        button_layout = QHBoxLayout()
        button_layout.setContentsMargins(0, 0, 0, 0)
        button_layout.setSpacing(10)
        
        # Nút Hủy
        cancel_button = self.create_button(
            "🚫 Hủy", 
            "#f44336", "#d32f2f", 
            self.reject,
            True  # font đậm
        )
        
        # Nút Lưu
        save_button = self.create_button(
            "💾 Lưu thay đổi", 
            "#2196F3", "#1976D2", 
            self.save_changes,
            True  # font đậm
        )
        
        button_layout.addStretch(1)
        button_layout.addWidget(cancel_button)
        button_layout.addWidget(save_button)
        
        parent_layout.addLayout(button_layout)
    
    def create_button(self, text, bg_color, hover_color, callback, is_bold=False):
        """Tạo nút với kiểu dáng nhất định"""
        button = QPushButton(text)
        font_size = 12
        font = QFont("Arial", font_size)
        if is_bold:
            font.setBold(True)
        button.setFont(font)
        button.setStyleSheet(f"""
            QPushButton {{
                background-color: {bg_color};
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 4px;
            }}
            QPushButton:hover {{
                background-color: {hover_color};
            }}
        """)
        button.clicked.connect(callback)
        return button
    
    def load_image(self, image_path):
        """Tải và hiển thị ảnh từ đường dẫn"""
        if not image_path:
            self.image_frame.setText("Không có ảnh")
            return
        
        # Chuẩn hóa đường dẫn
        normalized_path = self.normalize_path(image_path)
        
        # Tải ảnh từ đường dẫn
        pixmap = QPixmap(normalized_path)
        
        if not pixmap.isNull():
            # Thay đổi kích thước ảnh để vừa với khung
            pixmap = pixmap.scaled(
                self.image_frame.width() - 10, 
                self.image_frame.height() - 10,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation
            )
            self.image_frame.setPixmap(pixmap)
        else:
            print(f"Không thể tải ảnh từ: {normalized_path}")
            self.image_frame.setText("Không thể tải ảnh")
    
    def normalize_path(self, image_path):
        """Chuẩn hóa đường dẫn ảnh"""
        if not image_path:
            return None
            
        # Đảm bảo đường dẫn sử dụng dấu \ trên hệ thống Windows
        normalized_path = image_path.replace("/", "\\")
        
        # Xử lý đường dẫn tương đối
        if normalized_path.startswith("\\") or normalized_path.startswith("..") or normalized_path.startswith(".\\") or normalized_path.startswith("./"):
            current_dir = os.path.dirname(os.path.abspath(__file__))
            project_root = os.path.dirname(os.path.dirname(current_dir))
            
            if normalized_path.startswith("\\"):
                normalized_path = normalized_path[1:]  
                normalized_path = os.path.normpath(os.path.join(project_root, normalized_path))
            else:
                normalized_path = os.path.normpath(os.path.join(current_dir, normalized_path))
        
        # Xử lý đường dẫn không có phần gốc (như assets\DanhSachPhatHeThong\2.png)
        elif not os.path.isabs(normalized_path):
            current_dir = os.path.dirname(os.path.abspath(__file__))
            project_root = os.path.dirname(os.path.dirname(current_dir))
            normalized_path = os.path.normpath(os.path.join(project_root, normalized_path))
        
        return normalized_path
    
    def select_image(self):
        """Chọn ảnh mới từ hệ thống tệp"""
        file_dialog = QFileDialog(self)
        file_dialog.setWindowTitle("Chọn ảnh")
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        file_dialog.setNameFilter("Ảnh (*.png *.jpg *.jpeg *.bmp *.gif)")
        
        if file_dialog.exec() == QDialog.DialogCode.Accepted:
            selected_files = file_dialog.selectedFiles()
            if selected_files:
                self.new_image_path = selected_files[0]
                self.load_image(self.new_image_path)
                print(f"Đã chọn ảnh: {self.new_image_path}")
    
    def remove_image(self):
        """Xóa ảnh hiện tại"""
        self.new_image_path = ""  # Đánh dấu xóa ảnh
        self.image_frame.clear()
        self.image_frame.setText("Không có ảnh")
        print("Đã xóa ảnh")
    
    def save_changes(self):
        """Lưu các thay đổi vào cơ sở dữ liệu"""
        if not self.danh_sach:
            QMessageBox.warning(self, "Cảnh báo", "Không có dữ liệu danh sách phát để cập nhật!")
            return
        
        # Kiểm tra dữ liệu nhập vào
        title = self.title_field.text().strip()
        desc = self.desc_field.toPlainText().strip()
        
        if not title:
            QMessageBox.warning(self, "Cảnh báo", "Vui lòng nhập tiêu đề danh sách phát!")
            self.title_field.setFocus()
            return
        
        if len(title) > 255:
            QMessageBox.warning(
                self,
                "Lỗi",
                "Tiêu đề không được vượt quá 255 ký tự!",
                QMessageBox.StandardButton.Ok
            )
            return
        
        if len(desc) > 255:
            QMessageBox.warning(
                self,
                "Lỗi",
                "Mô tả không được vượt quá 255 ký tự!",
                QMessageBox.StandardButton.Ok
            )
            return
        
        try:
            # Hiển thị dialog xác nhận nếu có sự thay đổi ảnh
            if self.new_image_path is not None:
                if self.new_image_path == "":
                    # Xác nhận xóa ảnh
                    if not self.confirm_action("Xác nhận xóa ảnh", 
                                            "Bạn có chắc chắn muốn xóa ảnh của danh sách phát này?"):
                        return
                else:
                    # Xác nhận thay đổi ảnh
                    existing_image = self.check_existing_image()
                    if existing_image and not self.confirm_action("Xác nhận ghi đè ảnh", 
                                                                f"Ảnh của danh sách phát đã tồn tại ({existing_image}).\nBạn có muốn ghi đè lên ảnh hiện tại?"):
                        return
            
            # Chuẩn bị dữ liệu cập nhật
            update_data = self.prepare_update_data(title, desc)
            
            # Xử lý ảnh nếu có sự thay đổi
            self.process_image_update(update_data)
            print(f"Kết quả cập nhật: {update_data}")
            
            # Gọi BLL để cập nhật
            result = self.bll.cap_nhat_danh_sach_phat(update_data)
            
            if result:
                self.handle_save_success()
            else:
                self.handle_save_failure()
                
        except Exception as e:
            self.handle_save_error(e)

    def check_existing_image(self):
        """Kiểm tra xem ảnh của danh sách phát đã tồn tại chưa"""
        target_dir = os.path.join("assets", "DanhSachPhatHeThong")
        if os.path.exists(target_dir):
            for file in os.listdir(target_dir):
                if file.startswith(str(self.ma_danh_sach) + "."):
                    return file
        return None

    def confirm_action(self, title, message):
        """Hiển thị hộp thoại xác nhận và trả về kết quả"""
        reply = QMessageBox.question(
            self, title, message,
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
            QMessageBox.StandardButton.No
        )
        return reply == QMessageBox.StandardButton.Yes

    def prepare_update_data(self, title, desc):
        """Chuẩn bị dữ liệu cập nhật"""
        update_data = {
            "MaDanhSachPhatHeThong": self.ma_danh_sach,
            "TieuDe": title,
            "MoTa": desc,
            "TrangThai": 1 if self.status_combo.currentText() == "Hiển thị" else 0
        }
        
        # Thêm đường dẫn ảnh hiện tại nếu không có ảnh mới
        if self.new_image_path is None and self.danh_sach and hasattr(self.danh_sach, 'Anh'):
            current_image = self.danh_sach.Anh
            # Chuyển đổi dấu / thành \ nếu đường dẫn hiện tại sử dụng /
            if current_image and "/" in current_image:
                current_image = current_image.replace("/", "\\")
            update_data["Anh"] = current_image
                
        return update_data
        
    
    def process_image_update(self, update_data):
        """Xử lý cập nhật ảnh"""
        # Nếu không có sự thay đổi ảnh, giữ nguyên ảnh hiện tại
        if self.new_image_path is None:
            if self.danh_sach and hasattr(self.danh_sach, 'Anh'):
                update_data["Anh"] = self.danh_sach.Anh
            return
            
        # Nếu xóa ảnh
        if self.new_image_path == "":
            update_data["Anh"] = None
            self.remove_existing_image_file()
            return
            
        # Nếu có ảnh mới
        if os.path.exists(self.new_image_path):
            # Tạo thư mục lưu ảnh nếu chưa tồn tại
            target_dir = os.path.join("assets", "DanhSachPhatHeThong")
            os.makedirs(target_dir, exist_ok=True)
            
            # Lấy phần mở rộng của file mới
            _, file_ext = os.path.splitext(self.new_image_path)
            
            # Xóa các file ảnh cũ với cùng mã danh sách
            self.remove_existing_image_file()
            
            # Tạo tên file mới dựa trên mã danh sách và định dạng mới
            new_filename = f"{self.ma_danh_sach}{file_ext}"
            target_path = os.path.join(target_dir, new_filename)
            
            # Sao chép file ảnh mới vào thư mục đích
            print(f"Sao chép ảnh từ {self.new_image_path} đến {target_path}")
            shutil.copy2(self.new_image_path, target_path)
            
            # Cập nhật đường dẫn ảnh trong dữ liệu cập nhật với định dạng backslash
            db_image_path = f"assets\\DanhSachPhatHeThong\\{self.ma_danh_sach}{file_ext}"
            update_data["Anh"] = db_image_path
            print(f"Đường dẫn ảnh mới: {update_data['Anh']}")
    
    def remove_existing_image_file(self):
        """Xóa tất cả các file ảnh hiện có với mã danh sách này"""
        target_dir = os.path.join("assets", "DanhSachPhatHeThong")
        if os.path.exists(target_dir):
            for file in os.listdir(target_dir):
                # Kiểm tra nếu file bắt đầu bằng mã danh sách
                if file.startswith(str(self.ma_danh_sach) + "."):
                    # Đây là file ảnh của danh sách này
                    file_path = os.path.join(target_dir, file)
                    try:
                        print(f"Xóa file ảnh cũ: {file_path}")
                        os.remove(file_path)
                    except Exception as e:
                        print(f"Không thể xóa file ảnh cũ {file_path}: {e}")
    
    def handle_save_success(self):
        """Xử lý khi lưu thành công"""
        QMessageBox.information(
            self,
            "Thành công",
            "Cập nhật thông tin danh sách phát thành công!",
            QMessageBox.StandardButton.Ok
        )
        
        # Đánh dấu dữ liệu đã thay đổi
        self.is_data_changed = True
        
        # Phát signal trước khi đóng
        self.dataChanged.emit(True)
        
        # Đóng dialog
        self.accept()
    
    def handle_save_failure(self):
        """Xử lý khi lưu thất bại"""
        QMessageBox.warning(
            self,
            "Thất bại",
            "Không thể cập nhật thông tin danh sách phát. Vui lòng thử lại!",
            QMessageBox.StandardButton.Ok
        )
    
    def handle_save_error(self, error):
        """Xử lý khi có lỗi trong quá trình lưu"""
        QMessageBox.critical(
            self,
            "Lỗi",
            f"Đã xảy ra lỗi khi cập nhật thông tin: {str(error)}",
            QMessageBox.StandardButton.Ok
        )
        print(f"Lỗi khi cập nhật danh sách phát: {error}")
    
    def center_on_parent(self):
        """Căn giữa dialog so với cửa sổ cha hoặc màn hình"""
        if self.parent():
            # Căn giữa so với parent
            parent_rect = self.parent().geometry()
            x = parent_rect.x() + (parent_rect.width() - self.width()) // 2
            y = parent_rect.y() + (parent_rect.height() - self.height()) // 2
            
            # Đảm bảo dialog không ra ngoài màn hình
            screen_rect = QApplication.primaryScreen().availableGeometry()
            x = max(screen_rect.left(), min(x, screen_rect.right() - self.width()))
            y = max(screen_rect.top(), min(y, screen_rect.bottom() - self.height()))
            
            self.move(x, y)
        else:
            # Căn giữa màn hình nếu không có parent
            self.setGeometry(
                QStyle.alignedRect(
                    Qt.LayoutDirection.LeftToRight,
                    Qt.AlignmentFlag.AlignCenter,
                    self.size(),
                    QApplication.primaryScreen().availableGeometry()
                )
            )


if __name__ == "__main__":
    import sys
    from PyQt6.QtWidgets import QApplication
    
    app = QApplication(sys.argv)
    
    # Khởi tạo dialog với ID mẫu (ví dụ: 1)
    dialog = GUIChinhSuaDanhSachPhatHeThong(1)
    dialog.show()
    
    sys.exit(app.exec())