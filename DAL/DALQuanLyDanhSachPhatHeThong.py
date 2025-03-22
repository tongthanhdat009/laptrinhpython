from DAL.dbconnector import Database
from DTO.DTODanhSachPhatHeThong import DTODanhSachPhatHeThong
from datetime import datetime, date

class DALQuanLyDanhSachPhatHeThong:
    def __init__(self):
        super().__init__()
        # Khởi tạo database
        self.db = Database()  
        self.connection = self.db.connection
        self.cursor = self.db.cursor
        
    def lay_danh_sach_phat_he_thong(self):
        try:
            query = "SELECT MaDanhSachPhatHeThong, TieuDe, MoTa, NgayTao, Anh FROM DanhSachPhatHeThong"
            self.cursor.execute(query)
            rows = self.cursor.fetchall()
            
            if not rows:
                print("⚠️ Không có dữ liệu trong bảng DanhSachPhatHeThong")
                return []
                
            danh_sach = []
            for row in rows:
                ngay_tao = row["NgayTao"]
                if isinstance(ngay_tao, (datetime, date)):
                    ngay_tao = ngay_tao
                
                dto = DTODanhSachPhatHeThong(
                    MaDanhSachPhat=row["MaDanhSachPhatHeThong"],
                    TieuDe=row["TieuDe"],
                    MoTa=row["MoTa"],
                    NgayTao=ngay_tao,
                    Anh=row["Anh"]
                )
                danh_sach.append(dto)
                
            return danh_sach

        except Exception as e:
            print(f"❌ Lỗi SQL: {e}")
            return []