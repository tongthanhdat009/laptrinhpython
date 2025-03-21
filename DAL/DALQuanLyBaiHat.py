from DTO.DTOBaiHat import DTOBaiHat
from DAL.dbconnector import Database
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
        try:
            query = """
                INSERT INTO BaiHat (MaBaiHat, NgayPhatHanh, TieuDe, AnhBaiHat, MaXuatXu, MaTheLoai, FileNhac)
                VALUES (%s, STR_TO_DATE(%s, '%%Y-%%m-%%d'), %s, %s, %s, %s, %s)
            """
            self.cursor.execute(query, (
                baiHat.getMaBaiHat(),
                baiHat.getNgayPhatHanh(),
                baiHat.getTieuDe(),
                baiHat.getAnh(),
                int(baiHat.getMaXuatXu()),
                int(baiHat.getMaTheLoai()),
                baiHat.getFileNhac()
            ))
            self.conn.commit()
            return "Thành công"  # Trả về ID của bản ghi vừa thêm
        except Exception as e:
            print("Lỗi khi thêm bài hát:", e)
            return str(e)  # Trả về lỗi dưới dạng chuỗi để GUI có thể hiển thị
        
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