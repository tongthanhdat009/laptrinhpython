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
                Anh=row["Anh"],
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

