from datetime import date, datetime

class DTODanhSachPhatHeThong:
    def __init__(self, MaDanhSachPhatHeThong: int, TieuDe: str, MoTa: str, NgayTao: date, TrangThai:bool, Anh: str):
        self.__MaDanhSachPhatHeThong = MaDanhSachPhatHeThong
        self.__TieuDe = TieuDe
        self.__MoTa = MoTa
        self.__NgayTao = NgayTao if NgayTao else date.today()
        self.__TrangThai = TrangThai
        self.__Anh = Anh

    @property
    def TrangThai(self):
        return self.__TrangThai
        
    @TrangThai.setter
    def TrangThai(self, value):
        if isinstance(value, bool):
            self.__TrangThai = value
        else:
            raise ValueError("Trạng thái phải là kiểu boolean.")

    # Getter và Setter cho MaDanhSachPhatHeThong
    @property
    def MaDanhSachPhatHeThong(self):
        return self.__MaDanhSachPhatHeThong

    @MaDanhSachPhatHeThong.setter
    def MaDanhSachPhatHeThong(self, value):
        if isinstance(value, int) and value > 0:
            self.__MaDanhSachPhatHeThong = value
        else:
            raise ValueError("Mã danh sách phát phải là số nguyên dương.")

    # Getter và Setter cho TieuDe
    @property
    def TieuDe(self):
        return self.__TieuDe

    @TieuDe.setter
    def TieuDe(self, value):
        if isinstance(value, str) and value.strip():
            self.__TieuDe = value.strip()
        else:
            raise ValueError("Tiêu đề không được để trống.")

    # Getter và Setter cho MoTa
    @property
    def MoTa(self):
        return self.__MoTa

    @MoTa.setter
    def MoTa(self, value):
        if isinstance(value, str):
            self.__MoTa = value.strip()
        else:
            raise ValueError("Mô tả phải là chuỗi.")

    # Getter và Setter cho NgayTao
    @property
    def NgayTao(self):
        return self.__NgayTao

    @NgayTao.setter
    def NgayTao(self, value):
        if isinstance(value, date):
            self.__NgayTao = value
        else:
            raise ValueError("Ngày tạo phải là kiểu date.")

    # Getter và Setter cho Anh
    @property
    def Anh(self):
        return self.__Anh

    @Anh.setter
    def Anh(self, value):
        if isinstance(value, str) and value.strip():
            self.__Anh = value.strip()
        else:
            raise ValueError("Đường dẫn ảnh không được để trống.")

    # Hàm hiển thị thông tin
    def __str__(self):
        return f"ID: {self.__MaDanhSachPhatHeThong}, Tiêu Đề: {self.__TieuDe}, Ngày Tạo: {self.__NgayTao}, Ảnh: {self.__Anh}"