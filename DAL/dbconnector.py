import mysql.connector

class Database:
    _instance = None  # Biến static để lưu instance

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance._connect()
        return cls._instance

    def _connect(self):
        """Kết nối CSDL chỉ chạy một lần."""
        try:
            self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="phatnhac"
            )
            self.cursor = self.connection.cursor(dictionary=True)
            print("Kết nối MySQL thành công!")
        except mysql.connector.Error as e:
            print("Lỗi kết nối:", e)
            self.connection = None
            self.cursor = None

    def get_connection(self):
        """Trả về kết nối CSDL."""
        return self.connection

    def get_cursor(self):
        """Trả về con trỏ CSDL."""
        return self.cursor

    def close_connection(self):
        """Đóng kết nối khi không cần thiết nữa."""
        if self.connection and self.connection.is_connected():
            self.cursor.close()
            self.connection.close()
            Database._instance = None  # Reset để có thể tạo lại nếu cần
            print("Đã đóng kết nối MySQL")
