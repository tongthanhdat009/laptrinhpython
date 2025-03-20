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

    def themBaiHat(self, baiHat: DTOBaiHat):
        if not self.baiHatDAL.kiemTraTenTonTai(baiHat.getTieuDe()):
            maBaiHat = self.baiHatDAL.themBaiHat(baiHat)
            if maBaiHat:
                danhSachMaCaSi = [int(caSi.split('-')[0]) for caSi in baiHat.getCaSi()]
                for maCaSi in danhSachMaCaSi:
                    self.baiHatDAL.themThucHien(maBaiHat, maCaSi)
                    
                return "Thành công"
        return "Tên bài hát đã tồn tại"
    def xoaBaiHat(self, maBaiHat: int):
        return self.baiHatDAL.xoaBaiHat(maBaiHat)
    def layTenTheLoai(self):
        return self.baiHatDAL.layTenTheLoai()
    def layTenXuatXu(self):
        return self.baiHatDAL.layTenXuatXu()