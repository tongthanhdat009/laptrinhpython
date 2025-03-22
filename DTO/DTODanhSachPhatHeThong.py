from datetime import date, datetime

class DTODanhSachPhatHeThong:
    def __init__(self, MaDanhSachPhat: int, TieuDe: str, MoTa: str, NgayTao: date, Anh: str):
        self._MaDanhSachPhatHeThong = MaDanhSachPhat
        self._TieuDe = TieuDe
        self._MoTa = MoTa
        self._NgayTao = NgayTao if NgayTao else date.today()
        self._Anh = Anh

    # Getter và Setter cho MaDanhSachPhat
    @property
    def MaDanhSachPhat(self):
        return self._MaDanhSachPhatHeThong

    @MaDanhSachPhat.setter
    def MaDanhSachPhat(self, value):
        if isinstance(value, int) and value > 0:
            self._MaDanhSachPhatHeThong = value
        else:
            raise ValueError("Mã danh sách phát phải là số nguyên dương.")

    # Getter và Setter cho TieuDe
    @property
    def TieuDe(self):
        return self._TieuDe

    @TieuDe.setter
    def TieuDe(self, value):
        if isinstance(value, str) and value.strip():
            self._TieuDe = value.strip()
        else:
            raise ValueError("Tiêu đề không được để trống.")

    # Getter và Setter cho MoTa
    @property
    def MoTa(self):
        return self._MoTa

    @MoTa.setter
    def MoTa(self, value):
        if isinstance(value, str):
            self._MoTa = value.strip()
        else:
            raise ValueError("Mô tả phải là chuỗi.")

    # Getter và Setter cho NgayTao
    @property
    def NgayTao(self):
        return self._NgayTao

    @NgayTao.setter
    def NgayTao(self, value):
        if isinstance(value, date):
            self._NgayTao = value
        else:
            raise ValueError("Ngày tạo phải là kiểu date.")

    # Getter và Setter cho Anh
    @property
    def Anh(self):
        return self._Anh

    @Anh.setter
    def Anh(self, value):
        if isinstance(value, str) and value.strip():
            self._Anh = value.strip()
        else:
            raise ValueError("Đường dẫn ảnh không được để trống.")

    # Hàm hiển thị thông tin
    def __str__(self):
        return f"ID: {self._MaDanhSachPhatHeThong}, Tiêu Đề: {self._TieuDe}, Ngày Tạo: {self._NgayTao}, Ảnh: {self._Anh}"
