from DAL.DALBaiHat import DALBaiHat

class BLLQuanLy:
    def __init__(self):
        self.baiHatDAL = DALBaiHat()  # Khởi tạo DALBaiHat

    def layDanhSachBaiHat(self):
        """Lấy danh sách bài hát kèm danh sách ca sĩ."""
        dsBaiHat = self.baiHatDAL.layTatCaBaiHat()

        # Thêm danh sách ca sĩ vào từng bài hát
        for baiHat in dsBaiHat:
            danhSachCaSi = self.baiHatDAL.layTenCaSi(baiHat.getMaBaiHat())  
            baiHat.setCaSi(danhSachCaSi)  # Gán danh sách ca sĩ cho bài hát

        return dsBaiHat
