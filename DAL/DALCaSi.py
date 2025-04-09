from DTO.DTOCaSi import DTOCaSi
from DAL.dbconnector import Database

class DALCaSi:
    def __init__(self):
        db = Database()
        self.conn = db.get_connection()
        self.cursor = db.get_cursor()

    def layDanhSachCaSi(self):
        try:
            self.cursor.execute("SELECT * FROM CaSi")
            results = self.cursor.fetchall()
            danhSachCaSi = []
            for row in results:
                caSi = DTOCaSi(
                    maCaSi=row["MaCaSi"],
                    tenCaSi=row["TenCaSi"],
                    ngheDanh=row["NgheDanh"],
                    ngaySinh=row["NgaySinh"],
                    moTa=row["MoTa"],
                    anhCaSi=row["AnhCaSi"]
                )
                danhSachCaSi.append(caSi)
            return danhSachCaSi
        except Exception as e:
            print("Lỗi khi lấy danh sách ca sĩ:", e)
            return []

    def themCaSi(self, caSi: DTOCaSi):
        try:
            query = """
                INSERT INTO CaSi (TenCaSi, NgheDanh, NgaySinh, MoTa, AnhCaSi)
                VALUES (%s, %s, %s, %s, %s)
            """
            self.cursor.execute(query, (
                caSi.getTenCaSi(),
                caSi.getNgheDanh(),
                caSi.getNgaySinh(),
                caSi.getMoTa(),
                caSi.getAnhCaSi()
            ))
            self.conn.commit()
            return "Thành công"
        except Exception as e:
            print("Lỗi khi thêm ca sĩ:", e)
            return str(e)

    def xoaCaSi(self, maCaSi: int):
        try:
            # First delete any ThucHien records for this singer
            self.cursor.execute("DELETE FROM ThucHien WHERE MaCaSi = %s", (maCaSi,))
            
            # Then delete the singer record
            self.cursor.execute("DELETE FROM CaSi WHERE MaCaSi = %s", (maCaSi,))
            
            self.conn.commit()
            return "Thành công"
        except Exception as e:
            print("Lỗi khi xóa ca sĩ:", e)
            return str(e)

    def layToanBoTenCaSi(self):
        query = """
            SELECT CaSi.MaCaSi, CaSi.TenCaSi 
            FROM CaSi
        """
        self.cursor.execute(query)
        return [f"{row['MaCaSi']}-{row['TenCaSi']}" for row in self.cursor.fetchall()]

    def capNhatCaSi(self, caSi: DTOCaSi):
        try:
            query = """
                UPDATE CaSi 
                SET TenCaSi = %s,
                    NgheDanh = %s,
                    NgaySinh = %s,
                    MoTa = %s,
                    AnhCaSi = %s
                WHERE MaCaSi = %s
            """
            self.cursor.execute(query, (
                caSi.getTenCaSi(),
                caSi.getNgheDanh(),
                caSi.getNgaySinh(),
                caSi.getMoTa(),
                caSi.getAnhCaSi(),
                caSi.getMaCaSi()
            ))
            self.conn.commit()
            return "Thành công"
        except Exception as e:
            print("Lỗi khi cập nhật ca sĩ:", e)
            return str(e)
