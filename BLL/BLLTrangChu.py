from DAL.DALQuanLyBaiHat import DALBaiHat

class BLLTrangChu:
    def __init__(self):
        self.dal = DALBaiHat()

    def layBaiHatVoiXuatXu(self, maXuatXu):
        return self.dal.layBaiHatVoiXuatXu(maXuatXu)
