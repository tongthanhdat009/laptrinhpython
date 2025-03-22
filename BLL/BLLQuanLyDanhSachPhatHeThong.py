
class BLLQuanLyDanhSachPhatHeThong:
    def __init__(self):
        super().__init__()
        self.dal = DALQuanLyDanhSachPhatHeThong()
    def lay_danh_sach_phat_he_thong(self):
        return self.dal.lay_danh_sach_phat_he_thong()