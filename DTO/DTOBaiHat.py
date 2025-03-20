class DTOBaiHat:
    def __init__(self, MaBaiHat: int, NgayPhatHanh: str, TieuDe: str, Anh: str, MaXuatXu: int, TenXuatXu: str, MaTheLoai: int, TenTheLoai: str, FileNhac: str, CaSi: list):
        self.__MaBaiHat = MaBaiHat
        self.__NgayPhatHanh = NgayPhatHanh
        self.__TieuDe = TieuDe
        self.__Anh = Anh
        self.__MaXuatXu = MaXuatXu
        self.__TenXuatXu = TenXuatXu
        self.__MaTheLoai = MaTheLoai
        self.__TenTheLoai = TenTheLoai
        self.__FileNhac = FileNhac
        self.__CaSi = CaSi  # Danh sách ca sĩ (mảng)

    # Getter
    def getMaBaiHat(self):
        return self.__MaBaiHat

    def getNgayPhatHanh(self):
        return self.__NgayPhatHanh

    def getTieuDe(self):
        return self.__TieuDe

    def getAnh(self):
        return self.__Anh

    def getMaXuatXu(self):
        return self.__MaXuatXu

    def getTenXuatXu(self):
        return self.__TenXuatXu

    def getMaTheLoai(self):
        return self.__MaTheLoai

    def getTenTheLoai(self):
        return self.__TenTheLoai

    def getFileNhac(self):
        return self.__FileNhac

    def getCaSi(self):
        return self.__CaSi

    # Setter
    def setMaBaiHat(self, MaBaiHat: int):
        self.__MaBaiHat = MaBaiHat

    def setNgayPhatHanh(self, NgayPhatHanh: str):
        self.__NgayPhatHanh = NgayPhatHanh

    def setTieuDe(self, TieuDe: str):
        self.__TieuDe = TieuDe

    def setAnh(self, Anh: str):
        self.__Anh = Anh

    def setMaXuatXu(self, MaXuatXu: int):
        self.__MaXuatXu = MaXuatXu

    def setTenXuatXu(self, TenXuatXu: str):
        self.__TenXuatXu = TenXuatXu

    def setMaTheLoai(self, MaTheLoai: int):
        self.__MaTheLoai = MaTheLoai

    def setTenTheLoai(self, TenTheLoai: str):
        self.__TenTheLoai = TenTheLoai

    def setFileNhac(self, FileNhac: str):
        self.__FileNhac = FileNhac

    def setCaSi(self, CaSi: list):
        self.__CaSi = CaSi
    