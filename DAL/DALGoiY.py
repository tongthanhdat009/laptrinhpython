from DAL.dbconnector import Database
class DALGoiY:
    def __init__(self):
        db = Database()
        self.conn = db.get_connection()
        self.cursor = db.get_cursor()
    def layDiemTheLoai(self, idnguoidung: int):
        try:
            query = """
                SELECT BaiHat.MaTheLoai, COUNT(*) AS diemtheloai
                FROM (
                    SELECT *
                    FROM LuotNghe
                    WHERE MaNguoiDung = %s
                    ORDER BY ThoiGian DESC
                    LIMIT 50
                ) AS Top50
                JOIN BaiHat ON Top50.MaBaiHat = BaiHat.MaBaiHat
                GROUP BY BaiHat.MaTheLoai
            """
            self.cursor.execute(query, (idnguoidung,))
            results = self.cursor.fetchall()
            return {row["MaTheLoai"]: row["diemtheloai"] for row in results}
        except Exception as e:
            print("Lỗi khi lấy điểm thể loại:", e)
            return {}
    def layDiemXuatXu(self, idnguoidung: int):
        try:
            query = """
                SELECT BaiHat.MaXuatXu, COUNT(*) AS diemxuatxu
                FROM (
                    SELECT *
                    FROM LuotNghe
                    WHERE MaNguoiDung = %s
                    ORDER BY ThoiGian DESC
                    LIMIT 50
                ) AS Top50
                JOIN BaiHat ON Top50.MaBaiHat = BaiHat.MaBaiHat
                GROUP BY BaiHat.MaXuatXu
            """
            self.cursor.execute(query, (idnguoidung,))
            results = self.cursor.fetchall()
            return {row["MaXuatXu"]: row["diemxuatxu"] for row in results}
        except Exception as e:
            print("Lỗi khi lấy điểm xuất xứ:", e)
            return {}
    def layDiemCaSi(self, idnguoidung: int):
        try:
            query = """
                SELECT ThucHien.MaCaSi, COUNT(*) AS diemcasi
                FROM (
                    SELECT *
                    FROM LuotNghe
                    WHERE MaNguoiDung = %s
                    ORDER BY ThoiGian DESC
                    LIMIT 50
                ) AS Top50
                JOIN BaiHat ON Top50.MaBaiHat = BaiHat.MaBaiHat
                JOIN ThucHien ON BaiHat.MaBaiHat = ThucHien.MaBaiHat
                GROUP BY ThucHien.MaCaSi
            """
            self.cursor.execute(query, (idnguoidung,))
            results = self.cursor.fetchall()
            return {row["MaCaSi"]: row["diemcasi"] for row in results}
        except Exception as e:
            print("Lỗi khi lấy điểm ca sĩ:", e)
            return {}
        
    def layMaBaiHat(self):
        try:
            query = "SELECT MaBaiHat FROM BaiHat"
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            # Trả về danh sách mã bài hát
            return [row["MaBaiHat"] for row in results]
        except Exception as e:
            print("Lỗi khi lấy mã bài hát:", e)
            return []
