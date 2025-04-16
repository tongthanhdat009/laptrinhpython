from DAL.DALPhatNhac import DALPhatNhac
class BLLPhatNhac:
    def __init__(self):
        self.phatnhac = DALPhatNhac()
    def luuLichSuNghe(self, idbaihat, idnguoidung):
        self.phatnhac.luuLichSuNghe(idbaihat, idnguoidung)
    def kiemTraTimBaiHat(self, idnguoidung: int, idbaihat: int):
        return self.phatnhac.kiemTraTimBaiHat(idnguoidung, idbaihat)
    def timBaiHat(self, idnguoidung, idbaihat):
        self.phatnhac.timBaiHat(idnguoidung, idbaihat)
    def huyTimBaiHat(self,idnguoidung, idbaihat):
        self.phatnhac.huyTimBaiHat(idnguoidung,idbaihat)
    def layDanhSachPhat(self, idnguoidung: int):
        return self.phatnhac.layDanhSachPhat(idnguoidung)
    def themBaiHatVaoDanhSachPhat(self, idbaihat: int, iddanh_sach_phat: int):
        self.phatnhac.themBaiHatVaoDanhSachPhat(idbaihat, iddanh_sach_phat)
    def taoDanhSachPhat(self, tieu_de: str, mo_ta: str,idnguoidung: int,anh: str):
        return self.phatnhac.taoDanhSachPhat(tieu_de, mo_ta,idnguoidung, anh)
    def layMaDanhSachPhat(self):
        return self.phatnhac.layMaDanhSachPhat()