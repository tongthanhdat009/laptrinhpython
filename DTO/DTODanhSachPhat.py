import datetime

class DTODanhSachPhat:
    def __init__(self, 
                 ma_danh_sach_phat=0, 
                 tieu_de="", 
                 mo_ta="", 
                 ngay_tao=None, 
                 ma_nguoi_dung=0, 
                 anh=""):
        self._ma_danh_sach_phat = ma_danh_sach_phat
        self._tieu_de = tieu_de
        self._mo_ta = mo_ta
        # Nếu không cung cấp ngay_tao thì dùng ngày hiện tại
        self._ngay_tao = ngay_tao if ngay_tao is not None else datetime.date.today()
        self._ma_nguoi_dung = ma_nguoi_dung
        self._anh = anh

    # Getter và setter cho MaDanhSachPhat
    @property
    def ma_danh_sach_phat(self):
        return self._ma_danh_sach_phat

    @ma_danh_sach_phat.setter
    def ma_danh_sach_phat(self, value):
        self._ma_danh_sach_phat = value

    # Getter và setter cho TieuDe
    @property
    def tieu_de(self):
        return self._tieu_de

    @tieu_de.setter
    def tieu_de(self, value):
        self._tieu_de = value

    # Getter và setter cho MoTa
    @property
    def mo_ta(self):
        return self._mo_ta

    @mo_ta.setter
    def mo_ta(self, value):
        self._mo_ta = value

    # Getter và setter cho NgayTao
    @property
    def ngay_tao(self):
        return self._ngay_tao

    @ngay_tao.setter
    def ngay_tao(self, value):
        if not isinstance(value, datetime.date):
            raise ValueError("NgayTao phải là đối tượng datetime.date")
        self._ngay_tao = value

    # Getter và setter cho MaNguoiDung
    @property
    def ma_nguoi_dung(self):
        return self._ma_nguoi_dung

    @ma_nguoi_dung.setter
    def ma_nguoi_dung(self, value):
        self._ma_nguoi_dung = value

    # Getter và setter cho Anh
    @property
    def anh(self):
        return self._anh

    @anh.setter
    def anh(self, value):
        self._anh = value

    def __str__(self):
        return (f"DTODanhSachPhat(ma_danh_sach_phat={self._ma_danh_sach_phat}, "
                f"tieu_de='{self._tieu_de}', mo_ta='{self._mo_ta}', "
                f"ngay_tao={self._ngay_tao}, ma_nguoi_dung={self._ma_nguoi_dung}, anh='{self._anh}')")
