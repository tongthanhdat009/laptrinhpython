from DAL.DALQuanLyBaiHat import DALBaiHat
from DTO.DTOBaiHat import DTOBaiHat
class BLLQuanLy:
    def __init__(self):
        self.baiHatDAL = DALBaiHat()

    def layDanhSachBaiHat(self):
        dsBaiHat = self.baiHatDAL.layTatCaBaiHat()

        for baiHat in dsBaiHat:
            danhSachCaSi = self.baiHatDAL.layTenCaSi(baiHat.getMaBaiHat())  
            baiHat.setCaSi(danhSachCaSi)  

        return dsBaiHat
    
    def layToanBoTenCaSi(self):
        return self.baiHatDAL.layToanBoTenCaSi()
    
    def layMaBaiHat(self):
        return self.baiHatDAL.layMaBaiHat()
    
    def themBaiHat(self, baiHat: DTOBaiHat):
        if self.baiHatDAL.kiem_tra_trung_bai_hat(baiHat) == "Hợp lệ":
            if self.baiHatDAL.themBaiHat(baiHat) == "Thành công":
                danhSachMaCaSi = [int(caSi.split('-')[0]) for caSi in baiHat.getCaSi()]
                for maCaSi in danhSachMaCaSi:
                    self.baiHatDAL.themThucHien(baiHat.getMaBaiHat(), maCaSi)
                return "Thành công"
        return "Phiên bản bài hát đã tồn tại"
        
    def xoaBaiHat(self, maBaiHat: int):
        return self.baiHatDAL.xoaBaiHat(maBaiHat)
        
    def layTenTheLoai(self):
        return self.baiHatDAL.layTenTheLoai()
        
    def layTenXuatXu(self):
        return self.baiHatDAL.layTenXuatXu()
     def layDanhSachCaSi(self):
        return self.caSiDAL.layDanhSachCaSi()
        
    def themCaSi(self, caSi: DTOCaSi):
        return self.caSiDAL.themCaSi(caSi)
        
    def xoaCaSi(self, maCaSi: int):
        return self.caSiDAL.xoaCaSi(maCaSi)
        
    def capNhatCaSi(self, caSi: DTOCaSi):
        return self.caSiDAL.capNhatCaSi(caSi)
