from datetime import datetime
from DAL.dbconnector import Database
from DTO.DTODanhSachPhat import DTODanhSachPhat
class DALPhatNhac:
    def __init__(self):
        db = Database()
        self.conn = db.get_connection()
        self.cursor = db.get_cursor()
    
    def luuLichSuNghe(self, idbaihat, idnguoidung):
        thoi_gian = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        try:
            query = """
                INSERT INTO LuotNghe (MaNguoiDung, MaBaiHat, ThoiGian)
                VALUES (%s, %s, %s)
            """
            self.cursor.execute(query, (idnguoidung, idbaihat, thoi_gian))
            self.conn.commit()
        except Exception as e:
            print("Lỗi khi lưu lịch sử nghe:", e)
        
    def kiemTraTimBaiHat(self, idnguoidung: int, idbaihat: int):
        try:
            query = """
                SELECT 1 FROM YeuThich
                WHERE MaNguoiDung = %s AND MaBaiHat = %s
                LIMIT 1
            """
            self.cursor.execute(query, (idnguoidung, idbaihat))
            result = self.cursor.fetchone()
            return result is not None
        except Exception as e:
            print("Lỗi khi kiểm tra bài hát yêu thích:", e)
            return False
    def timBaiHat(self, idnguoidung: int, idbaihat: int):
        try:
            ngay_them = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            query = """
                INSERT INTO YeuThich (MaNguoiDung, MaBaiHat, NgayThem)
                VALUES (%s, %s, %s)
            """
            self.cursor.execute(query, (idnguoidung, idbaihat, ngay_them))
            self.conn.commit()
        except Exception as e:
            print("Lỗi khi thêm bài hát vào yêu thích:", e)
    
    def huyTimBaiHat(self, idnguoidung: int, idbaihat: int):
        try:
            query = """
                DELETE FROM YeuThich
                WHERE MaNguoiDung = %s AND MaBaiHat = %s
            """
            self.cursor.execute(query, (idnguoidung, idbaihat))
            self.conn.commit()
        except Exception as e:
            print("Lỗi khi xóa bài hát khỏi yêu thích:", e)


    def layDanhSachPhat(self, idnguoidung: int):
        playlists = []
        print("ID Người Dùng:", idnguoidung)
        try:
            query = """
                SELECT MaDanhSachPhat, TieuDe, MoTa, NgayTao, MaNguoiDung, Anh
                FROM DanhSachPhat
                WHERE MaNguoiDung = %s
            """
            self.cursor.execute(query, (idnguoidung,))
            rows = self.cursor.fetchall()

            for row in rows:
                ma_danh_sach_phat = row['MaDanhSachPhat']
                tieu_de = row['TieuDe']
                mo_ta = row['MoTa']
                ngay_tao = row['NgayTao']
                ma_nguoi_dung = row['MaNguoiDung']
                anh = row['Anh']

                print("MaDanhSachPhat:", ma_danh_sach_phat, "TieuDe:", tieu_de, "MoTa:", mo_ta, "NgayTao:", ngay_tao, "MaNguoiDung:", ma_nguoi_dung, "Anh:", anh)

                dto = DTODanhSachPhat(
                    ma_danh_sach_phat=ma_danh_sach_phat,
                    tieu_de=tieu_de,
                    mo_ta=mo_ta,
                    ngay_tao=ngay_tao,
                    ma_nguoi_dung=ma_nguoi_dung,
                    anh=anh
                )
                playlists.append(dto)
            return playlists
        except Exception as e:
            print("Lỗi khi lấy danh sách phát:", e)
            return []

        
    def themBaiHatVaoDanhSachPhat(self, idbaihat: int, iddanh_sach_phat: int):
        try:
            query = """
                INSERT INTO ChiTietDanhSachPhat (MaBaiHat, MaDanhSachPhat)
                VALUES (%s, %s)
            """
            self.cursor.execute(query, (idbaihat, iddanh_sach_phat))
            self.conn.commit()
        except Exception as e:
            print("Lỗi khi thêm bài hát vào danh sách phát:", e)
    
    def taoDanhSachPhat(self, tieu_de: str, mo_ta: str, idnguoidung: int, anh: str):
        print("Tạo danh sách phát với tiêu đề:", tieu_de, "Mô tả:", mo_ta, "ID người dùng:", idnguoidung, "Ảnh:", anh)
        try:
            query = """
                INSERT INTO DanhSachPhat (TieuDe, MoTa, NgayTao, MaNguoiDung, Anh)
                VALUES (%s, %s, NOW(), %s, %s)
            """
            self.cursor.execute(query, (tieu_de, mo_ta, idnguoidung, anh))
            self.conn.commit()
            return self.cursor.lastrowid  # Trả về ID mới thêm
        except Exception as e:
            print("Lỗi khi thêm danh sách phát:", e)
    
    def layMaDanhSachPhat(self):
        try:
            query = """
                SELECT MAX(MaDanhSachPhat) AS MaxMaDanhSachPhat FROM DanhSachPhat
            """
            self.cursor.execute(query)
            result = self.cursor.fetchone()
            return result['MaxMaDanhSachPhat'] + 1 if result else None
        except Exception as e:
            print("Lỗi khi lấy mã danh sách phát lớn nhất:", e)
            return None
