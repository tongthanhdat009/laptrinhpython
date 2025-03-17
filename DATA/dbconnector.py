import sys
import mysql.connector
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QTableWidget, QTableWidgetItem, QMessageBox

class MySQLApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Kết nối MySQL với PyQt6")
        self.setGeometry(100, 100, 600, 400)

        # Layout
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Nút tải dữ liệu
        self.load_button = QPushButton("Tải dữ liệu từ MySQL")
        self.load_button.clicked.connect(self.load_data)
        self.layout.addWidget(self.load_button)

        # Bảng hiển thị dữ liệu
        self.table = QTableWidget()
        self.layout.addWidget(self.table)

    def load_data(self):
        try:
            # Kết nối MySQL
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="phatnhac"
            )
            
            if connection.is_connected():
                print("✅ Kết nối thành công!")
                cursor = connection.cursor()

                # Truy vấn dữ liệu
                query = "SELECT * FROM BaiHat"
                cursor.execute(query)
                records = cursor.fetchall()

                # Hiển thị dữ liệu lên bảng
                self.table.setRowCount(len(records))
                self.table.setColumnCount(len(cursor.column_names))
                self.table.setHorizontalHeaderLabels(cursor.column_names)

                for row_idx, row_data in enumerate(records):
                    for col_idx, col_data in enumerate(row_data):
                        self.table.setItem(row_idx, col_idx, QTableWidgetItem(str(col_data)))

                cursor.close()
                connection.close()
        except mysql.connector.Error as e:
            QMessageBox.critical(self, "Lỗi MySQL", f"Lỗi: {e}")

# Chạy ứng dụng
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MySQLApp()
    window.show()
    sys.exit(app.exec())
