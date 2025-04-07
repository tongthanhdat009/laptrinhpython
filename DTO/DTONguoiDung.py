class DTONguoiDung:
    def __init__(self, ma_nguoi_dung: int, ten_nguoi_dung: str, tai_khoan: str, mat_khau: str, ma_quyen: int, anh: bytes = None, hoat_dong: bool = None):
        self._ma_nguoi_dung = ma_nguoi_dung
        self._ten_nguoi_dung = ten_nguoi_dung
        self._tai_khoan = tai_khoan
        self._mat_khau = mat_khau
        self._ma_quyen = ma_quyen
        self._anh = anh
        self._hoat_dong = hoat_dong
    
    @property
    def ma_nguoi_dung(self):
        return self._ma_nguoi_dung
    
    @ma_nguoi_dung.setter
    def ma_nguoi_dung(self, value):
        self._ma_nguoi_dung = value
    
    @property
    def ten_nguoi_dung(self):
        return self._ten_nguoi_dung
    
    @ten_nguoi_dung.setter
    def ten_nguoi_dung(self, value):
        self._ten_nguoi_dung = value
    
    @property
    def tai_khoan(self):
        return self._tai_khoan
    
    @tai_khoan.setter
    def tai_khoan(self, value):
        self._tai_khoan = value
    
    @property
    def mat_khau(self):
        return self._mat_khau
    
    @mat_khau.setter
    def mat_khau(self, value):
        self._mat_khau = value
    
    @property
    def ma_quyen(self):
        return self._ma_quyen
    
    @ma_quyen.setter
    def ma_quyen(self, value):
        self._ma_quyen = value
    
    @property
    def anh(self):
        return self._anh
    
    @anh.setter
    def anh(self, value):
        self._anh = value
    
    @property
    def hoat_dong(self):
        return self._hoat_dong
    
    @hoat_dong.setter
    def hoat_dong(self, value):
        self._hoat_dong = value
    
    def __repr__(self):
        return f"UserDTO(ma_nguoi_dung={self._ma_nguoi_dung}, ten_nguoi_dung='{self._ten_nguoi_dung}', tai_khoan='{self._tai_khoan}', ma_quyen={self._ma_quyen}, hoat_dong={self._hoat_dong})"
