from DTO.DTOBaiHat import DTOBaiHat
from DAL.dbconnector import Database
import datetime
class DALBaiHat:
    def __init__(self):
        db = Database() # Lấy instance của Database
        self.conn = db.get_connection()
        self.cursor = db.get_cursor()

    def layTatCaBaiHat(self):
        self.cursor.execute("SELECT * FROM baihat, theloai, xuatxu WHERE BaiHat.MaTheLoai = TheLoai.MaTheLoai AND BaiHat.MaXuatXu = XuatXu.MaXuatXu")
        results = self.cursor.fetchall()
        danhSachBaiHat = []
        for row in results:
            baiHat = DTOBaiHat(
                MaBaiHat=row["MaBaiHat"],
                NgayPhatHanh=row["NgayPhatHanh"],
                TieuDe=row["TieuDe"],
                Anh=row["AnhBaiHat"],
                MaXuatXu=row["MaXuatXu"],
                TenXuatXu=row["TenXuatXu"],
                MaTheLoai=row["MaTheLoai"],
                TenTheLoai=row["TenTheLoai"],
                FileNhac=row["FileNhac"],
                CaSi=[]  # Chưa lấy danh sách ca sĩ
            )
            danhSachBaiHat.append(baiHat)
        return danhSachBaiHat
    
    def layTenCaSi(self, MaBaiHat: str):
        query = """
            SELECT CaSi.MaCaSi, CaSi.TenCaSi 
            FROM ThucHien
            JOIN CaSi ON ThucHien.MaCaSi = CaSi.MaCaSi
            WHERE ThucHien.MaBaiHat = %s
        """
        self.cursor.execute(query, (MaBaiHat,))
        return [f"{row['MaCaSi']}-{row['TenCaSi']}" for row in self.cursor.fetchall()]

    def layToanBoTenCaSi(self):
        query = """
            SELECT CaSi.MaCaSi, CaSi.TenCaSi 
            FROM CaSi
        """
        self.cursor.execute(query)
        return [f"{row['MaCaSi']}-{row['TenCaSi']}" for row in self.cursor.fetchall()]

    def themBaiHat(self, baiHat: DTOBaiHat):
        ngay_phat_hanh = baiHat.getNgayPhatHanh()
        try:
            ngay_phat_hanh = datetime.datetime.strptime(ngay_phat_hanh, "%Y-%m-%d").date()
        except ValueError:
            print("Lỗi: Định dạng ngày không hợp lệ! Cần có dạng YYYY-MM-DD.")
            return "Lỗi định dạng ngày"

        query = """
            INSERT INTO BaiHat (MaBaiHat, NgayPhatHanh, TieuDe, AnhBaiHat, MaXuatXu, MaTheLoai, FileNhac)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        try:
            self.cursor.execute(query, (
                baiHat.getMaBaiHat(),
                ngay_phat_hanh,  
                baiHat.getTieuDe(),
                baiHat.getAnh(),
                int(baiHat.getMaXuatXu()),
                int(baiHat.getMaTheLoai()),
                baiHat.getFileNhac()
            ))
            self.conn.commit()
            print("Thêm bài hát thành công!")
            return "Thành công"
        except Exception as e:
            print("Lỗi khi thêm bài hát:", e)
            return str(e)
        
    def layMaBaiHat(self):
        try:
            self.cursor.execute("SELECT COALESCE(MAX(MaBaiHat), 0) + 1 AS NextID FROM baihat")
            result = self.cursor.fetchone()
            if result and "NextID" in result:
                return result["NextID"]
            else:
                return 1
        except Exception as e:
            print("Lỗi:", e)
            return None


    def kiem_tra_trung_bai_hat(self, dto_bai_hat: DTOBaiHat):
        """
        Kiểm tra bài hát với danh sách ca sĩ đã tồn tại trong hệ thống hay chưa.

        :param dto_bai_hat: Đối tượng DTOBaiHat chứa thông tin bài hát cần kiểm tra.
        :return: "Trùng" nếu bài hát + ca sĩ đã tồn tại (không dư, không thiếu), "Hợp lệ" nếu chưa tồn tại.
        """
        tieu_de = dto_bai_hat.getTieuDe()
        danh_sach_ca_si_raw = dto_bai_hat.getCaSi()  # Danh sách ca sĩ dạng "1-Sơn Tùng", "2-Đen"
        
        # Chuyển danh sách ca sĩ thành tập hợp các mã int
        danh_sach_ca_si = {int(ca_si.split('-')[0]) for ca_si in danh_sach_ca_si_raw}

        # Truy vấn tất cả bài hát có cùng tiêu đề trong hệ thống
        query = "SELECT MaBaiHat FROM BaiHat WHERE TieuDe = %s"
        self.cursor.execute(query, (tieu_de,))
        bai_hat_ton_tai = self.cursor.fetchall()  # Danh sách mã bài hát có cùng tiêu đề

        if bai_hat_ton_tai:
            for row in bai_hat_ton_tai:
                ma_bai_hat = row["MaBaiHat"]

                # Lấy danh sách mã ca sĩ đã thực hiện bài hát đó
                query = "SELECT MaCaSi FROM ThucHien WHERE MaBaiHat = %s"
                self.cursor.execute(query, (ma_bai_hat,))
                ca_si_ton_tai = {row["MaCaSi"] for row in self.cursor.fetchall()}  # Chuyển thành tập hợp int

                # Nếu danh sách ca sĩ trùng khớp hoàn toàn, trả về "Trùng"
                if danh_sach_ca_si == ca_si_ton_tai:
                    return "Trùng"

        return "Hợp lệ"


    def themThucHien(self, maBaiHat: int, maCaSi: int):
        try:
            query = """
                INSERT INTO ThucHien (MaBaiHat, MaCaSi) VALUES (%s, %s)
            """
            self.cursor.execute(query, (maBaiHat, maCaSi))
            self.conn.commit()
        except Exception as e:
            print("Lỗi khi thêm thực hiện:", e)

    def xoaBaiHat(self, maBaiHat: str):
        try:
            self.cursor.execute("DELETE FROM BaiHat WHERE MaBaiHat = %s", (maBaiHat,))
            self.conn.commit()
            return "Thành công"
        except Exception as e:
            print("Lỗi khi xóa bài hát:", e)
            return "Thất bại"

    def kiemTraTenTonTai(self, tenBaiHat: str):
        try:
            print(tenBaiHat)
            self.cursor.execute("SELECT COUNT(*) FROM BaiHat WHERE TieuDe = %s", (tenBaiHat,))
            result = self.cursor.fetchone()
            return result[0] > 0
        except Exception as e:
            print("Lỗi khi kiểm tra tên bài hát:", e)
            return False
    def layTenTheLoai(self): 
        query = """
            SELECT MaTheLoai, TenTheLoai 
            FROM theloai
        """
        self.cursor.execute(query)
        return [f"{row['MaTheLoai']}-{row['TenTheLoai']}" for row in self.cursor.fetchall()]
    def layTenXuatXu(self): 
        query = """
            SELECT MaXuatXu, TenXuatXu 
            FROM xuatxu
        """
        self.cursor.execute(query)
        return [f"{row['MaXuatXu']}-{row['TenXuatXu']}" for row in self.cursor.fetchall()]
    
    def xoaBaiHat(self, mabaihat: int):
        try:
            # Xóa bản ghi trong bảng ThucHien liên quan đến bài hát
            self.cursor.execute("DELETE FROM BaiHat WHERE MaBaiHat = %s", (mabaihat,))
            
            # Lưu thay đổi vào database
            self.conn.commit()
            return "Thành công"
        
        except Exception as e:
            print("Lỗi khi xóa bản ghi trong ThucHien:", e)
            return "Thất bại"
        
    def layBaiHatVoiXuatXu(self, maXuatXu: int):
        try:
            query = """
                SELECT baihat.*, xuatxu.TenXuatXu
                FROM baihat
	            LEFT JOIN xuatxu ON baihat.MaXuatXu = xuatxu.MaXuatXu
                WHERE xuatxu.MaXuatXu= %s
            """
            self.cursor.execute(query, (maXuatXu,))
            results = self.cursor.fetchall()
            return results
        except Exception as e:
            print("Lỗi khi lấy bài hát:", e)
            return []
