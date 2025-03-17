import mysql.connector

try:
    # Kết nối tới MySQL
    connection = mysql.connector.connect(
        host="localhost",        # Địa chỉ máy chủ MySQL
        user="root",             # Tên người dùng MySQL
        password="",       # Mật khẩu MySQL
        database="phatnhac"        # Tên Database
    )

    if connection.is_connected():
        print("Kết nối thành công!")
        
except mysql.connector.Error as e:
    print("Lỗi:", e)

finally:
    if 'connection' in locals() and connection.is_connected():
        connection.close()
        print("Đã đóng kết nối")