class DTOCaSi:
    def __init__(self, maCaSi: int, tenCaSi: str, anhCaSi: str, ngheDanh: str = "", ngaySinh: str = "", moTa: str = ""):
        self.__maCaSi = maCaSi
        self.__tenCaSi = tenCaSi
        self.__anhCaSi = anhCaSi
        self.__ngheDanh = ngheDanh
        self.__ngaySinh = ngaySinh
        self.__moTa = moTa

    def getMaCaSi(self) -> int:
        return self.__maCaSi

    def getTenCaSi(self) -> str:
        return self.__tenCaSi

    def getAnhCaSi(self) -> str:
        return self.__anhCaSi

    def setMaCaSi(self, maCaSi: int):
        self.__maCaSi = maCaSi

    def setTenCaSi(self, tenCaSi: str):
        self.__tenCaSi = tenCaSi

    def setAnhCaSi(self, anhCaSi: str):
        self.__anhCaSi = anhCaSi

    def getNgheDanh(self) -> str:
        return self.__ngheDanh

    def getNgaySinh(self) -> str:
        return self.__ngaySinh

    def getMoTa(self) -> str:
        return self.__moTa

    def setNgheDanh(self, ngheDanh: str):
        self.__ngheDanh = ngheDanh

    def setNgaySinh(self, ngaySinh: str):
        self.__ngaySinh = ngaySinh

    def setMoTa(self, moTa: str):
        self.__moTa = moTa

    def __str__(self):
        return f"CaSi(Ma: {self.__maCaSi}, Ten: {self.__tenCaSi}, NgheDanh: {self.__ngheDanh})"
